from youtube_transcript_api import YouTubeTranscriptApi
from utils.helpers import extract_video_id
import streamlit as st
from typing import Tuple

def fetch_video_data(video_url: str) -> Tuple[str, str]:
    try:
        video_id = extract_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry["text"] for entry in transcript])
        return "Unknown", transcript_text
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return "Unknown", "No transcript available for this video."
