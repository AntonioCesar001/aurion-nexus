# Guia de Alta Complexidade: Uso do NotebookLM

O **NotebookLM** deve ser acionado tanto pelo time **Aurion** quanto pelo **Aurora** sempre que um projeto exigir uma camada superior de análise de dados, pesquisa técnica ou síntese de contexto.

## 1. Gatilhos de Ativação (Quando usar?)
- **Arquiteturas Multi-Nuvem**: Desenhos de sistemas que cruzam diversos provedores.
- **Análise Legada**: Processamento de grandes volumes de documentação pré-existente.
- **Pesquisa de Estado da Arte**: Quando o squad precisar de benchmarks técnicos pesados.
- **Documentação de Sistema**: Gerar bases de conhecimento ricas a partir de código-fonte.

## 2. Fluxo de Invocação
1. **Identificação**: O Aurion CEO ou o Squad Lead da Aurora identifica a necessidade de "Higher Intelligence".
2. **Invocação**: O `ResearchAgent` (para Aurion) ou o `backend-architect` (para Aurora) aciona o `notebooklm-mcp`.
3. **Síntese**: O output deve ser condensado em uma recomendação prática no contrato de execução.

---
> [!TIP]
> Use o NotebookLM para criar "Second Opinion" em decisões críticas de segurança ou escalabilidade.
