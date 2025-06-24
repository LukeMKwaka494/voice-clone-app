import streamlit as st
from pathlib import Path

st.set_page_config(page_title="PNG 50th Voice App")
st.title("🇵🇬 PNG 50th Anniversary Voice App")
st.markdown("**Powered by Pulse of PNG Voice**")

voice_path = Path("assets/pulse_of_png_clone_voice.wav")

if voice_path.exists():
    st.audio(voice_path.read_bytes(), format="audio/wav")
else:
    st.error("Voice file not found.")

st.text_area("Type something you'd like the voice to say:", placeholder="Your message here...")
