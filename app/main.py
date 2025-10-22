from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import inference, notebook

# Initialize FastAPI app
app = FastAPI(title="EdgeServer LLM Server", version="1.0.0")

# -------------------------------------------------------------------
# 🧠 CORS Setup – allows your frontend (Vite/React) to connect
# -------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------------
# 🔗 Include backend route modules
# -------------------------------------------------------------------
app.include_router(inference.router)
app.include_router(notebook.router)

# -------------------------------------------------------------------
# 🏠 Root Route
# -------------------------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Edge LLM Server is running!",
        "endpoints": ["/predict", "/models", "/run_cell"]
    }
