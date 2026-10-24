/* Shared helpers for Scouting Out Scouts pages. */
(function () {
  // Only links to these official Scouting sites are ever shown from data.json, whatever it says.
  // Keep this list in sync with tools/check_data.py.
  const APPROVED = ["scouting.org", "scoutingevent.com", "247scouting.com", "summitbsa.org", "nesa.org",
    "baltimorescouting.org", "broadcreekscouting.org", "ncacscouting.org", "gotosnyder.org",
    "delmarvacouncil.org", "sacscouting.org", "newbirthoffreedom.org", "padutchbsa.org", "cccbsa.org",
    "hovc.org", "scoutingphilly.org", "virginiaheadwaters.org", "oa-scouting.org", "nentico.org"];

  function safeUrl(u) {
    try {
      const url = new URL(u);
      if (url.protocol !== "https:" && url.protocol !== "http:") return null;
      const h = url.hostname.toLowerCase();
      return APPROVED.some(d => h === d || h.endsWith("." + d)) ? url.href : null;
    } catch (e) { return null; }
  }
  function el(tag, cls, text) {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function linkOrNote(u, cls, text) {
    const href = safeUrl(u);
    if (!href) return el("span", "small", "Link pending review");
    const a = el("a", cls, text); a.href = href; a.target = "_blank"; a.rel = "noopener noreferrer";
    return a;
  }
  function parse(iso) {
    if (!iso) return null;
    const [y, m, d] = iso.split("-").map(Number);
    return new Date(y, m - 1, d);
  }
  const MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  const MONTHS_LONG = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  function fmtDate(iso) { const d = parse(iso); return d ? MONTHS_LONG[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear() : ""; }
  function today() { const t = new Date(); return new Date(t.getFullYear(), t.getMonth(), t.getDate()); }
  function loadData() {
    return fetch("data.json", { cache: "no-cache" }).then(r => { if (!r.ok) throw new Error(r.status); return r.json(); });
  }

  window.SOS = { APPROVED, safeUrl, el, linkOrNote, parse, MONTHS, MONTHS_LONG, fmtDate, today, loadData };
})();
