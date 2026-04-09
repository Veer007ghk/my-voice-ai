import streamlit as st
import asyncio
import edge_tts
import os

# Ultra-Stable Page Setup
st.set_page_config(page_title="Harsh AI Studio Pro", page_icon="🎙️", layout="wide")

# VIP Modern Interface Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .guide-box {
        background-color: #F8F9FA; padding: 20px; border-radius: 15px;
        border-left: 6px solid #1A73E8; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .stats-card {
        background: #FFFFFF; padding: 15px; border-radius: 12px;
        text-align: center; border: 1px solid #E0E0E0;
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 55px; width: 100%; transition: 0.3s;
    }
    label { font-size: 1.1rem !important; font-weight: 600 !important; color: #3C4043 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Studio Pro</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT ANALYZER")
    script = st.text_area("Paste your story or script here:", height=350, placeholder="Write your content...", key="main_script")
    
    # Accurate Stats Calculation
    words = len(script.split())
    chars = len(script)
    # 140-150 words per minute is ideal for storytelling
    total_sec = round((words / 145) * 60)
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>Chars<br><b>{chars}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>Duration<br><b style='color:#1A73E8;'>{total_sec // 60}m {total_sec % 60}s</b></div>", unsafe_allow_html=True)

    # 💡 EXPERT TUNING GUIDE PANEL
    st.markdown("""
    <div class='guide-box'>
        <h4 style='margin-top:0;'>🚀 PRO CREATOR GUIDE</h4>
        <b>1. Vocal Depth (Pitch):</b><br>
        • <b>Heavy Base (-8 to -12):</b> Best for Suspense, World Affairs, and Horror Stories.<br>
        • <b>Natural Style (-2 to -5):</b> Best for Educational and News content.<br><br>
        <b>2. Speech Rate (Speed):</b><br>
        • <b>Slow Pace (-5 to -10):</b> Use for Emotional or Thriller stories (increases impact).<br>
        • <b>Normal Pace (-2 to 0):</b> Use for general Information and Vlogs.<br><br>
        <i><b>Note:</b> For 'Asad' voice, keep Depth at -8 for the most realistic heavy sound.</i>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎙️ VOCAL LIBRARY (STRICT 15)")
    # यह लिस्ट अब लॉक है, इसमें 15 की 15 आवाज़ें रहेंगी
    v_map = {
        "1. Madhur (Hindi Male)": "hi-IN-MadhurNeural",
        "2. Swara (Hindi Female)": "hi-IN-SwaraNeural",
        "3. Asad (Bold Male - Deep)": "ur-PK-AsadNeural",
        "4. Uzma (Soft Female - Calm)": "ur-PK-UzmaNeural",
        "5. Prabhat (Indian Eng News)": "en-IN-PrabhatNeural",
        "6. Neerja (Indian Eng Soft)": "en-IN-NeerjaNeural",
        "7. Ravi (Indian Eng Friendly)": "en-IN-RaviNeural",
        "8. Ananya (Indian Eng Modern)": "en-IN-AnanyaNeural",
        "9. Christopher (US Deep Male)": "en-US-ChristopherNeural",
        "10. Guy (US Natural Male)": "en-US-GuyNeural",
        "11. Ava (US Soft Female)": "en-US-AvaNeural",
        "12. Jenny (US Professional)": "en-US-JennyNeural",
        "13. Thomas (UK Formal Male)": "en-GB-ThomasNeural",
        "14. Ryan (UK Casual Male)": "en-GB-RyanNeural",
        "15. Libby (UK Clear Female)": "en-GB-LibbyNeural"
    }
    
    selected_voice = st.selectbox("Select Your Vocal Cord:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ PERFORMANCE TUNING")
    # Pitch & Rate Sliders with Clear Formatting
    v_pitch = st.slider("Vocal Depth (Heavy/Sharp)", -20, 20, -8, help="Decrease for deeper voice")
    v_rate = st.slider("Speech Rate (Speed Control)", -20, 20, -5, help="Decrease for slower speech")
    
    st.write("---")
    st.markdown("### 🎵 ATMOSPHERIC MOOD")
    bgm_mood = st.selectbox("Choose Background Vibe:", ["None", "Mysterious", "Serious News", "Cinematic", "Emotional"])
    st.info("💡 Tip: Use 'Mysterious' BGM with -10 Vocal Depth for your fictional stories.")

st.write("---")

# FINAL PRODUCTION ENGINE
if st.button("🚀 GENERATE PROFESSIONAL PRODUCTION"):
    if not script.strip():
        st.warning("Please enter your script first!")
    else:
        try:
            voice_id = v_map[selected_voice]
            
            async def run_gen():
                # Correct Parameter Strings for edge-tts
                p_str = f"{v_pitch:+}Hz"
                r_str = f"{v_rate:+}%"
                
                communicate = edge_tts.Communicate(script, voice_id, pitch=p_str, rate=r_str)
                await communicate.save("harsh_final_hq.mp3")

            with st.spinner("Harsh AI is crafting your masterpiece..."):
                asyncio.run(run_gen())
            
            if os.path.exists("harsh_final_hq.mp3"):
                st.success("✅ Your Audio Production is Ready!")
                st.audio("harsh_final_hq.mp3")
                with open("harsh_final_hq.mp3", "rb") as f:
                    st.download_button("📥 Download HQ Audio (MP3)", f, file_name="Harsh_Master_Audio.mp3")
            else:
                st.error("Generation failed. Please try slightly different Pitch/Rate settings.")
                
        except Exception as e:
            st.error(f"Technical Alert: {e}. Please ensure Pitch is within -10 to +10 for best stability.")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | v12.0 Master Production | 2026</p>", unsafe_allow_html=True)import streamlit as st
import asyncio
import edge_tts
import os

# Ultra-Stable Page Setup
st.set_page_config(page_title="Harsh AI Studio Pro", page_icon="🎙️", layout="wide")

# VIP Modern Interface Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .guide-box {
        background-color: #F8F9FA; padding: 20px; border-radius: 15px;
        border-left: 6px solid #1A73E8; margin-top: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .stats-card {
        background: #FFFFFF; padding: 15px; border-radius: 12px;
        text-align: center; border: 1px solid #E0E0E0;
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 55px; width: 100%; transition: 0.3s;
    }
    label { font-size: 1.1rem !important; font-weight: 600 !important; color: #3C4043 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Studio Pro</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT ANALYZER")
    script = st.text_area("Paste your story or script here:", height=350, placeholder="Write your content...", key="main_script")
    
    # Accurate Stats Calculation
    words = len(script.split())
    chars = len(script)
    # 140-150 words per minute is ideal for storytelling
    total_sec = round((words / 145) * 60)
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>Chars<br><b>{chars}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>Duration<br><b style='color:#1A73E8;'>{total_sec // 60}m {total_sec % 60}s</b></div>", unsafe_allow_html=True)

    # 💡 EXPERT TUNING GUIDE PANEL
    st.markdown("""
    <div class='guide-box'>
        <h4 style='margin-top:0;'>🚀 PRO CREATOR GUIDE</h4>
        <b>1. Vocal Depth (Pitch):</b><br>
        • <b>Heavy Base (-8 to -12):</b> Best for Suspense, World Affairs, and Horror Stories.<br>
        • <b>Natural Style (-2 to -5):</b> Best for Educational and News content.<br><br>
        <b>2. Speech Rate (Speed):</b><br>
        • <b>Slow Pace (-5 to -10):</b> Use for Emotional or Thriller stories (increases impact).<br>
        • <b>Normal Pace (-2 to 0):</b> Use for general Information and Vlogs.<br><br>
        <i><b>Note:</b> For 'Asad' voice, keep Depth at -8 for the most realistic heavy sound.</i>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎙️ VOCAL LIBRARY (STRICT 15)")
    # यह लिस्ट अब लॉक है, इसमें 15 की 15 आवाज़ें रहेंगी
    v_map = {
        "1. Madhur (Hindi Male)": "hi-IN-MadhurNeural",
        "2. Swara (Hindi Female)": "hi-IN-SwaraNeural",
        "3. Asad (Bold Male - Deep)": "ur-PK-AsadNeural",
        "4. Uzma (Soft Female - Calm)": "ur-PK-UzmaNeural",
        "5. Prabhat (Indian Eng News)": "en-IN-PrabhatNeural",
        "6. Neerja (Indian Eng Soft)": "en-IN-NeerjaNeural",
        "7. Ravi (Indian Eng Friendly)": "en-IN-RaviNeural",
        "8. Ananya (Indian Eng Modern)": "en-IN-AnanyaNeural",
        "9. Christopher (US Deep Male)": "en-US-ChristopherNeural",
        "10. Guy (US Natural Male)": "en-US-GuyNeural",
        "11. Ava (US Soft Female)": "en-US-AvaNeural",
        "12. Jenny (US Professional)": "en-US-JennyNeural",
        "13. Thomas (UK Formal Male)": "en-GB-ThomasNeural",
        "14. Ryan (UK Casual Male)": "en-GB-RyanNeural",
        "15. Libby (UK Clear Female)": "en-GB-LibbyNeural"
    }
    
    selected_voice = st.selectbox("Select Your Vocal Cord:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ PERFORMANCE TUNING")
    # Pitch & Rate Sliders with Clear Formatting
    v_pitch = st.slider("Vocal Depth (Heavy/Sharp)", -20, 20, -8, help="Decrease for deeper voice")
    v_rate = st.slider("Speech Rate (Speed Control)", -20, 20, -5, help="Decrease for slower speech")
    
    st.write("---")
    st.markdown("### 🎵 ATMOSPHERIC MOOD")
    bgm_mood = st.selectbox("Choose Background Vibe:", ["None", "Mysterious", "Serious News", "Cinematic", "Emotional"])
    st.info("💡 Tip: Use 'Mysterious' BGM with -10 Vocal Depth for your fictional stories.")

st.write("---")

# FINAL PRODUCTION ENGINE
if st.button("🚀 GENERATE PROFESSIONAL PRODUCTION"):
    if not script.strip():
        st.warning("Please enter your script first!")
    else:
        try:
            voice_id = v_map[selected_voice]
            
            async def run_gen():
                # Correct Parameter Strings for edge-tts
                p_str = f"{v_pitch:+}Hz"
                r_str = f"{v_rate:+}%"
                
                communicate = edge_tts.Communicate(script, voice_id, pitch=p_str, rate=r_str)
                await communicate.save("harsh_final_hq.mp3")

            with st.spinner("Harsh AI is crafting your masterpiece..."):
                asyncio.run(run_gen())
            
            if os.path.exists("harsh_final_hq.mp3"):
                st.success("✅ Your Audio Production is Ready!")
                st.audio("harsh_final_hq.mp3")
                with open("harsh_final_hq.mp3", "rb") as f:
                    st.download_button("📥 Download HQ Audio (MP3)", f, file_name="Harsh_Master_Audio.mp3")
            else:
                st.error("Generation failed. Please try slightly different Pitch/Rate settings.")
                
        except Exception as e:
            st.error(f"Technical Alert: {e}. Please ensure Pitch is within -10 to +10 for best stability.")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | v12.0 Master Production | 2026</p>", unsafe_allow_html=True)
