import streamlit as st
from client import MCPClient
import time
import os

# Inicializa MCP Client
client = MCPClient()

# =========================
# 🤖 AGENT
# =========================
def agent(pergunta: str):

    pergunta_lower = pergunta.lower()

    # 🔢 cálculo por palavras
    if any(p in pergunta_lower for p in ["calcule", "calcular", "quanto é", "faz a conta"]):
        expressao = (
            pergunta_lower
            .replace("calcule", "")
            .replace("calcular", "")
            .replace("quanto é", "")
            .replace("faz a conta", "")
            .strip()
        )

        return client.call_tool("calcular", expressao)

    # 🔢 cálculo direto
    elif any(op in pergunta_lower for op in ["+", "-", "*", "/"]):
        return client.call_tool("calcular", pergunta_lower)

    # 📄 leitura de arquivo
    elif any(p in pergunta_lower for p in ["leia", "abra", "mostre o arquivo"]):
        palavras = pergunta_lower.split()

        for palavra in palavras:
            if ".txt" in palavra:
                return client.call_tool("ler_arquivo", palavra)

        return "Não encontrei o nome do arquivo."

    # 🧠 MCP info
    elif "mcp" in pergunta_lower:
        return client.call_tool("ler_arquivo", "dados.txt")

    else:
        return (
            "Posso te ajudar com:\n"
            "- Cálculos\n"
            "- Leitura de arquivos\n"
            "- Explicações sobre MCP"
        )


# =========================
# 🎨 UI
# =========================
st.set_page_config(page_title="MCP Agent", layout="centered")

st.title("🤖 MCP Agent Inteligente")
st.write("Sistema com Agent + MCP + FastAPI")

st.sidebar.title("⚙️ Sobre")
st.sidebar.info("Fluxo: User → Agent → MCP → Tools")

def limpar_markdown(texto: str):
    return (
        texto
        .replace("👉", "\n👉")
        .replace("🔄", "\n🔄")
        .replace("🧠", "\n🧠")
        .replace("🔌", "\n🔌")
    )
# =========================
# 💬 CHAT
# =========================
if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Digite sua mensagem...")

if user_input:
    resposta = agent(user_input)

    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("assistant", resposta))


for role, msg in st.session_state.chat:
    with st.chat_message(role):
         st.markdown(limpar_markdown(msg))


# =========================
# 🎬 VÍDEO (SUBSTITUI PPT)
# =========================
st.markdown("---")
st.markdown("## 🎬 Apresentação em Vídeo (MCP)")

arquivo_video = st.text_input(
    "Caminho do vídeo:",
    "apresentacao.mp4",
    label_visibility="collapsed"
)

if st.button("▶️ Abrir vídeo"):

    if not os.path.exists(arquivo_video):
        st.error("Arquivo não encontrado")
    else:
        st.video(arquivo_video)  # 🔥 AQUI É O FIX REAL
        #st.success("Vídeo carregado na interface!")
#  python -m streamlit run app.py