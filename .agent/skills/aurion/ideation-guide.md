# Guia de Ideação e Otimização (KnowledgeAgent)

Este guia define como o **KnowledgeAgent** deve processar inputs brutos do usuário para transformá-los em briefings de alta performance para a equipe técnica.

## 1. Princípios de Otimização
- **Clareza de Objetivo**: Definir o "Porquê" antes do "Como".
- **Decomposição Inteligente**: Quebrar ideias complexas em módulos independentes (P0/P1/P2).
- **Antecipação de Riscos**: Identificar potenciais gargalos técnicos, de segurança ou de escalabilidade.
- **Contexto Rico**: Adicionar referências a tecnologias, bibliotecas e padrões de design relevantes.

## 2. Checklist de Refinamento
Antes de enviar para a equipe de IA, o briefing deve responder:
1. Qual o output exato esperado?
2. Quais são as restrições técnicas (stack, performance, custos)?
3. Como a entrega será validada? (Critérios de Aceite).
4. Existem dependências externas?

## 3. Formato de Saída (The "Golden Briefing")
Todo refinamento deve resultar em um **Contract** seguindo o schema `task_contract.schema.json`.

---
> [!TIP]
> Use o histórico de sucessos e falhas armazenado na memória operacional para sugerir melhorias proativas em cada nova ideia.
