from fastapi import APIRouter, Header, HTTPException
import io, contextlib, traceback, sys

router = APIRouter()

@router.post("/run_cell")
def run_notebook_cell(code: str, x_api_key: str = Header(...)):
    try:
        local_vars = {}
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(code, {}, local_vars)
        output = buf.getvalue()
        return {"output": output, "variables": list(local_vars.keys())}
    except Exception as e:
        return {"error": str(e), "traceback": traceback.format_exc()}
