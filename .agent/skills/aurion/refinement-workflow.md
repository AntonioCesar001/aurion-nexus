# Blueprint: Fluxo de Ideação e Refinamento

## 1. Recepção de Ideia (Aurion CEO)
O Aurion CEO recebe o input bruto no `Aurion-Interface.md` e aciona o squad administrativo.

## 2. Clarificação e Pesquisa (ResearchAgent)
- Investiga o contexto técnico da ideia.
- Identifica ambiguidades e solicita clarificação via Aurion CEO.
- Entrega um `RESEARCH_OUTPUT` com foco em viabilidade.

## 3. Otimização e Planejamento (PlannerAgent)
- Pega o output de pesquisa e a ideia original.
- Aplica padrões de otimização (ex: arquitetura limpa, segurança, escalabilidade).
- Converte a ideia em um conjunto de **Task Contracts** (P0/P1/P2).

## 4. Revisão e Quality Gate (ReviewerAgent)
- Valida se os contratos estão claros e possuem critérios de sucesso verificáveis.
- Garante que a "outra equipe de IA" terá tudo o que precisa para executar sem dúvidas.

## 5. Handoff para Especialistas
- Após aprovação, os contratos são enviados para os agentes em `agency-agents/`.
