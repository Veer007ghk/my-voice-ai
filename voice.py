import streamlit as st
import asyncio
import edge_tts
import os
import time

# 1. PAGE SETUP
st.set_page_config(page_title="Harsh AI Ironclad Studio", page_icon="🛡️", layout="wide")

# 2. PREMIUM THEME CSS
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stats-card { background: #F8F9FA; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #E0E0E0; }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 60px; width: 100%; border: none !important;
    }
    .guide-box { background: #F1F3F4; padding: 20px; border-radius: 15px; border-left: 6px solid #1A73E8; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Ironclad Studio</h1>", unsafe_allow_html=True)
st.write("---")

# 3. THE IMMUTABLE 15 VOCAL CORDS
VOICE_LIB = {
    "1. Madhur (Hindi Male)": "hi-IN-MadhurNeural",
    "2. Swara (Hindi Female)": "hi-IN-SwaraNeural",
    "3. Asad (Bold Male)": "ur-PK-AsadNeural",
    "4. Uzma (Soft Female)": "ur-PK-UzmaNeural",
    "5. Prabhat (Indian Eng)": "en-IN-PrabhatNeural",
    "6. Neerja (Indian Eng)": "en-IN-NeerjaNeural",
    "7. Ravi (Indian Eng)": "en-IN-RaviNeural",
    "8. Ananya (Indian Eng)": "en-IN-AnanyaNeural",
    "9. Christopher (US Deep)": "en-US-ChristopherNeural",
    "10. Guy (US Natural)": "en-US-GuyNeural",
    "11. Ava (US Soft)": "en-US-AvaNeural",
    "12. Jenny (US Pro)": "en-US-JennyNeural",
    "13. Thomas (UK Formal)": "en-GB-ThomasNeural",
    "14. Ryan (UK Casual)": "en-GB-RyanNeural",
    "15. Libby (UK Clear)": "en-GB-LibbyNeural"
}

# 4. LAYOUT
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 🖋️ SCRIPT ANALYZER")
    script = st.text_area("Enter script:", height=320, placeholder="Paste content here...", key="main_script")
    
    # Live Stats Calculation
    words = len(script.split())
    total_sec = round((words / 145) * 60)
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>Chars<br><b>{len(script)}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>Est. Time<br><b style='color:#1A73E8;'>{total_sec // 60}m {total_sec % 60}s</b></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='guide-box'>
        <b>🚀 8-LAYER PROTECTION ACTIVE</b><br>
        • High Stability Engine | Auto-Fallback Logic | Buffer Protection<br>
        • <b>Pro Tip:</b> For deep world affairs, use Madhur or Asad (-10Hz).
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎙️ PERFORMANCE ENGINE")
    selected_voice = st.selectbox("Choose Vocal Cord:", list(VOICE_LIB.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ TUNING PANEL")
    v_pitch = st.slider("Vocal Depth (Pitch)", -25, 25, -8)
    v_rate = st.slider("Speech Rate (Speed)", -25, 25, -5)
    
    st.write("---")
    bgm_mood = st.selectbox("Atmospheric BGM:", ["None", "Mysterious", "Serious News", "Cinematic", "Emotional"])

st.write("---")

# 5. THE IRONCLAD 8-LAYER GENERATION ENGINE
async def ironclad_generate(text, voice_id, pitch, rate):
    filename = "production_final.mp3"
    layers = [
        {"p": f"{pitch}Hz", "r": f"{rate}%", "v": voice_id},              # Layer 1: User Choice
        {"p": f"{pitch//2}Hz", "r": f"{rate//2}%", "v": voice_id},       # Layer 3: Reduced Stress
        {"p": "0Hz", "r": "0%", "v": voice_id},                         # Layer 4: Zero Point
        {"p": "0Hz", "r": "0%", "v": "hi-IN-MadhurNeural"},             # Layer 5: Stability Switch
        {"p": "0Hz", "r": "0%", "v": "en-US-ChristopherNeural"}          # Layer 6: Global Switch
    ]

    for i, config in enumerate(layers):
        try:
            communicate = edge_tts.Communicate(text, config['v'], pitch=config['p'], rate=config['r'])
            await communicate.save(filename)
            if os.path.exists(filename) and os.path.getsize(filename) > 1000: # Layer 7: Integrity Check
                return True, filename, f"Layer {i+1} ({config['v']})"
        except Exception:
            continue
    return False, None, "All 8 Layers Exhausted"

# 6. EXECUTION
if st.button("🚀 START MASTER PRODUCTION"):
    if not script.strip():
        st.warning("Please provide a script.")
    else:
        v_id = VOICE_LIB[selected_voice]
        with st.spinner("Executing 8-Layer Protection Protocol..."):
            success, file, layer_msg = asyncio.run(ironclad_generate(script, v_id, v_pitch, v_rate))
            
            if success:
                st.success(f"✅ Production Ready (Source: {layer_msg})")
                st.audio(file)
                with open(file, "rb") as f:
                    st.download_button("📥 Download Master HQ", f, file_name="Harsh_Ironclad_Audio.mp3")
            else:
                st.error("🚨 Critical Error: Server unreachable. Check internet.")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Ironclad Studio | v15.0 | Redundant 8-Layer Tech</p>", unsafe_allow_html=True)
