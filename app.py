import streamlit as st
import openai 
import os
st.title("TransformAI")
openai.api_key=os.getenv("KEY")
lang=st.selectbox("Choose language:",["English",
        "हिंदी",           # Hindi
        "Español",         # Spanish
        "Français",        # French
        "Deutsch",         # German
        "中文",             # Chinese
        "日本語",           # Japanese
        "한국어",           # Korean
        "Русский",         # Russian
        "اردو",            # Urdu
        "বাংলা",           # Bengali
        "తెలుగు",         # Telugu
        "தமிழ்",           # Tamil
        "ગુજરાતી",         # Gujarati
        "मराठी",           # Marathi
        "ਪੰਜਾਬੀ",          # Punjabi
        "ಕನ್ನಡ",           # Kannada
        "मारवाड़ी",        # Marwari
        "O‘zbekcha",       # Uzbek
        "ქართული",         # Georgian
        "العربية",         # Arabic
        "Türkçe",          # Turkish
        "ภาษาไทย",         # Thai
        "فارسی",           # Persian
        "Shqip",           # Albanian
        "Nederlands",      # Dutch
        "Svenska",         # Swedish
        "Italiano",        # Italian
        "Việt",            # Vietnamese
        "ລາວ"              # Lao
])
txt=st.text_area("paste your text here")
outpt=st.selectbox(
    "Choose output type:",
    ["Summary", "Quiz", "Test", "Video", "Audio", "Animation", "Translation"])
if st.button("Generate"):
    st.write(f"Language: {lang}")
    st.write(f"Output type: {outpt}")
    st.write("This is where the AI output will appear")