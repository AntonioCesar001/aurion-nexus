---
title: "Estratégias de redução de tokens em multi-agentes"
created: 2026-04-19T02:31:48.343024+00:00
source: agent-session
tags: token-economics, llmops, cost-optimization
---

# Estratégias de redução de tokens em multi-agentes

As 4 melhores práticas do mercado para reduzir consumo: 1) Model Routing (Haiku para triagem, Opus para execução), 2) Prompt Caching (90% de redução em input tokens repetidos), 3) Compressão de Contexto (nunca passar HTML bruto entre agentes), 4) Workflow Pruning (usar linters determinísticos antes de LLM reviewers).
