# AI Studio Demo — Build Prompt

Paste this into AI Studio's app builder to create the same tool as the
Streamlit demo, so the room can compare outputs side by side.

## App description to enter in AI Studio

```
Build a single-page app called "Idea Sharpener".

It has one text input where a user types a rough, one-line startup idea,
and one button labeled "Sharpen it".

When clicked, send the idea to the model with this instruction:

"You are a sharp startup mentor helping a builder at a bootcamp turn a
rough one-line idea into something they can test with a real person this
week. Rough idea: {idea}. Respond in exactly this format, nothing else:
Problem statement: <one clear sentence naming the specific person and the
specific problem they have, not a description of the solution>
First test user: <one concrete suggestion for who to show this to in the
next 48 hours — be specific about where to find them, not a vague persona>"

Display the model's response below the button, formatted clearly with the
two labeled sections. Keep the interface minimal — one input, one button,
one output area. No extra fields.
```

## Steps to narrate live

1. Paste the app description above into AI Studio's builder.
2. Test it inside AI Studio first — use the *same* example idea you used
   in the Streamlit demo (e.g. "an app that helps students find study
   partners") so the room can compare the two outputs directly.
3. Use **Export & Publish** to get a live link.
4. Open the link on a phone in front of the room — same moment as the
   Streamlit demo.

## Talking point for the contrast

In the Streamlit version, you manually created a `secrets.toml` and pasted
it into Streamlit Cloud's Secrets settings — you were responsible for the
API key end to end. In AI Studio, the key is handled by the platform when
you publish. Same idea, two completely different amounts of manual work —
that's the real difference between the code and no-code paths, not just
"one has a text editor and one doesn't."
