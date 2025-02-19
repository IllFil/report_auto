from src.audio_to_text.whisper import get_transcript
from src.llm.model import get_model_res
from src.utils.pdf_create import save_pdf_transcript, model_report_pdf

model_name = 'gpt-4o-mini-2024-07-18'
transcript = get_transcript(r'C:\Users\ilyaf\Documents\report_auto\voice_lab\deposition.mp3')
save_pdf_transcript("transcript.pdf", "Transcript", transcript)
res = get_model_res(model_name,transcript)
model_report_pdf("model_output.pdf",  res)

print(res)