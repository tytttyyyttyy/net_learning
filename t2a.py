from pathlib import Path
import openai
import os

# 讀取 API 金鑰
keyfile = Path("/Users/ty/Desktop/internetsystem/a.env/key.txt")
key = keyfile.read_text()
openai.api_key = key

speech_file_path = Path("/Users/ty/Desktop") / "speech.mp3"

user_question = input("請輸入要轉成語音的文字: ")

response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=user_question
)
response.stream_to_file(speech_file_path)
 
audio_file= open("/Users/ty/Desktop/speech.mp3", "rb")
transcription = openai.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
