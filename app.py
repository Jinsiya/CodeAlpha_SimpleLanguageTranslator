import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import json
import pyperclip
from datetime import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* Global Styles */
.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #1a1f35 100%);
    color: #e2e8f0;
}

/* Hide default Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Container */
.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

/* Glass Morphism Card - NO EMPTY BOXES */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
}

/* Title Styles */
.title-container {
    text-align: center;
    margin-bottom: 30px;
}

.glow-title {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(135deg, #818cf8, #6366f1, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

.subtitle {
    color: #94a3b8;
    font-size: 16px;
    font-weight: 300;
}

/* Input Area - NO EMPTY SPACE */
.stTextArea {
    margin-bottom: 0 !important;
}

.stTextArea > div > div > textarea {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 15px !important;
    color: #e2e8f0 !important;
    font-size: 16px !important;
    padding: 15px !important;
    min-height: 100px !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
}

/* Labels - COMPACT */
.stTextArea label, .stSelectbox label {
    color: #94a3b8 !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    margin-bottom: 5px !important;
    display: block !important;
}

/* Select Box - COMPACT */
.stSelectbox {
    margin-top: 15px !important;
    margin-bottom: 20px !important;
}

.stSelectbox > div > div {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 15px !important;
    color: #e2e8f0 !important;
}

/* Translate Button */
.stButton {
    margin-top: 5px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #6366f1, #3b82f6) !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    padding: 12px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
}

/* Output Section - NO EMPTY BOXES */
.output-container {
    background: rgba(30, 41, 59, 0.6) !important;
    border-radius: 15px !important;
    padding: 15px !important;
    border: 1px solid rgba(99, 102, 241, 0.2) !important;
    margin: 15px 0 !important;
}

.output-text {
    font-size: 18px !important;
    color: #e2e8f0 !important;
    padding: 10px !important;
    background: rgba(0, 0, 0, 0.2) !important;
    border-radius: 10px !important;
    margin: 0 !important;
}

/* Success message - COMPACT */
.stSuccess {
    background: rgba(34, 197, 94, 0.1) !important;
    border: 1px solid rgba(34, 197, 94, 0.2) !important;
    border-radius: 12px !important;
    padding: 10px 15px !important;
    margin: 0 0 10px 0 !important;
    color: #4ade80 !important;
}

/* Action Buttons - COMPACT */
.action-btn {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    padding: 8px !important;
}

/* Audio Player - COMPACT */
.audio-container {
    margin: 0 !important;
    padding: 0 !important;
}

audio {
    width: 100% !important;
    margin: 5px 0 !important;
}

.caption-text {
    color: #94a3b8 !important;
    font-size: 12px !important;
    text-align: center !important;
    margin: 0 !important;
}

/* History Section */
.history-title {
    color: #94a3b8;
    font-size: 20px;
    font-weight: 600;
    margin: 25px 0 15px 0;
}

.history-item {
    background: rgba(30, 41, 59, 0.5) !important;
    border-left: 3px solid #6366f1 !important;
    border-radius: 12px !important;
    padding: 12px 16px !important;
    margin-bottom: 10px !important;
}

.history-label {
    color: #94a3b8 !important;
    font-size: 11px !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    margin: 0 !important;
}

.history-text {
    color: #e2e8f0 !important;
    font-size: 14px !important;
    margin: 3px 0 !important;
}

.history-lang {
    display: inline-block !important;
    background: rgba(99, 102, 241, 0.2) !important;
    padding: 2px 12px !important;
    border-radius: 20px !important;
    font-size: 12px !important;
    color: #818cf8 !important;
}

/* Divider */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.2), transparent);
    margin: 25px 0;
}

/* Fix spacing */
.element-container {
    margin: 0 !important;
    padding: 0 !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="title-container">
    <div class="glow-title">🌍 AI Translator</div>
    <div class="subtitle">Instant Translation • Voice Output • History</div>
</div>
""", unsafe_allow_html=True)

# ---------- LANGUAGES ----------
languages = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

# ---------- HISTORY ----------
HISTORY_FILE = "history.json"

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

# ---------- INPUT SECTION ----------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Input Area
text = st.text_area("✍️ Enter text to translate", height=100, placeholder="Type or paste your text here...")

# Language Selection
lang_name = st.selectbox("🎯 Select Target Language", list(languages.keys()))
lang_code = languages[lang_name]

# Translate Button
translate_btn = st.button("🚀 Translate", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- OUTPUT SECTION ----------
if translate_btn and text.strip():
    try:
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        # Success message
        st.success("✅ Translation complete!")
        
        # Output text
        st.markdown('<div class="output-container">', unsafe_allow_html=True)
        st.markdown(f'<div class="output-text">{translated}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📋 Copy Text", use_container_width=True):
                pyperclip.copy(translated)
                st.toast("✨ Copied to clipboard!", icon="✅")
        
        with col2:
            tts = gTTS(translated)
            tts.save("output.mp3")
            audio_file = open("output.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")
            st.caption("🔊 Click play to listen")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Save history
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
        
        history.append({
            "input": text,
            "output": translated,
            "lang": lang_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=4)
            
    except Exception as e:
        st.error(f"Translation error: {str(e)}")

# ---------- DIVIDER ----------
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ---------- HISTORY SECTION ----------
st.markdown('<div class="history-title">📜 Recent Translations</div>', unsafe_allow_html=True)

with open(HISTORY_FILE, "r") as f:
    history = json.load(f)

if history:
    for item in reversed(history[-5:]):
        st.markdown(f"""
        <div class="history-item">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                <span class="history-lang">{item['lang']}</span>
                <span style="color: #64748b; font-size: 10px;">{item.get('timestamp', '')}</span>
            </div>
            <div style="margin-top: 3px;">
                <div class="history-label">Input</div>
                <div class="history-text">{item['input'][:80]}{'...' if len(item['input']) > 80 else ''}</div>
            </div>
            <div style="margin-top: 3px;">
                <div class="history-label">Translation</div>
                <div class="history-text" style="color: #818cf8;">{item['output'][:80]}{'...' if len(item['output']) > 80 else ''}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("💡 No translations yet. Start translating to see history here!")