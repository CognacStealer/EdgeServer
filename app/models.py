# model.py
# ---------------------------------------------------------------------------
# EdgeServer Ultra-Light Model Loader (CPU-Optimized, No RAG)
# ---------------------------------------------------------------------------
# Features:
# ✅ Runs fully on CPU
# ✅ Low hallucination, concise factual answers
# ✅ Uses TinyLlama (instruction-tuned)
# ✅ Clean and lightweight — no retriever, no external DB
# ---------------------------------------------------------------------------

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ---------------------------------------------------------------------------
# MODEL CONFIGURATION
# ---------------------------------------------------------------------------
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

SYSTEM_PROMPT = (
    "You are EdgeServer, a concise and factual assistant. "
    "Always answer briefly and truthfully. "
    "If unsure, say 'I’m not sure about that.'"
)

print(f"🔹 Loading CPU-friendly model: {MODEL_NAME}")

# ---------------------------------------------------------------------------
# DEVICE SELECTION
# ---------------------------------------------------------------------------
device = "cpu"
print(f"💻 Using device: CPU")

# ---------------------------------------------------------------------------
# LOAD MODEL & TOKENIZER
# ---------------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,  # CPU safe
    low_cpu_mem_usage=True
)

# ---------------------------------------------------------------------------
# CREATE PIPELINE
# ---------------------------------------------------------------------------
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU mode
)

print(f"✅ Model '{MODEL_NAME}' loaded successfully on CPU!")

# ---------------------------------------------------------------------------
# GENERATE RESPONSE
# ---------------------------------------------------------------------------
def generate_response(prompt: str, max_new_tokens: int = 100):
    """
    Generate a concise and factual response using TinyLlama.
    """
    try:
        max_new_tokens = int(max_new_tokens)
    except Exception:
        max_new_tokens = 100

    full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}\nAssistant:"

    outputs = pipe(
        full_prompt,
        max_new_tokens=max_new_tokens,
        temperature=0.2,           # low temperature => more factual
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=False            # deterministic output for stable answers
    )[0]["generated_text"]

    # Strip prompt from the start of the generated text
    if outputs.startswith(full_prompt):
        outputs = outputs[len(full_prompt):]

    return outputs.strip()

# ---------------------------------------------------------------------------
# AVAILABLE MODEL OPTIONS
# ---------------------------------------------------------------------------
def list_available_models():
    return [
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # ✅ best factual CPU model
        "tiiuae/falcon-1b-instruct",           # slightly heavier
        "microsoft/phi-2"                      # more factual but slower on CPU
    ]

# ---------------------------------------------------------------------------
# DEMO TEST (optional)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_prompt = input("\n🧠 Ask a question: ")
    print("\n🤖 Assistant:", generate_response(test_prompt))
