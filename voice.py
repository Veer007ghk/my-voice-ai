import streamlit as st
import asyncio
import edge_tts
import base64

st.set_page_config(page_title="Harsh AI Voice Studio Pro", page_icon="🎙️")
st.title("🎙️ World Affairs AI Voice Studio")

text = st.text_area("अपनी स्क्रिप्ट यहाँ पेस्ट करें:", placeholder="नमस्ते दोस्तों...", height=200)

voice_option = st.selectbox(
    "आवाज़ चुनें:",
    ("hi-IN-MadhurNeural (भारी पुरुष आवाज़)", "hi-IN-SwaraNeural (साफ महिला आवाज़)")
)

# यहाँ हम पिच और रफ़्तार को कंट्रोल करेंगे
if st.button("Generate Realistic Voice"):
    if text:
        async def generate():
            v_name = voice_option.split(" ")[0]
            
            # पिच -10Hz मतलब आवाज़ थोड़ी भारी (Deep) होगी
            # रेट -5% मतलब बोलने की रफ़्तार थोड़ी कम होगी ताकि न्यूज़ साफ़ सुनाई दे
            communicate = edge_tts.Communicate(text, v_name, pitch="-10Hz", rate="-5%")
            await communicate.save("output.mp3")

        asyncio.run(generate())

        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.download_button(label="ऑडियो डाउनलोड करें", data=audio_bytes, file_name="news_pro.mp3", mime="audio/mp3")
    else:
        st.warning("कृपया पहले कुछ टेक्स्ट लिखें!")
