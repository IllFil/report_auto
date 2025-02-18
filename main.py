import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline, AutoTokenizer
from datasets import load_dataset

device = "cuda:0" if torch.cuda.is_available() else "cpu"

if device == "cuda:0":
    print("Using GPU")

torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"
print("Loading tokenizer")
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
print("Model loaded")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    chunk_length_s=30,
    batch_size=16,
    device=device,
)


result = pipe("voice_lab/Voice 250218_090553.mp3")
print(result["text"])