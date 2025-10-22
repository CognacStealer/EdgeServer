# 🚀 EdgeServer — Local LLM Inference Server

**Author:** [@CognacStealer](https://github.com/CognacStealer)
**Version:** 1.0.0

EdgeServer is a lightweight **local LLM server** designed to run **TinyLlama (or similar small models)** on **low-end CPUs** efficiently.
It exposes **FastAPI endpoints** for inference and notebook-based fine-tuning, allowing **local model customization** without needing a high-end GPU.

---

## 🧩 Overview

**Core Idea:**

> EdgeServer allows any user — even with low-end hardware — to interact with and fine-tune small LLMs locally through a centralized server running entirely on CPU.
> It serves as a **bridge** that lets local clients (e.g., web apps, notebooks) use and fine-tune models efficiently via REST API requests.

### ✨ Features

* ✅ **CPU-optimized** — no GPU required
* ✅ **FastAPI backend** with CORS support
* ✅ Modular route system (`inference`, `notebook`)
* ✅ Preloaded **TinyLlama** (1.1B Chat) model
* ✅ **Deterministic, factual** output generation
* ✅ **Frontend-ready** (React / Vite compatible)

---

## 📁 Project Structure

```
EdgeServer/
│
├── app/
│   ├── routes/
│   │   ├── inference.py
│   │   ├── notebook.py
│   ├── __init__.py
│
├── model.py                 # Model loader (TinyLlama)
├── main.py                  # FastAPI server entry point
├── requirements.txt         # All dependencies
└── README.md                # You're reading this 🙂
```

---

## ⚙️ Setup Instructions

Follow these steps to set up and run **EdgeServer** locally.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/CognacStealer/EdgeServer.git
cd EdgeServer
```

---

### 2️⃣ Create a Virtual Environment

Creating a **virtual environment** isolates dependencies and ensures stability.

#### 🪟 On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Upgrade pip

```bash
pip install --upgrade pip
```

---

### 4️⃣ Install Dependencies

Create a `requirements.txt` file if not already present, with the following content:

```txt
fastapi
uvicorn
transformers
torch
sentencepiece
```

Then install:

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Server

Start your FastAPI app using **Uvicorn**:

```bash
uvicorn main:app --reload
```

**Expected Output:**

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

## 🌐 API Endpoints

| Endpoint    | Method | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| `/`         | GET    | Root route — status and available endpoints      |
| `/predict`  | POST   | Generate LLM response from user prompt           |
| `/models`   | GET    | List available models (TinyLlama, Falcon, Phi-2) |
| `/run_cell` | POST   | Execute notebook-style fine-tuning code          |

---

## 🧠 Example Usage

### 1️⃣ Test Root Endpoint

After the server is running:

```bash
curl http://127.0.0.1:8000/
```

Response:

```json
{
  "status": "ok",
  "message": "Edge LLM Server is running!",
  "endpoints": ["/predict", "/models", "/run_cell"]
}
```

---

### 2️⃣ Generate LLM Response

Example query:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"prompt": "Explain edge computing in one line"}'
```

Response:

```json
{
  "response": "Edge computing processes data closer to its source to reduce latency and bandwidth."
}
```

---

## 🧩 Model Configuration

Default model:
`TinyLlama/TinyLlama-1.1B-Chat-v1.0`

### Available Options

| Model Name                           | Description                              |
| ------------------------------------ | ---------------------------------------- |
| `TinyLlama/TinyLlama-1.1B-Chat-v1.0` | ⚡ Best lightweight factual model for CPU |
| `tiiuae/falcon-1b-instruct`          | 🦅 Slightly heavier but capable          |
| `microsoft/phi-2`                    | 🧩 More factual, slower on CPU           |

### Behavior Controls (in `model.py`)

* `temperature = 0.2` → factual responses
* `do_sample = False` → deterministic output
* `repetition_penalty = 1.1` → prevents looping
* `SYSTEM_PROMPT` defines assistant personality

---

## 🧠 Project Goals

EdgeServer acts as a **local AI node** that:

* Helps **low-end systems** perform model inference or fine-tuning
* Allows **LAN or shared access** to local LLMs
* Enables **fine-tuning within notebooks** for domain-specific use cases

---

## 🧰 Developer Notes

* Runs fully on **CPU** (torch float32 + `low_cpu_mem_usage=True`)
* Extend routes easily inside `/app/routes`
* Can be deployed on **LAN** for multiple clients
* Ideal for **edge AI** and **lightweight inference** setups

---

## 🧾 License

This project is released under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

## 👨‍💻 Author

**EdgeServer**
Developed & maintained by **[@CognacStealer](https://github.com/CognacStealer)**
Contributions and improvements are always welcome!

---

Would you like me to add a **Docker deployment section** (so others can run this instantly using one command like `docker run cognacstealer/edgeserver`)? It’ll make this project plug-and-play for LAN and Raspberry Pi environments.
