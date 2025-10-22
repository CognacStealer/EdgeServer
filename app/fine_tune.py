from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset
import os, json
from datetime import datetime

MODELS_DIR = os.path.join(os.path.dirname(__file__), "../user_models")
os.makedirs(MODELS_DIR, exist_ok=True)

def fine_tune_model(base_model: str, user: str, data: list[dict]):
    """Fine-tune a model using user data."""
    model_path = os.path.join(MODELS_DIR, f"{user}_{base_model}_{datetime.now().strftime('%Y%m%d%H%M%S')}")
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model)

    dataset = Dataset.from_list(data)
    dataset = dataset.map(lambda x: tokenizer(x["prompt"], truncation=True, padding="max_length"), batched=True)

    training_args = TrainingArguments(
        output_dir=model_path,
        per_device_train_batch_size=1,
        num_train_epochs=1,
        save_strategy="epoch",
        logging_dir=f"{model_path}/logs",
    )

    trainer = Trainer(model=model, args=training_args, train_dataset=dataset)
    trainer.train()

    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)

    return {"status": "success", "model_path": model_path}
