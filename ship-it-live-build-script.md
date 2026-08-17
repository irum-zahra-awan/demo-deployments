# "Ship It" — Live Build Script
### GDG Cloud × League of Launchers · 19 August 2026

**Demo concept (built twice):** a tiny tool that takes a one-line rough idea and returns (1) a sharper problem statement and (2) a suggested first person to test it on. One API call, ~15 lines of logic — small enough to build live twice in one session, on-topic for a bootcamp about shipping.

---

## Part 1 — Streamlit → Streamlit Community Cloud (35 min)

**Audience:** CS/Python teams already using Streamlit.
**Outcome:** a public URL, deployed from GitHub, with the API key handled safely.

### Setup (before session)
- A GitHub account, signed in
- A free Gemini API key (aistudio.google.com → Get API key)
- Python + `streamlit`, `google-generativeai` installed locally, or use GitHub Codespaces if laptops are a mess

### Steps to narrate live

1. **Write the app (`app.py`)** — keep it visibly short, this is the point:
   - Text input for the rough idea
   - One call to the Gemini API with a fixed prompt template asking for a sharper problem statement + a suggested first test user
   - Display the result with `st.write`

2. **Secrets, not hardcoded keys** — this is the teaching moment for the "sharing safely" gap:
   - Locally: `.streamlit/secrets.toml`, read via `st.secrets["GEMINI_API_KEY"]`
   - Explicitly show what NOT to do: pasting the key straight into `app.py`
   - Add `.streamlit/secrets.toml` to `.gitignore` before the first commit — narrate this out loud, it's the step people skip

3. **Push to GitHub**
   - New public repo, push `app.py`, `requirements.txt`, `.gitignore`
   - Confirm the key file did *not* get pushed (`git status` / check on GitHub)

4. **Deploy on Streamlit Community Cloud**
   - share.streamlit.io → New app → pick the repo/branch/file
   - Add the secret in the app's Settings → Secrets (paste the same `GEMINI_API_KEY = "..."` there — this is where it lives in production, not in the repo)
   - Deploy → wait ~1–2 min → live URL

5. **Test it on the projector** — open the URL on a phone in the room, type a rough idea, show the output live. This is the "put it in someone's hands" moment, made literal.

### Known snags to pre-empt
- Free tier sleeps after inactivity — first load after idle can take 20–30 sec. Mention this so nobody panics mid-demo.
- `requirements.txt` version mismatches — pin versions if a package errors on deploy.
- Gemini free-tier rate limits — mention roughly what breaks at high traffic (ties to "what it costs to run" gap).

---

## Part 2 — Google AI Studio → Export & Publish (35 min)

**Audience:** no-code / vibe-coding teams.
**Outcome:** the same concept, shipped without writing code, via AI Studio's native publish flow.

> **Before this block:** confirm with Naqi Rizvi whether his 4 Aug session already covered export/publish specifically. If it did, shorten this to a fast recap + focus session time on Q&A/troubleshooting instead of a full rebuild.

### Steps to narrate live

1. **Build the same concept in AI Studio's app builder**
   - Prompt describing the tool: takes a rough idea, returns a sharper problem statement + suggested first test user
   - Keep the interface to a single input box and output panel — mirror the Streamlit version so the comparison is obvious

2. **Test inside AI Studio** before publishing — same idea input as the Streamlit demo, so the room can compare outputs side by side.

3. **Export & Publish**
   - Use AI Studio's built-in publish flow to get a live link
   - Show where the API key lives in this flow (AI Studio manages it — call out the contrast with the manual secrets handling in Part 1, since that difference is exactly what "no-code vs code" means in practice)

4. **Test it on the projector** — same phone-in-the-room moment as Part 1.

### Known snags to pre-empt
- Publish flow may require a Google account with billing awareness even on free tier — check this beforehand so it's not a surprise live.
- Free-tier quota ceiling — same "what breaks at scale" conversation as Part 1.

---

## Part 3 — Free-Tier Reality Check (15 min)

Quick, direct, no slides:
- Streamlit Community Cloud: sleep-on-inactivity, resource limits
- AI Studio / Gemini API: request-per-minute caps on free tier
- Supabase/Firebase free tier as the next step up if a team needs real persisted data or accounts (mention only — not a build)
- One line on "don't commit your key" as a recap, since it's the single most common way a team's demo breaks in front of a judge

## Part 4 — Open Lab (25 min)

Teams deploy their own project with you and any co-trainers circulating. Meet room: open a breakout or a running thread so remote builders aren't stuck watching. Priority: unblock anyone within 5–10 minutes of getting stuck, don't let one team eat the whole lab.

---

### Closing line for the room
Narrow and shipped beats ambitious and unfinished. The checkpoint needs a link and a stranger who used it while you watched — not a better idea.
