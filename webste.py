import streamlit as st
import google.generativeai as genai
import os
from gtts import gTTS
import tempfile

st.title("TransformAI")
genai.configure(api_key=os.getenv("KEY"))

lang_codes = {
    "English": "en", "हिंदी": "hi", "Español": "es", "Français": "fr", "Deutsch": "de",
    "中文": "zh", "日本語": "ja", "한국어": "ko", "Русский": "ru", "اردو": "ur",
    "বাংলা": "bn", "తెలుగు": "te", "தமிழ்": "ta", "ગુજરાતી": "gu", "मराठी": "mr",
    "ਪੰਜਾਬੀ": "pa", "ಕನ್ನಡ": "kn", "मारवाड़ी": "rwr", "O‘zbekcha": "uz", "ქართული": "ka",
    "العربية": "ar", "Türkçe": "tr", "ภาษาไทย": "th", "فارسی": "fa", "Shqip": "sq",
    "Nederlands": "nl", "Svenska": "sv", "Italiano": "it", "Việt": "vi", "ລາວ": "lo"
}

lang = st.selectbox("Choose language:", list(lang_codes.keys()))
txt = st.text_area("Paste your text here")
outpt = st.selectbox(
    "Choose output type:",
    ["Summary", "Quiz", "Test", "Audio"]
)

# Initialize session states
if "sp_state" not in st.session_state:
    st.session_state.sp_state = False
if "result" not in st.session_state:
    st.session_state.result = ""

# Generate output
if st.button("Generate"):
    if txt.strip() == "":
        st.warning("Please enter some text to generate output.")
    else:
        prompt = f"Please generate a {outpt} of the following text in {lang}:\n\n{txt}"

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        st.session_state.result = response.candidates[0].content.parts[0].text

        st.subheader("Output:")
        st.subheader("Try clicking the speaker as given below")
        st.write(st.session_state.result)
if st.session_state.result:
    st.write(st.session_state.result)
if st.button("🔊 Listen") and st.session_state.result != "":
    st.session_state.sp_state = True
if st.session_state.sp_state:
    speech = st.selectbox("Choose speech language:", list(lang_codes.keys()))
    if speech != lang:
        translate_prompt = f"Translate the following text to {speech}:\n\n{st.session_state.result}"
        translate_model = genai.GenerativeModel("gemini-1.5-flash")
        translate_response = translate_model.generate_content(translate_prompt)
        text_for_tts = translate_response.candidates[0].content.parts[0].text
    else:
        text_for_tts = st.session_state.result

    tts = gTTS(text=text_for_tts, lang=lang_codes[speech])
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tts.save(tmp.name + ".mp3")
        au = tmp.name + ".mp3"
        st.audio(au, format="audio/mp3")
