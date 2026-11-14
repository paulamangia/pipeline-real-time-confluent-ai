[README.md](https://github.com/user-attachments/files/34855110/README.md)
# Pipeline Real-Time End-to-End com Confluent Cloud e Agentes de IA

Projeto desenvolvido para o Desafio de Projeto da trilha **IBM - Confluent: Dados em tempo real para agentes de IA** na plataforma [DIO](https://dio.me).

---

## 🎯 Objetivo do Projeto
Demonstrar a construção de um pipeline de dados em tempo real utilizando a arquitetura orientada a eventos com **Confluent Cloud (Apache Kafka)** e **Apache Flink SQL**, alimentando um **Agente de IA** responsável por analisar sentimentos de chamados de clientes e priorizar atendimentos críticos instantaneamente.

---

## 🏗️ Arquitetura do Pipeline

```
  [ Cliente / Sistema de Origem ]
                 │
                 ▼
     [ Schema Registry (JSON) ] ──── Validação de Contrato
                 │
                 ▼
  [ Tópico Kafka: chamados_suporte ] (Entrada Bruta)
                 │
                 ▼
       [ Apache Flink SQL ] ──────── Limpeza e Filtro Contínuo
                 │
                 ▼
  [ Tópico Kafka: chamados_para_ia ] (Dados Higienizados)
                 │
                 ▼
        [ Agente de IA ] ─────────── Classificação e Roteamento
                 │
                 ▼
  [ Notificação / Atendimento Urgente ]
```

---

## 📁 Estrutura de Arquivos

* [`schemas/chamado_schema.json`](schemas/chamado_schema.json): Esquema de contrato de dados registrado para governança com Schema Registry.
* [`flink/transformacao_chamados.sql`](flink/transformacao_chamados.sql): Query de streaming contínuo em Flink SQL que filtra dados inválidos e roteia mensagens.
* [`agent/agent_consumer.py`](agent/agent_consumer.py): Script Python simulando o consumo dos eventos do Kafka e a tomada de decisão do Agente de IA.

---

## 💡 Principais Decisões de Arquitetura

1. **Desacoplamento e Baixa Latência:** Em vez de fazer a aplicação de atendimento aguardar requisições lentas, os eventos são inseridos no Apache Kafka com confirmação imediata.
2. **Governança via Schema Registry:** Garante compatibilidade e integridade estrutural das mensagens que circulam no cluster.
3. **Processamento In-Flight com Flink SQL:** Os dados são tratados e filtrados em voo, evitando sobrecarregar e gastar tokens desnecessários com o modelo de IA para mensagens vazias ou inválidas.
4. **Agente de IA Reativo:** Atua como consumidor em tempo real, respondendo a eventos em milissegundos para casos urgentes de clientes insatisfeitos.

---

## 🚀 Como Executar o Projeto Localmente

1. **Pré-requisitos:** Ter o Python 3 instalado.
2. **Executar o agente de teste:**
   ```bash
   cd agent
   python agent_consumer.py
   ```
3. O script demonstrará a leitura de eventos e a tomada de decisão automática do agente.
