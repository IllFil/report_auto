from src.audio_to_text.whisper import get_transcript
from src.llm.model import get_model_res
from src.utils.pdf_create import save_pdf_transcript, model_report_pdf
from src.utils.convert_m4a_to_mp3 import convert_m4a_to_mp3

MODEL_NAME = 'gpt-4o-mini-2024-07-18'
m4a_path = r'C:\Users\ilyaf\Documents\report_auto\voice_lab\Voice 250218_110524.m4a'
mp3_path = r'C:\Users\ilyaf\Documents\report_auto\voice_lab\Voice 250218_110524.mp3'
convert_m4a_to_mp3(m4a_path, mp3_path)
transcript = get_transcript(r'C:\Users\ilyaf\Documents\report_auto\voice_lab\Voice 250218_110524.mp3')
save_pdf_transcript("transcript.pdf", "Transcript", transcript)
res = get_model_res(MODEL_NAME,transcript)
model_report_pdf(res)

print(res)