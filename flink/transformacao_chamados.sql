-- ========================================================
-- PIPELINE EM TEMPO REAL COM FLINK SQL (CONFLUENT CLOUD)
-- ========================================================

-- 1. Tabela conectada ao tópico Kafka de entrada (chamados brutos)
CREATE TABLE chamados_suporte (
    id_chamado STRING,
    cliente STRING,
    mensagem STRING,
    data_envio TIMESTAMP(3)
) WITH (
    'connector' = 'kafka',
    'topic' = 'chamados_suporte',
    'format' = 'json'
);

-- 2. Tabela conectada ao tópico Kafka de saída (chamados filtrados para IA)
CREATE TABLE chamados_para_ia (
    id_chamado STRING,
    cliente STRING,
    mensagem STRING
) WITH (
    'connector' = 'kafka',
    'topic' = 'chamados_para_ia',
    'format' = 'json'
);

-- 3. Inserção contínua: filtra chamados com mensagens válidas
INSERT INTO chamados_para_ia
SELECT 
    id_chamado,
    cliente,
    TRIM(mensagem) AS mensagem
FROM chamados_suporte
WHERE mensagem IS NOT NULL AND CHAR_LENGTH(TRIM(mensagem)) > 5;
