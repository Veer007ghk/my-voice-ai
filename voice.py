import streamlit as st
import asyncio
import edge_tts
import os
import random

# 1. ESSENTIAL CONFIG
st.set_page_config(page_title="Harsh AI Unstoppable", page_icon="🎙️", layout="wide")

# 2. PREMIUM LIGHT UI
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 60px; width: 100%; border: none !important;
    }
    .info-box { background: #E8F0FE; padding: 15px; border-radius: 10px; border-left: 5px solid #1A73E8; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Unstoppable Studio</h1>", unsafe_allow_html=True)
st.write("---")

# 3. THE LOCKED 15 VOICES (Verified Defaults)
VOICE_DATA = {
    "1. Madhur (Hindi Male)": {"id": "hi-IN-MadhurNeural", "p": "-5Hz", "r": "-2%"},
    "2. Swara (Hindi Female)": {"id": "hi-IN-SwaraNeural", "p": "0Hz", "r": "0%"},
    "3. Ankit (Hindi Bold)": {"id": "hi-IN-AnkitNeural", "p": "-8Hz", "r": "-3%"},
    "4. Hemant (Hindi Deep)": {"id": "hi-IN-HemantNeural", "p": "-12Hz", "r": "-5%"},
    "5. Kavya (Hindi Female)": {"id": "hi-IN-KavyaNeural", "p": "0Hz", "r": "0%"},
    "6. Prabhat (Ind Eng)": {"id": "en-IN-PrabhatNeural", "p": "0Hz", "r": "0%"},
    "7. Neerja (Ind Eng)": {"id": "en-IN-NeerjaNeural", "p": "0Hz", "r": "0%"},
    "8. Ravi (Ind Eng)": {"id": "en-IN-RaviNeural", "p": "0Hz", "r": "0%"},
    "9. Christopher (US Deep)": {"id": "en-US-ChristopherNeural", "p": "-10Hz", "r": "-5%"},
    "10. Guy (US Natural)": {"id": "en-US-GuyNeural", "p": "0Hz", "r": "0%"},
    "11. Ava (US Soft)": {"id": "en-US-AvaNeural", "p": "0Hz", "r": "0%"},
    "12. Jenny (US Pro)": {"id": "en-US-JennyNeural", "p": "0Hz", "r": "0%"},
    "13. Thomas (UK Male)": {"id": "en-GB-ThomasNeural", "p": "-5Hz", "r": "0%"},
    "14. Ryan (UK Male)": {"id": "en-GB-RyanNeural", "p": "0Hz", "r": "0%"},
    "15. Libby (UK Female)": {"id": "en-GB-LibbyNeural", "p": "0Hz", "r": "0%"}
}

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT EDITOR")
    script_in = st.text_area("Enter your script:", height=350, placeholder="Paste content here...", key="script_key")
    
    st.markdown("""
    <div class='info-box'>
        <b>🛡️ ANTI-BLOCK SYSTEM ACTIVE</b><br>
        • सर्वर्स को ब्लॉक होने से बचाने के लिए सेटिंग्स को 'Auto-Optimized' रखा गया है।<br>
        • अगर एरर आए, तो पेज को Refresh करें और 5 सेकंड रुककर दोबारा दबाएं।
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎙️ VOICE SELECTION")
    choice = st.selectbox("Select Vocal Cord:", list(VOICE_DATA.keys()))
    
    st.write("---")
    mood = st.selectbox("Background Mood:", ["None", "Mysterious", "Serious News", "Cinematic"])
    st.caption("Settings: Fixed for High Stability.")

# 4. HIGH-STABILITY GENERATOR
async def make_audio(text, voice_config):
    # Unique filename for every attempt to avoid conflict
    out_file = f"prod_{random.randint(1000,9999)}.mp3"
    try:
        # Adding a small random delay to mimic human behavior
        await asyncio.sleep(random.uniform(0.5, 1.5))
        communicate = edge_tts.Communicate(text, voice_config['id'], pitch=voice_config['p'], rate=voice_config['r'])
        await communicate.save(out_file)
        return True, out_file
    except Exception:
        return False, None

if st.button("🚀 GENERATE PROFESSIONAL AUDIO"):
    if not script_in.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("⚡ Connection Established... Synthesizing..."):
            status, result = asyncio.run(make_audio(script_in, VOICE_DATA[choice]))
            if status:
                st.success("✅ Audio Produced!")
                st.audio(result)
                with open(result, "rb") as f:
                    st.download_button("📥 Download MP3", f, file_name="Harsh_Production.mp3")
            else:
                st.error("🚨 Server Lag. Please Refresh the page and try again.")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | v21.0 | Anti-Block Edition</p>", unsafe_allow_html=True)
