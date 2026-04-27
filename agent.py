# agent.py
from client import MCPClient

client = MCPClient()

def agent(pergunta: str):
    
    if "calcule" in pergunta.lower():
        expressao = pergunta.lower().replace("calcule", "").strip()
        return client.call_tool("calcular", expressao)

    elif "leia o arquivo" in pergunta.lower():
        caminho = pergunta.lower().replace("leia o arquivo", "").strip()
        return client.call_tool("ler_arquivo", caminho)

    else:
        return "Não sei como ajudar com isso ainda."

if __name__ == "__main__":
    while True:
        pergunta = input("Você: ")
        resposta = agent(pergunta)
        print("Agent:", resposta)