/* Dial-in Kompass – Service Worker
   Seiten: zuerst Netzwerk (damit Updates sofort ankommen), offline aus dem Cache.
   Bibliotheken, Schriften, Icons: aus dem Cache, im Hintergrund aktualisiert. */
const CACHE = 'dial-in-v15';
const CORE = ['/', '/en/', '/manifest.webmanifest', '/en/manifest.webmanifest', '/icons/icon-180.png', '/icons/icon-192.png', '/icons/icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if(req.method !== 'GET') return;
  const url = new URL(req.url);
  if(url.hostname === 'visualizer.coffee' || url.hostname.endsWith('.supabase.co')) return;   // Sync und Konto nie cachen
  if(req.mode === 'navigate'){
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match(url.pathname.startsWith('/en') ? '/en/' : '/'))));
    return;
  }
  const cacheable = url.origin === location.origin || /cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|fonts\.(googleapis|gstatic)\.com/.test(url.hostname);
  if(!cacheable) return;
  e.respondWith(caches.match(req).then(hit => {
    const net = fetch(req).then(res => { if(res && (res.ok || res.type === 'opaque')){ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return res; }).catch(() => hit);
    return hit || net;
  }));
});
