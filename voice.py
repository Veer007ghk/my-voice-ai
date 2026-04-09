import streamlit as st
import asyncio
import edge_tts
import base64

# वेबसाइट का टाइटल और लेआउट
st.set_page_config(page_title="Harsh AI Voice Generator", page_icon="🎙️")
st.title("🎙️ My Personal AI Voice Studio")
st.write("World Affairs के लिए प्रीमियम और रियलिस्टिक आवाज़ यहाँ जनरेट करें।")

# टेक्स्ट इनपुट बॉक्स
text = st.text_area("अपनी स्क्रिप्ट यहाँ पेस्ट करें:", placeholder="नमस्ते दोस्तों, आज हम बात करेंगे...", height=200)

# आवाज़ चुनने का ऑप्शन
voice_option = st.selectbox(
    "आवाज़ चुनें:",
    ("hi-IN-MadhurNeural (दमदार पुरुष)", "hi-IN-SwaraNeural (साफ महिला आवाज़)", "en-IN-PrabhatNeural (Indian English Male)")
)

# जनरेट बटन
if st.button("Generate Realistic Voice"):
    if text:
        async def generate():
            # आवाज़ का नाम सेट करना
            v_name = voice_option.split(" ")[0]
            communicate = edge_tts.Communicate(text, v_name)
            await communicate.save("output.mp3")

        # रन करना
        asyncio.run(generate())

        # ऑडियो प्लेयर दिखाना
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        
        # डाउनलोड बटन
        st.download_button(label="Audio Download Karein", data=audio_bytes, file_name="news_audio.mp3", mime="audio/mp3")
    else:
        st.warning("कृपया पहले कुछ टेक्स्ट लिखें!")