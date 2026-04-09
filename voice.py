import streamlit as st
import asyncio
import edge_tts
import os

# Ultra Stable Page Configuration
st.set_page_config(page_title="Harsh AI Production Studio", page_icon="🎙️", layout="wide")

# VIP Light Theme Design
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #202124; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem; font-weight: 800; text-align: center; margin-bottom: 5px;
    }
    .stats-card {
        background: #F8F9FA; padding: 15px; border-radius: 12px;
        text-align: center; border: 1px solid #E0E0E0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 10px !important; font-weight: bold !important;
        height: 50px; width: 100%; transition: 0.3s;
    }
    label { font-size: 1rem !important; font-weight: 600 !important; color: #3C4043 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Production Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5F6368;'>Ultimate Voice Engine | 100% Fixed Pitch & Rate</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.6, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT EDITOR")
    # स्क्रिप्ट इनपुट बॉक्स
    script = st.text_area("Enter your script here:", height=380, placeholder="Paste your story or news script here...", key="main_script")
    
    # लाइव कैलकुलेशन
    words = len(script.split())
    chars = len(script)
    total_sec = round((words / 150) * 60) # 150 wpm average
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>Chars<br><b>{chars}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>Duration<br><b style='color:#1A73E8;'>{total_sec // 60}m {total_sec % 60}s</b></div>", unsafe_allow_html=True)

    if st.button("🗑️ Reset Editor"):
        st.session_state.main_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ VOCAL LIBRARY")
    # पूरी 15 आवाजों की फिक्स्ड लिस्ट
    v_map = {
        "1. Madhur (Hindi Male)": "hi-IN-MadhurNeural",
        "2. Swara (Hindi Female)": "hi-IN-SwaraNeural",
        "3. Asad (Urdu/Hindi Bold Male)": "ur-PK-AsadNeural",
        "4. Uzma (Urdu/Hindi Soft Female)": "ur-PK-UzmaNeural",
        "5. Prabhat (Indian English Male)": "en-IN-PrabhatNeural",
        "6. Neerja (Indian English Female)": "en-IN-NeerjaNeural",
        "7. Ravi (Indian English Male)": "en-IN-RaviNeural",
        "8. Ananya (Indian English Female)": "en-IN-AnanyaNeural",
        "9. Christopher (US Deep Male)": "en-US-ChristopherNeural",
        "10. Guy (US Natural Male)": "en-US-GuyNeural",
        "11. Ava (US Soft Female)": "en-US-AvaNeural",
        "12. Jenny (US Professional Female)": "en-US-JennyNeural",
        "13. Thomas (UK Formal Male)": "en-GB-ThomasNeural",
        "14. Ryan (UK Casual Male)": "en-GB-RyanNeural",
        "15. Libby (UK Clear Female)": "en-GB-LibbyNeural"
    }
    
    selected_voice = st.selectbox("Choose Vocal Model:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ TUNING PANEL")
    # फिक्स्ड पिच और रेट स्लाइडर्स
    v_pitch = st.slider("Vocal Depth (Pitch)", -25, 25, -10, help="Negative makes voice deeper/heavier")
    v_rate = st.slider("Speech Rate (Speed)", -25, 25, -5, help="Negative makes it slower")
    
    st.write("---")
    st.info("💡 Hint: Use 'Asad' with -15 Pitch for an extremely heavy World Affairs voice.")

st.write("---")

# जेनरेशन बटन
if st.button("🚀 GENERATE MASTER PRODUCTION"):
    if not script.strip():
        st.warning("Please enter your script first!")
    else:
        try:
            voice_id = v_map[selected_voice]
            
            async def run_production():
                # पिच और रेट को सही फॉर्मेट में फ़ोर्स करना
                p_param = f"{v_pitch:+}Hz"
                r_param = f"{v_rate:+}%"
                
                communicate = edge_tts.Communicate(script, voice_id, pitch=p_param, rate=r_param)
                await communicate.save("final_voice.mp3")

            with st.spinner("AI Studio is synthesizing your professional audio..."):
                asyncio.run(run_production())
            
            st.success("✅ Success! Your production-ready audio is generated.")
            st.audio("final_voice.mp3")
            
            with open("final_voice.mp3", "rb") as f:
                st.download_button("📥 Download Master MP3", f, file_name="Harsh_AI_Production.mp3")
                
        except Exception as e:
            st.error(f"Technical Error: {e}")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Production Studio | v9.0 Final | 2026</p>", unsafe_allow_html=True)
