import math
import unicodedata
import pyttsx3
import win32com.client
import os
import time
from pptx import Presentation
import subprocess



# 🔊 engine de voz
engine = pyttsx3.init()


def falar(texto):
    engine.say(texto)
    engine.runAndWait()
    return "Falando..."


# 🔤 normalização
def normalizar(texto):
    return unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII").lower()


# 🔢 cálculo (mantido como está)
def calcular(expressao: str):
    try:
        return str(eval(expressao))
    except Exception as e:
        return f"Erro no cálculo: {e}"


# 📄 leitura de arquivo
def ler_arquivo(caminho: str):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(caminho, "r", encoding="latin-1") as f:
                return f.read()
        except Exception as e:
            return f"Erro ao ler arquivo: {e}"
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"
    

# =========================
# 🎬 VÍDEO (SUBSTITUI PPT COMPLETAMENTE)
# =========================
_video_ativo = None

import os

def apresentar_video(caminho: str):
    try:
        if not os.path.exists(caminho):
            return {"erro": "Arquivo não encontrado", "caminho": caminho}

        os.startfile(caminho)  # 🔥 abre instantaneamente no player padrão

        return {
            "status": "ok",
            "arquivo": caminho,
            "tipo": "video_mp4"
        }

    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}