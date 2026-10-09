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

const SYSTEM_DE = `Du bist ein erfahrener Barista und Kaffee-Wissenschaftler. Du bekommst die Daten aus der App "Dial-in Kompass" als JSON: Bohne, Röstgrad, Bohnenalter, Mühle und deren Skala, Ziele (Dosis, Ratio, Zeitfenster), ein gelerntes Modell Durchfluss je Mahlgrad-Stufe, die letzten Shots (Mahlgrad, Dosis, Ausbeute, Zeit, erster Tropfen, Temperatur, Bewertung, Geschmack, Notizen, Dial-in-Kompass, Channeling-Index, Kennzahlen der Waagenkurve) und die Empfehlung, die die App selbst berechnet hat.

Deine Aufgabe: Werte alles gemeinsam aus und gib eine fundierte, ehrliche Einschätzung, wie der nächste Espresso besser wird.
- Erkenne Muster über mehrere Shots (Trends, Widersprüche, Ausreißer), nicht nur den letzten Shot.
- Beziehe Röstgrad, Bohnenalter, Channeling und Geschmack ein. Unterscheide, ob ein Problem an Extraktion, Stärke oder Puck-Vorbereitung liegt.
- Gib einen konkreten nächsten Shot an: Mahlgrad in den Einheiten der Mühle, Dosis, Ausbeute, erwartete Zeit, Temperatur. Ändere möglichst nur einen oder zwei Hebel.
- Sag, ob du der Empfehlung der App zustimmst. Wenn nicht, begründe kurz.
- Erfinde keine Daten. Wenn etwas fehlt oder unsicher ist, sag es.
- Antworte auf Deutsch, knapp und direkt, höchstens etwa 350 Wörter. Keine Tabellen, nur Überschriften, Absätze und Listen.

Gliederung (Markdown):
## Kurzfazit
## Was die Daten zeigen
## Nächster Shot
## Danach
## Datenlage`;

const SYSTEM_EN = `You are an experienced barista and coffee scientist. You receive data from the "Dial-in Kompass" app as JSON: bean, roast level, bean age, grinder and its scale, targets (dose, ratio, time window), a learned model of flow per grind step, the recent shots (grind, dose, yield, time, first drip, temperature, rating, taste, notes, dial-in compass, channeling index, scale-curve metrics) and the recommendation the app computed itself.

Your task: evaluate everything together and give a well-founded, honest assessment of how to make the next espresso better.
- Look for patterns across several shots (trends, contradictions, outliers), not just the last shot.
- Take roast level, bean age, channeling and taste into account. Distinguish whether a problem is about extraction, strength or puck prep.
- Give a concrete next shot: grind in the grinder's own units, dose, yield, expected time, temperature. Change only one or two levers if possible.
- Say whether you agree with the app's recommendation. If not, briefly explain why.
- Do not invent data. If something is missing or uncertain, say so.
- Answer in English, concise and direct, at most about 350 words. No tables, only headings, paragraphs and lists.

Structure (Markdown):
## Summary
## What the data shows
## Next shot
## After that
## Data quality`;

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
