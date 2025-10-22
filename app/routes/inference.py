from fastapi import APIRouter, Header, HTTPException, Query
from app.models import generate_response, list_available_models
import json

router = APIRouter()

# Load user tokens from file
with open("users.json") as f:
    USERS = json.load(f)

# Token verification
def verify_token(x_api_key: str):
    if x_api_key not in USERS.values():
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# ------------------ ROUTES ----------------------

@router.get("/predict")
def predict(
    input: str = Query(..., description="User input text"),
    x_api_key: str = Header(...),
    max_new_tokens: int = 300
):
    # Verify user
    token = verify_token(x_api_key)
    username = [u for u, t in USERS.items() if t == token][0]

    # Generate response
    output = generate_response(input, max_new_tokens=max_new_tokens)
    return {"user": username, "input": input, "prediction": output}


@router.get("/models")
def get_models():
    return {"available_models": list_available_models()}
