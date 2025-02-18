from src.audio_to_text.whisper import get_transcript
from src.llm.model import get_model_res


model_name = 'gpt-4o-mini-2024-07-18'
transcript = get_transcript(r'C:\Users\ilyaf\Documents\report_auto\voice_lab\deposition.mp3')
res = get_model_res(model_name,transcript)

print(res)