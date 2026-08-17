# Idea Sharpener — Streamlit Demo

The "Ship It" session demo app. Takes a one-line idea, returns a sharper
problem statement and a suggested first test user.

## Run it locally (test before the session)

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# edit .streamlit/secrets.toml and paste in a real Gemini API key
streamlit run app.py
```

Get a free Gemini API key at https://aistudio.google.com → "Get API key".

## Deploy live in the session

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Idea Sharpener demo"
   git branch -M main
   git remote add origin <your-empty-github-repo-url>
   git push -u origin main
   ```
   Confirm `secrets.toml` is NOT in the repo (only `secrets.toml.example` should show up on GitHub).

2. **Deploy on Streamlit Community Cloud**
   - Go to https://share.streamlit.io
   - "New app" → pick the repo, branch `main`, file `app.py`
   - Before/after deploying, open **Settings → Secrets** and paste:
     ```
     GEMINI_API_KEY = "your-real-key"
     ```
   - Deploy. First load can take 20-60 seconds.

3. **Test on a phone** in front of the room — that's the demo.

## Notes for the live narration

- Point out `.gitignore` before the first commit — this is the "don't leak your key" moment.
- The Secrets box on Streamlit Cloud is the production equivalent of the local `secrets.toml` — same value, different place.
- Free tier sleeps after inactivity. Mention it so a slow first load doesn't look like a failure.
