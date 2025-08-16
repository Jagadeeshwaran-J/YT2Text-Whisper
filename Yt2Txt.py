import os
import yt_dlp
import whisper


# Function to download YouTube audio directly as MP3 using yt_dlp
def download_audio(youtube_url, output_path="audio.mp3"):
    """
    Downloads the audio from a YouTube video as MP3 using yt_dlp.
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'temp_audio.%(ext)s',  # temp filename
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        # After conversion, yt_dlp should create temp_audio.mp3
        if os.path.exists("temp_audio.mp3"):
            os.rename("temp_audio.mp3", output_path)
            print(f"Audio saved as {output_path}")
            return output_path
        else:
            raise Exception("Audio file not created")
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")
        return None


# Function to transcribe audio using Whisper
def transcribe_audio(audio_path):
    """
    Transcribes an audio file using the Whisper 'base' model.
    """
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found at {audio_path}")
        return ""

    # Create the 'model' directory if it doesn't exist
    model_dir = os.path.join(os.getcwd(), 'model')
    os.makedirs(model_dir, exist_ok=True)

    print("Loading Whisper model...")
    # The 'download_root' parameter saves the model files to the specified directory.
    model = whisper.load_model("base", download_root=model_dir)

    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    return result["text"]


# Main function
def youtube_to_text(youtube_url):
    """
    Main function: downloads audio, transcribes it, and cleans up.
    """
    audio_path = download_audio(youtube_url)
    if audio_path:
        transcript = transcribe_audio(audio_path)
        os.remove(audio_path)  # Clean up audio file
        return transcript
    return "Transcription failed."


# Example Usage
if __name__ == "__main__":
    youtube_url = "https://youtu.be/FAyKDaXEAgc?si=2V6ReT2523kMW7h0"
    text_output = youtube_to_text(youtube_url)
    print("\n--- Transcription ---")
    print(text_output)