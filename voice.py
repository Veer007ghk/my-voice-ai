import streamlit as st
import asyncio
import edge_tts
import os

# VIP पेज कॉन्फ़िगरेशन
st.set_page_config(
    page_title="Harsh AI VIP Voice Studio", 
    page_icon="🎙️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# अल्ट्रा-प्रोफेशनल डार्क VIP थीम (CSS)
st.markdown("""
    <style>
    /* मुख्य बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    /* ग्लास बॉक्स इफ़ेक्ट */
    .css-1y4p8pa {
        padding: 2rem;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    /* टेक्स्ट एरिया कस्टमाइजेशन */
    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3) !important;
        color: #e0e0e0 !important;
        border: 1px solid #4a4e69 !important;
        border-radius: 15px !important;
        font-size: 16px;
    }
    /* बटन स्टाइलिंग - VIP लुक */
    .stButton>button {
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        font-size: 18px;
        margin: 4px 2px;
        transition: 0.4s;
        border-radius: 12px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 198, 255, 0.4);
        color: white;
    }
    /* साइडबार और सेलेक्ट बॉक्स */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px !important;
    }
    /* टाइटल एनीमेशन */
    .title-container {
        text-align: center;
        padding: 20px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        margin-bottom: 25px;
    }
    h1 {
        text-shadow: 2px 2px 4px #000000;
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# हैडर सेक्शन
st.markdown("""
    <div class="title-container">
        <h1 style='color: #00d2ff; margin-bottom: 0;'>💎 Harsh AI VIP Voice Studio</h1>
        <p style='color: #bdc3c7; font-size: 1.1em;'>Professional Voice Production for World Affairs & Beyond</p>
    </div>
    """, unsafe_allow_html=True)

# मुख्य लेआउट
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("### 🖋️ अपनी स्क्रिप्ट यहाँ लिखें")
    # स्क्रिप्ट इनपुट
    text_input = st.text_area("", height=400, placeholder="यहाँ अपनी स्क्रिप्ट पेस्ट करें...", key="script_box")
    
    if st.button("🗑️ Clear Text"):
        st.session_state.script_box = ""
        st.rerun()

with col2:
    st.markdown("### 🎭 वॉइस और एक्सेंट")
    
    # VIP वॉइस कलेक्शन (बिना एरर वाला मैप)
    voice_map = {
        "--- 🇮🇳 शुद्ध भारतीय हिंदी ---": "hi-IN-MadhurNeural",
        "दमदार पुरुष (Madhur)": "hi-IN-MadhurNeural",
        "साफ़ महिला (Swara)": "hi-IN-SwaraNeural",
        
        "--- 🇺🇸 अमेरिकन एक्सेंट ---": "en-US-GuyNeural",
        "पुरुष (Guy - American)": "en-US-GuyNeural",
        "पुरुष (Christopher - American)": "en-US-ChristopherNeural",
        "महिला (Ava - American)": "en-US-AvaNeural",
        "महिला (Jenny - American)": "en-US-JennyNeural",
        
        "--- 🇬🇧 ब्रिटिश एक्सेंट ---": "en-GB-ThomasNeural",
        "पुरुष (Thomas - British)": "en-GB-ThomasNeural",
        "महिला (Libby - British)": "en-GB-LibbyNeural",

        "--- 🇮🇳 भारतीय इंग्लिश ---": "en-IN-PrabhatNeural",
        "पुरुष (Prabhat - Indian)": "en-IN-PrabhatNeural",
        "महिला (Ananya - Indian)": "en-IN-AnanyaNeural"
    }
    
    selected_label = st.selectbox("वोकल कॉर्ड चुनें:", list(voice_map.keys()))
    
    st.markdown("---")
    st.markdown("### 🎚️ VIP ट्यूनिंग पैनल")
    pitch = st.slider("आवाज़ का भारीपन (Pitch)", -20, 20, -5, help="नेगेटिव वैल्यू आवाज़ को भारी बनाती है")
    rate = st.slider("बोलने की रफ़्तार (Speed)", -20, 20, -2, help="नेगेटिव वैल्यू रफ़्तार कम करती है")

st.markdown("---")

# जेनरेशन लॉजिक (Error Proof)
if st.button("🎙️ GENERATE AUDIO (VIP MODE)"):
    if "---" in selected_label:
        st.error("⚠️ कृपया सूची से एक वास्तविक आवाज़ चुनें (कैटेगरी हेडर नहीं)!")
    elif not text_input.strip():
        st.warning("❗ महोदय, स्क्रिप्ट बॉक्स खाली है। कृपया कुछ लिखें।")
    else:
        try:
            target_voice = voice_map[selected_label]
            
            async def generate_audio():
                p_str = f"{pitch}Hz"
                r_str = f"{rate}%"
                communicate = edge_tts.Communicate(text_input, target_voice, pitch=p_str, rate=r_str)
                await communicate.save("vip_output.mp3")

            with st.status("💎 AI स्टूडियो आवाज़ प्रोसेस कर रहा है...", expanded=True) as status:
                asyncio.run(generate_audio())
                status.update(label="✅ ऑडियो सफलतापूर्वक तैयार!", state="complete", expanded=False)

            # ऑडियो प्लेयर
            st.audio("vip_output.mp3", format='audio/mp3')
            
            # डाउनलोड बटन
            with open("vip_output.mp3", "rb") as file:
                st.download_button(
                    label="📥 VIP ऑडियो डाउनलोड करें",
                    data=file,
                    file_name="Harsh_VIP_Voice.mp3",
                    mime="audio/mp3"
                )
        except Exception as e:
            st.error(f"❌ तकनीकी समस्या: {e}")

st.markdown("<p style='text-align: center; color: #57606f; margin-top: 50px;'>© 2026 Harsh BAMS | Ultimate Content Creator Tools</p>", unsafe_allow_html=True)
