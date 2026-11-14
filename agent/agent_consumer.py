"""
Agente de IA Consumidor de Eventos em Tempo Real
Conecta ao fluxo de dados preparado pelo Confluent Cloud / Flink SQL
e realiza análise de sentimento e priorização em tempo real.
"""

import json
import time

def analisar_com_ia(mensagem: str) -> dict:
    """
    Simula a inteligência do agente de IA.
    Em um ambiente produtivo, este ponto conecta a LLMs como watsonx.ai, Gemini ou GPT.
    """
    termos_criticos = ["atrasado", "cancelar", "péssimo", "horrível", "procon", "processo", "urgente"]
    mensagem_lower = mensagem.lower()
    
    for termo in termos_criticos:
        if termo in mensagem_lower:
            return {
                "sentimento": "CRÍTICO/NEGATIVO",
                "prioridade": "ALTA",
                "acao_sugerida": "Encaminhar imediatamente para atendente humano nível 2"
            }
            
    return {
        "sentimento": "NEUTRO/POSITIVO",
        "prioridade": "NORMAL",
        "acao_sugerida": "Responder via assistente virtual com FAQ padrão"
    }

def executar_agente():
    # Exemplos de eventos entregues pelo fluxo Kafka/Flink
    chamados_stream = [
        {
            "id_chamado": "TKT-101",
            "cliente": "Carlos Silva",
            "mensagem": "Como faço para alterar meu endereço de entrega cadastrado?"
        },
        {
            "id_chamado": "TKT-102",
            "cliente": "Mariana Souza",
            "mensagem": "Meu pedido está 10 dias atrasado e o suporte não responde! Quero cancelar tudo!"
        },
        {
            "id_chamado": "TKT-103",
            "cliente": "Roberto Dias",
            "mensagem": "Gostaria de saber quais as formas de pagamento disponíveis."
        }
    ]

    print("=" * 65)
    print(" 🚀 AGENTE DE IA EM TEMPO REAL CONECTADO AO CONFLUENT CLOUD")
    print("=" * 65)
    print("Ouvindo tópico Kafka: 'chamados_para_ia'...\n")

    for evento in chamados_stream:
        print(f"📥 [NOVO EVENTO RECEBIDO] ID: {evento['id_chamado']} | Cliente: {evento['cliente']}")
        print(f"💬 Mensagem: \"{evento['mensagem']}\"")
        
        # Análise em tempo real pelo agente
        decisao = analisar_com_ia(evento["mensagem"])
        
        print(f"🤖 [DECISÃO DA IA]:")
        print(f"   • Prioridade:  {decisao['prioridade']}")
        print(f"   • Sentimento:  {decisao['sentimento']}")
        print(f"   • Encaminhamento: {decisao['acao_sugerida']}")
        print("-" * 65)
        time.sleep(1)

    print("\n✅ Fluxo demonstrativo finalizado com sucesso!")

if __name__ == "__main__":
    executar_agente()
