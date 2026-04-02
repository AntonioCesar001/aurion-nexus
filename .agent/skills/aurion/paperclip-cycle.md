# Ciclo Operativo Paperclip (v1)

Para garantir que o Paperclip utilize o time **Aurion** de forma eficiente, seguimos o ciclo de 72 horas:

## ⏳ Fase 1: Ingestão e Refinamento (0h - 24h)
- 00h: **Paperclip** recebe input do usuário.
- 02h: **Aurion (Planner)** decompõe o objetivo.
- 06h: **Aurion (Research)** valida viabilidade técnica.
- 12h: **Aurion (Reviewer)** valida o contrato de execução.
- 24h: **Checkpoint T+24** (Baseline aprovada).

## 🛠️ Fase 2: Execução e Qualidade (24h - 48h)
- 26h: **Aurora Squad** inicia execução paralela (Backend, UI, AI).
- 36h: **Paperclip (DevOps)** configura ambiente de staging.
- 48h: **Checkpoint T+48** (Review parcial e testes de integração).

## 🚀 Fase 3: Validação e Entrega (48h - 72h)
- 50h: **Paperclip (Security/QA)** realiza gates de segurança e testes E2E.
- 60h: **Paperclip (Shepherd)** consolida a entrega.
- 72h: **Checkpoint T+72** (Deploy prod/Vercel e relatório final).

---
> [!NOTE]
> O Paperclip prioriza a **qualidade** sobre a velocidade em ciclos T-3 (72h).
