from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_transcript(video_id: str) -> str:
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_data = ytt_api.fetch(video_id, languages=["en"])
        return " ".join(chunk.text for chunk in transcript_data)

    except TranscriptsDisabled:
        return "No captions available for this video."

