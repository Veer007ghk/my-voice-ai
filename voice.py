import streamlit as st
import asyncio
import edge_tts

# वेबसाइट का लुक और फील
st.set_page_config(page_title="Harsh Pro AI Voice Studio", page_icon="🎙️", layout="wide")

st.title("🎙️ Ultimate Multi-Accent AI Studio")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    text = st.text_area("अपनी स्क्रिप्ट यहाँ पेस्ट करें (हिंदी या इंग्लिश):", height=350, placeholder="अपनी स्क्रिप्ट यहाँ लिखें...")

with col2:
    st.subheader("आवाज़ और एक्सेंट")
    
    # कैटेगरी के हिसाब से आवाजों का बँटवारा
    voice_options = {
        "--- शुद्ध भारतीय हिंदी (Pure Hindi) ---": "hi-IN-MadhurNeural",
        "पुरुष (Madhur - Indian Hindi)": "hi-IN-MadhurNeural",
        "महिला (Swara - Indian Hindi)": "hi-IN-SwaraNeural",
        
        "--- अमेरिकन एक्सेंट (Pure US English) ---": "en-US-GuyNeural",
        "पुरुष (Guy - American US)": "en-US-GuyNeural",
        "पुरुष (Christopher - American US)": "en-US-ChristopherNeural",
        "महिला (Ava - American US)": "en-US-AvaNeural",
        "महिला (Jenny - American US)": "en-US-JennyNeural",
        
        "--- ब्रिटिश एक्सेंट (Pure UK English) ---": "en-GB-ThomasNeural",
        "पुरुष (Thomas - British UK)": "en-GB-ThomasNeural",
        "पुरुष (Ryan - British UK)": "en-GB-RyanNeural",
        "महिला (Libby - British UK)": "en-GB-LibbyNeural",
        "महिला (Sonia - British UK)": "en-GB-SoniaNeural",

        "--- भारतीय इंग्लिश (Indian English) ---": "en-IN-PrabhatNeural",
        "पुरुष (Prabhat - Indian Accent)": "en-IN-PrabhatNeural",
        "महिला (Neerja - Indian Accent)": "en-IN-NeerjaNeural"
    }
    
    selected_label = st.selectbox("वोकल कॉर्ड और एक्सेंट चुनें:", list(voice_options.keys()))
    selected_voice = voice_options[selected_label]
    
    st.markdown("### ट्यूनिंग")
    pitch = st.slider("आवाज़ का भारीपन (Pitch)", -20, 20, -5)
    rate = st.slider("बोलने की रफ़्तार (Speed)", -20, 20, -2)

st.markdown("---")

# अगर यूजर ने हेडर (---) चुन लिया है तो उसे रोकने के लिए
if st.button("🚀 Generate Realistic Audio"):
    if "---" in selected_label:
        st.error("कृपया कैटेगरी के अंदर से एक आवाज़ चुनें, हेडर नहीं!")
    elif text:
        async def generate():
            p_str = f"{pitch}Hz"
            r_str = f"{rate}%"
            communicate = edge_tts.Communicate(text, selected_voice, pitch=p_str, rate=r_str)
            await communicate.save("output.mp3")

        with st.spinner('AI आवाज़ तैयार कर रहा है...'):
            asyncio.run(generate())

        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        
        st.download_button(
            label="⬇️ ऑडियो डाउनलोड करें",
            data=audio_bytes,
            file_name="harsh_ai_voice.mp3",
            mime="audio/mp3"
        )
    else:
        st.error("कृपया पहले स्क्रिप्ट लिखें!")

st.success("टिप: अमेरिकन एक्सेंट के लिए 'Guy' या 'Christopher' चुनें, यह वर्ल्ड अफेयर्स के लिए वर्ल्ड-क्लास लगेगा।")
