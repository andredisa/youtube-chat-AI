import streamlit as st
from config.settings import get_config
from services.youtube_service import fetch_video_data
from services.embedchain_service import create_embedchain_app
import tempfile

st.title("Chat with YouTube Video 📺")
st.caption("This app allows you to chat with a YouTube video using OpenAI API")

openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    db_path = tempfile.mkdtemp()
    app = create_embedchain_app(db_path, openai_access_token)
    video_url = st.text_input("Enter YouTube Video URL")

    if video_url:
        title, transcript = fetch_video_data(video_url)
        if transcript != "No transcript available for this video.":
            app.add(transcript, data_type="text", metadata={"title": title, "url": video_url})
            st.success(f"Added video '{title}' to knowledge base!")
        else:
            st.warning("No transcript available.")

        prompt = st.text_input("Ask any question about the YouTube Video")
        if prompt:
            try:
                st.write(app.chat(prompt))
            except Exception as e:
                st.error(f"Chat error: {e}")
