import streamlit as st
import asyncio
import edge_tts
import os

# Page Config
st.set_page_config(page_title="Harsh AI Studio", page_icon="🎙️", layout="wide")

# Modern Light Theme Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #202124; }
    .main-header {
        background: linear-gradient(90deg, #4285F4, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stTextArea textarea {
        border: 2px solid #E0E0E0 !important;
        border-radius: 15px !important;
        background-color: #F8F9FA !important;
        color: #202124 !important;
    }
    .stButton>button {
        background-color: #4285F4 !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        width: 100%;
    }
    label { font-size: 1.1rem !important; font-weight: 600 !important; color: #5F6368 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Voice Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Professional & Realistic Vocal Production</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    text_data = st.text_area("अपनी स्क्रिप्ट यहाँ लिखें:", height=400, placeholder="नमस्ते दोस्तों...", key="user_script")
    if st.button("🗑️ Clear All"):
        st.session_state.user_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ वोकल लाइब्रेरी")
    
    # 15 प्रीमियम आवाजें (7 हिंदी और मिक्स)
    v_map = {
        "1. मधुर (Madhur) - शुद्ध हिंदी पुरुष": "hi-IN-MadhurNeural",
        "2. स्वर (Swara) - शुद्ध हिंदी महिला": "hi-IN-SwaraNeural",
        "3. असद (Asad) - गहरा बेस (Deep Voice)": "ur-PK-AsadNeural",
        "4. उज्मा (Uzma) - शांत महिला आवाज़": "ur-PK-UzmaNeural",
        "5. प्रभात (Prabhat) - न्यूज़ एंकर": "en-IN-PrabhatNeural",
        "6. नीरजा (Neerja) - प्रोफेशनल महिला": "en-IN-NeerjaNeural",
        "7. रवि (Ravi) - दोस्ताना लहजा": "en-IN-RaviNeural",
        "8. क्रिस्टोफर (Christopher) - भारी अमेरिकन": "en-US-ChristopherNeural",
        "9. गाय (Guy) - न्यूट्रल अमेरिकन": "en-US-GuyNeural",
        "10. एवा (Ava) - सॉफ्ट अमेरिकन": "en-US-AvaNeural",
        "11. जेनी (Jenny) - मधुर अमेरिकन": "en-US-JennyNeural",
        "12. थॉमस (Thomas) - गंभीर ब्रिटिश": "en-GB-ThomasNeural",
        "13. रयान (Ryan) - यंग ब्रिटिश": "en-GB-RyanNeural",
        "14. लिब्बी (Libby) - साफ़ ब्रिटिश": "en-GB-LibbyNeural",
        "15. मेसी (Maisie) - ब्रिटिश महिला": "en-GB-MaisieNeural"
    }
    
    selected_v = st.selectbox("आवाज़ चुनें:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ ट्यूनिंग पैनल")
    v_pitch = st.slider("आवाज़ का भारीपन (Pitch)", -20, 20, -5)
    v_rate = st.slider("बोलने की रफ़्तार (Speed)", -20, 20, -2)

st.write("---")

if st.button("🚀 GENERATE PROFESSIONAL AUDIO"):
    if not text_data.strip():
        st.warning("कृपया पहले स्क्रिप्ट बॉक्स में कुछ लिखें।")
    else:
        try:
            target_voice = v_map[selected_v]
            async def start_tts():
                p = f"{v_pitch}Hz"
                r = f"{v_rate}%"
                comm = edge_tts.Communicate(text_data, target_voice, pitch=p, rate=r)
                await comm.save("final_output.mp3")

            with st.spinner("AI आवाज़ तैयार कर रहा है..."):
                asyncio.run(start_tts())
            
            st.success("तैयार है!")
            st.audio("final_output.mp3")
            with open("final_output.mp3", "rb") as f:
                st.download_button("📥 डाउनलोड ऑडियो", f, file_name="Harsh_AI_Audio.mp3")
        except Exception as err:
            st.error(f"Error: {err}")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | Pro Edition 2026</p>", unsafe_allow_html=True)
