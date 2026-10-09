// KI-Analyse für den Dial-in Kompass.
// Prüft den angemeldeten Nutzer, begrenzt die Läufe pro Tag und fragt die Claude API.
// Secrets: ANTHROPIC_API_KEY (Pflicht), ANTHROPIC_MODEL (optional), AI_DAILY_LIMIT (optional, Standard 20)
import { createClient } from "jsr:@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors, "Content-Type": "application/json" } });

const SYSTEM_DE = `Du bist ein erfahrener Barista und Kaffee-Wissenschaftler. Du bekommst die Daten aus der App "Dial-in Kompass" als JSON: Bohne, Röstgrad, Bohnenalter, Öffnung der Packung, Mühle und deren Skala, Maschine, Ziele (Dosis, Ratio, Zeitfenster), das gelernte Modell der App (Durchfluss je Mahlgrad-Stufe und erwartete Zeiten je Mahlgrad), die letzten Shots (Mahlgrad, Dosis, Ausbeute, Zeit, erster Tropfen, Temperatur, Bewertung, Geschmack, Notizen, Dial-in-Kompass, Channeling-Index mit Belegen, Kennzahlen der Waagenkurve) und die Empfehlung, die die App selbst berechnet hat.

Deine Rolle: Du prüfst und ergänzt die App, du ersetzt sie nicht.
- Die Zahlen der App sind die Grundlage: erwartete Zeiten je Mahlgrad, Channeling-Index samt Belegen, Kompass. Rechne sie nicht neu und widersprich ihnen nicht ohne konkreten Datenpunkt.
- Die Empfehlung der App ist der Ausgangspunkt. Bestätige sie, wenn die Daten nicht klar dagegen sprechen. Weiche nur ab, wenn du einen konkreten Shot oder Wert als Beleg nennen kannst, und dann höchstens um eine Mahlgrad-Stufe oder bei einem einzigen Hebel.
- Ergänze, was die App nicht sieht: Muster über mehrere Shots, Notizen, erster Shot des Tages, Packung frisch geöffnet, Widersprüche in den Angaben.
- Channeling nur behaupten, wenn die Kurve es belegt. Hinweise nur aus Geschmack sind schwach.
- Schlage nur Temperaturen vor, die die Maschine einstellen kann.
- Erfinde keine Daten. Antworte auf Deutsch, knapp und direkt, höchstens etwa 300 Wörter. Keine Tabellen, nur Überschriften, Absätze und Listen.

Gliederung (Markdown):
## Abgleich mit der App
(ein bis zwei Sätze: zugestimmt oder angepasst, und warum)
## Was die Daten zeigen
## Nächster Shot
## Danach
## Datenlage

Schließe mit genau einem JSON-Codeblock für die App, ohne weiteren Text danach:
\`\`\`json
{"agree": true, "grind": "8,2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "ein kurzer Satz"}
\`\`\`
"agree" ist true, wenn dein nächster Shot der Empfehlung der App entspricht.`;

const SYSTEM_EN = `You are an experienced barista and coffee scientist. You receive data from the "Dial-in Kompass" app as JSON: bean, roast level, bean age, bag opening, grinder and its scale, machine, targets (dose, ratio, time window), the app's learned model (flow per grind step and expected times per grind setting), the recent shots (grind, dose, yield, time, first drip, temperature, rating, taste, notes, dial-in compass, channeling index with evidence, scale-curve metrics) and the recommendation the app computed itself.

Your role: you review and complement the app, you do not replace it.
- The app's numbers are the basis: expected times per grind setting, channeling index with its evidence, compass. Do not recompute them and do not contradict them without a concrete data point.
- The app's recommendation is the starting point. Confirm it unless the data clearly speaks against it. Deviate only if you can name a concrete shot or value as evidence, and then by at most one grind step or on a single lever.
- Add what the app cannot see: patterns across several shots, notes, first shot of the day, freshly opened bag, contradictions in the inputs.
- Only claim channeling if the curve shows it. Signs from taste alone are weak.
- Only suggest temperatures the machine can actually set.
- Do not invent data. Answer in English, concise and direct, at most about 300 words. No tables, only headings, paragraphs and lists.

Structure (Markdown):
## Check against the app
(one or two sentences: agreed or adjusted, and why)
## What the data shows
## Next shot
## After that
## Data quality

End with exactly one JSON code block for the app, with no text after it:
\`\`\`json
{"agree": true, "grind": "8.2", "dose": 18, "yield": 36, "timeSec": 23, "temp": "92 °C", "reason": "one short sentence"}
\`\`\`
"agree" is true if your next shot matches the app's recommendation.`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return json({ error: "method" }, 405);
  try {
    const key = Deno.env.get("ANTHROPIC_API_KEY");
    if (!key) return json({ error: "no_key" }, 503);
    const model = Deno.env.get("ANTHROPIC_MODEL") || "claude-haiku-5-5";
    const daily = Number(Deno.env.get("AI_DAILY_LIMIT") || 20);

    const jwt = (req.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
    const admin = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
    const { data: u, error: authErr } = await admin.auth.getUser(jwt);
    const user = u?.user;
    if (authErr || !user) return json({ error: "auth" }, 401);

    const since = new Date(Date.now() - 24 * 3600 * 1000).toISOString();
    const { count } = await admin.from("ai_runs").select("id", { count: "exact", head: true }).eq("user_id", user.id).gte("created_at", since);
    const used = count ?? 0;
    if (used >= daily) return json({ error: "limit", limit: daily }, 429);

    const body = await req.json().catch(() => ({}));
    const lang = body?.lang === "en" ? "en" : "de";
    const payload = JSON.stringify(body?.data ?? {});
    if (payload.length > 80000) return json({ error: "too_large" }, 413);

    const r = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
      body: JSON.stringify({
        model,
        // Die 5.5-Modelle denken adaptiv; das Denken zählt zu max_tokens. Niedriger Aufwand hält es kurz und günstig.
        max_tokens: 8000,
        output_config: { effort: "low" },
        system: lang === "en" ? SYSTEM_EN : SYSTEM_DE,
        messages: [{ role: "user", content: (lang === "en" ? "Here is my data:" : "Hier sind meine Daten:") + "\n\n```json\n" + payload + "\n```" }],
      }),
    });
    const out = await r.json().catch(() => ({}));
    if (!r.ok) return json({ error: "upstream", status: r.status, detail: String(out?.error?.message || "").slice(0, 300) }, 502);
    const text = (out.content || []).filter((c: { type: string }) => c.type === "text").map((c: { text: string }) => c.text).join("\n").trim();

    await admin.from("ai_runs").insert({ user_id: user.id, model, tokens_in: out.usage?.input_tokens ?? null, tokens_out: out.usage?.output_tokens ?? null });
    if (!text) return json({ error: "empty", stop: out.stop_reason ?? null }, 502);
    return json({ text, model, left: Math.max(0, daily - used - 1), limit: daily });
  } catch (e) {
    return json({ error: "server", detail: String(e).slice(0, 200) }, 500);
  }
});
