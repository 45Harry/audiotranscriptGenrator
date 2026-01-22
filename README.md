# Audio Analysis & Transcription Project

This project provides tools for processing audio files and generating Nepali transcriptions, primarily for Text-to-Speech (TTS) dataset creation.

## Files

- **`transscript.py`**: Transcribes `.wav` files located in `tts_dataset/wavs` using OpenAI's Whisper model (configured for Nepali). Outputs to CSV and TXT.
- **`baking.py`**: A more comprehensive utility that splits long audio files (mp3, etc.) into shorter segments (7-10s) and generates transcripts.
- **`audiofiles/`**: Directory for source audio files.
- **`tts_dataset/wavs/`**: Directory containing split `.wav` files ready for transcription.

## Setup

1.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Install FFmpeg** (Required for `pydub` / audio processing):
    - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html), extract, and add the `bin` folder to your System PATH.
    - **Linux**: `sudo apt install ffmpeg`
    - **Mac**: `brew install ffmpeg`

## Usage

### helper: Transcription only
If you already have `.wav` files in `tts_dataset/wavs`:
```bash
python transscript.py
```
This will generate:
- `transcripts.csv`: Metadata format.
- `nepali_transcripts.txt`: Text format.

### baking.py: Split & Process
To split new audio files and process them:
1. Place audio in `audiofiles/`.
2. Run:
   ```bash
   python baking.py
   ```

This Python script downloads audio from a YouTube video and converts it into a WAV file using the yt-dlp library.
It first cleans the YouTube URL by removing tracking or extra query parameters to avoid download issues.
The script selects the best available audio format from the video source.
Using FFmpeg post-processing, it extracts the audio and converts it into a high-quality WAV file.
The output file is saved with a fixed, simplified filename to avoid problems with long or special characters.
Playlist downloads are disabled to ensure only a single video is processed.
Download progress and logs are shown in the terminal for transparency.
The script includes basic error handling to catch and display download or conversion errors.
It is suitable for preparing audio data for tasks like speech-to-text, audio analysis, or machine learning.
The YouTube link is hardcoded for reliability when terminal input fails.
This approach is efficient for extracting clean audio from online video sources.
