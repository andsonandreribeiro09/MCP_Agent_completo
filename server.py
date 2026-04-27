# server.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from tools import calcular, ler_arquivo, apresentar_video

# =========================
# 🧠 IMPORTAÇÃO DOS TOOLS
# =========================
from tools import (
    calcular,
    ler_arquivo,
    falar,
    apresentar_video
)

app = FastAPI()

# =========================
# 🌐 CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# 📦 REQUEST MCP
# =========================
class ToolRequest(BaseModel):
    tool_name: str
    input: str = ""


# =========================
# ⚙️ EXECUTOR MCP
# =========================
@app.post("/execute")
def execute_tool(req: ToolRequest):

    if req.tool_name == "calcular":
        result = calcular(req.input)

    elif req.tool_name == "ler_arquivo":
        result = ler_arquivo(req.input)

    elif req.tool_name == "falar":
        result = falar(req.input)

    # 🎬 NOVO: VÍDEO (SUBSTITUI PPT COMPLETO)
    elif req.tool_name == "apresentar_video":
        result = apresentar_video(req.input)

    else:
        result = "Tool não encontrada"

    return {"result": result}

#   python -m uvicorn server:app --reload