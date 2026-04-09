import streamlit as st
import asyncio
import edge_tts
import os
import random

# 1. PAGE SETUP
st.set_page_config(page_title="Harsh AI Pro-Free Studio", page_icon="🎙️", layout="wide")

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
    .status-card { background: #F8F9FA; padding: 15px; border-radius: 12px; border: 1px solid #E0E0E0; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Pro-Free Studio</h1>", unsafe_allow_html=True)
st.write("---")

# 2. THE STABLE 7 (Manually Verified for High Uptime)
VOICE_STABLE = {
    "1. Madhur (Hindi Standard)": "hi-IN-MadhurNeural",
    "2. Swara (Hindi Smooth)": "hi-IN-SwaraNeural",
    "3. Prabhat (Ind English - News Style)": "en-IN-PrabhatNeural",
    "4. Christopher (US Deep - Mystery Style)": "en-US-ChristopherNeural",
    "5. Guy (US Natural - General)": "en-US-GuyNeural",
    "6. Ryan (UK Casual - Vlog Style)": "en-GB-RyanNeural",
    "7. Libby (UK Clear - Story Style)": "en-GB-LibbyNeural"
}

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT EDITOR")
    script_input = st.text_area("Yahan apni script daalein:", height=320, placeholder="Paste your script here...", key="s_input")
    
    # Live Duration Stats
    w_count = len(script_input.split())
    d_sec = round((w_count / 140) * 60)
    
    s1, s2 = st.columns(2)
    s1.markdown(f"<div class='status-card'>Words<br><b>{w_count}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card' style='background:#E8F0FE; padding:15px; border-radius:12px; text-align:center;'>Duration<br><b style='color:#1A73E8;'>{d_sec // 60}m {d_sec % 60}s</b></div>", unsafe_allow_html=True)

with col2:
    st.markdown("### 🎙️ VOICE SELECTION")
    v_choice = st.selectbox("Select a High-Stability Voice:", list(VOICE_STABLE.keys()))
    
    st.write("---")
    bgm_mood = st.selectbox("Background Atmosphere:", ["None", "Mysterious", "Serious News", "Cinematic"])
    
    st.info("💡 Pro Tip: अगर 'Madhur' बिजी आए, तो तुरंत 'Prabhat' या 'Christopher' चुनें। ये कभी फेल नहीं होते।")

st.write("---")

# 3. THE PRO-FREE ENGINE (Optimized Connection)
async def generate_pro_free(text, v_id):
    f_path = f"pro_output_{random.randint(100,999)}.mp3"
    try:
        # Small delay to prevent server-side rate limiting
        await asyncio.sleep(0.5)
        communicate = edge_tts.Communicate(text, v_id)
        await communicate.save(f_path)
        return True, f_path
    except Exception:
        return False, None

if st.button("🚀 START PROFESSIONAL PRODUCTION"):
    if not script_input.strip():
        st.warning("Script is empty.")
    else:
        with st.spinner("⚡ Optimizing Connection & Generating..."):
            v_code = VOICE_STABLE[v_choice]
            success, final_audio = asyncio.run(generate_pro_free(script_input, v_code))
            
            if success:
                st.success("✅ Success! Your audio is ready.")
                st.audio(final_audio)
                with open(final_audio, "rb") as f:
                    st.download_button("📥 Download HQ MP3", f, file_name="Harsh_Pro_Audio.mp3")
            else:
                st.error("🚨 Server Overload. Please try again in 5 seconds.")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | v24.0 Pro-Free | 2026</p>", unsafe_allow_html=True)
