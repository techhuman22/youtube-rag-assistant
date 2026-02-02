import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import sys

with open("debug_output.txt", "w") as f:
    f.write(f"Python executable: {sys.executable}\n")
    f.write(f"Module file: {youtube_transcript_api.__file__}\n")
    f.write(f"Class/Object: {YouTubeTranscriptApi}\n")
    f.write(f"Dir: {dir(YouTubeTranscriptApi)}\n")

with open("debug_output_2.txt", "w") as f:
    try:
        f.write("Attempting to instantiate and fetch...\n")
        api = YouTubeTranscriptApi()
        # We can't easily fetch a real video without internet or a valid ID, but we can check if the method exists.
        f.write(f"Instance created: {api}\n")
        f.write(f"Has fetch method: {hasattr(api, 'fetch')}\n")
        f.write(f"Has list method: {hasattr(api, 'list')}\n")
    except Exception as e:
        f.write(f"Error testing instance: {e}\n")
