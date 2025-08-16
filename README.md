# 🎙️ YouTube Audio Transcriber with Whisper  

This project allows you to:  
1. Download audio from a YouTube video using **yt-dlp**.  
2. Transcribe the audio into text using **OpenAI Whisper**.  
3. Save and clean up downloaded files automatically.  

It’s a simple end-to-end pipeline for YouTube → Audio → Text.  

---

## 🚀 Features
- Downloads only the **audio** (not full video) in MP3 format.  
- Uses **Whisper (base model)** for speech-to-text transcription.  
- Stores the Whisper model locally in a `model/` folder.  
- Cleans up audio files automatically after transcription.  

---

## 🛠️ Step 1: Install Requirements  

Make sure you have **Python 3.8+** installed. Then install the required libraries:  

```bash
pip install -r requirements.txt
```

Additional dependencies:  
- **FFmpeg** (required for audio conversion).  

### Install FFmpeg:  
- On **Linux / Mac**:  
  ```bash
  sudo apt-get install ffmpeg
  ```  
- On **Windows**:  
  1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).  
  2. Extract it.  
  3. Add the `bin/` folder to your system PATH.  

---

## 📂 Step 2: Project Structure  

```
youtube-transcriber/
│── Yt2Txt.py     # Main Python script
│── model/             # Whisper model files will be saved here
│── README.md          # Project documentation
│── requirements.txt   # packages
```

---

## 📝 Step 3: How the Code Works  

1. **Download Audio**  
   - The script uses `yt-dlp` to fetch audio from the YouTube link.  
   - It extracts and saves the audio as an MP3 file.  

2. **Save Whisper Model**  
   - Whisper’s `"base"` model is downloaded automatically and saved inside the `model/` folder.  

3. **Transcription**  
   - The audio file is passed to Whisper.  
   - The model converts speech → text.  

4. **Clean Up**  
   - Once transcription is done, the MP3 file is deleted to save space.  

5. **Output**  
   - The transcription is printed on the screen.  

---

## ▶️ Step 4: Run the Project  

Run the script with:  

```bash
python transcriber.py
```

Default YouTube link is already included in the script:  
```python
youtube_url = "https://youtu.be/FAyKDaXEAgc?si=2V6ReT2523kMW7h0"
```

You can replace this with **any YouTube link**.  

---

## 📌 Example Output  

```
Audio saved as audio.mp3
Loading Whisper model...
Transcribing audio...

--- Transcription ---
Hello everyone, welcome to this video...
```

---

✅ That’s it! You now have a working **YouTube → Audio → Text Transcriber** using Whisper.  
