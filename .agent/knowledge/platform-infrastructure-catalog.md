# Catálogo de Referência de Plataforma e Infraestrutura para Agentes (Aurion)

Esta lista contém referências de infraestrutura, plataforma e SRE para orçamentar decisões de gateways, segurança e K8s.

## 🧠 IA Interpretation Guidelines
1. **Infrastructure as Code**: Se a tarefa envolver terraform ou k8s, consulte a Fase 2 antes de gerar manifestos.
2. **Security & Secrets**: O agente **Shield** deve validar o uso de segredos baseado no [hashicorp/vault] deste catálogo.
3. **Observation**: Use as referências de Monitoramento (Fase 3) para estruturar logs e status pages.
4. **Linking**: Conecte com os protocolos de infra em [[.agent/skills/aurora/infra-deploy/SKILL.md]].

## Fase 1 — Fundação adicional da plataforma e arquitetura

### Categoria: API Gateway
* **Kong/kong** — [GitHub](https://github.com/Kong/kong)
  O que ensina para a IA: gateway de API e de IA com foco em performance, extensibilidade por plugins e operação cloud-native.
  Uso: projetar borda de APIs, políticas de tráfego e centralização de concerns transversais. Nível: avançado.

* **krakend/krakend-ce** — [GitHub](https://github.com/krakend/krakend-ce)
  O que ensina para a IA: API Gateway stateless, declarativo e de alta performance.
  Uso: agregar APIs, compor respostas e hardening de borda sem acoplar lógica ao backend. Nível: avançado.

### Categoria: Service Mesh
* **istio/istio** — [GitHub](https://github.com/istio/istio)
  O que ensina para a IA: segurança, controle e observabilidade de tráfego entre serviços (mTLS, policies).
  Uso: comunicação entre microservices em Kubernetes com controle fino de tráfego. Nível: avançado.

* **linkerd/linkerd2** — [GitHub](https://github.com/linkerd/linkerd2)
  O que ensina para a IA: service mesh com foco em simplicidade operacional e baixa sobrecarga.
  Uso: quando o problema exigir service mesh com menor complexidade operacional. Nível: avançado.

---

## Fase 2 — Operação segura e infraestrutura de plataforma

### Categoria: Secrets / Gestão de Segredos
* **hashicorp/vault** — [GitHub](https://github.com/hashicorp/vault)
  O que ensina para a IA: gestão centralizada de segredos, criptografia como serviço e trilha de auditoria.
  Uso: projetar armazenamento e rotação segura de segredos em produção. Nível: avançado.

* **external-secrets/external-secrets** — [GitHub](https://github.com/external-secrets/external-secrets)
  O que ensina para a IA: sincronização de segredos externos (AWS/Vault) com Kubernetes Secrets por operador.
  Uso: infraestrutura Cloud/K8s integrando secrets providers externos. Nível: avançado.

### Categoria: Packaging / Configuração de Kubernetes
* **helm/helm** — [GitHub](https://github.com/helm/helm)
  O que ensina para a IA: empacotamento, instalação e gerenciamento de aplicações em Kubernetes.
  Uso: estruturar charts, releases e instalação de plataformas. Nível: intermediário.

* **kubernetes-sigs/kustomize** — [GitHub](https://github.com/kubernetes-sigs/kustomize)
  O que ensina para a IA: customização declarativa de YAML sem templates invasivos.
  Uso: versionar diferenças de K8s manifests entre dev, staging e produção. Nível: intermediário.

---

## Fase 3 — Operação externa, incidentes e comunicação operacional

### Categoria: Incident Management / Status Pages / Uptime
* **OneUptime/oneuptime** — [GitHub](https://github.com/OneUptime/oneuptime)
  O que ensina para a IA: monitoramento, incidentes, on-call, status page e observabilidade numa plataforma.
  Uso: modelar rotas de resposta a incidentes e status pages complexas. Nível: avançado.

* **TwiN/gatus** — [GitHub](https://github.com/TwiN/gatus)
  O que ensina para a IA: health dashboard, checks sintéticos e alerting developer-oriented leve.
  Uso: monitoramento e status page com baixa complexidade. Nível: intermediário.

### Categoria: Notificações / Communication Infrastructure
* **novuhq/novu** — [GitHub](https://github.com/novuhq/novu)
  O que ensina para a IA: infraestrutura unificada para in-app, email, SMS e push.
  Uso: desenhar centro de notificações multicanal e delivery de mensagens. Nível: intermediário.

---

## Fase 4 — Dados, qualidade, catálogo e governança de dados

### Categoria: Data Catalog / Metadata / Lineage
* **open-metadata/openmetadata** — [GitHub](https://github.com/open-metadata/openmetadata)
  O que ensina para a IA: catálogo central de metadados, governança, lineage.
  Uso: modelar catálogo, ownership e políticas de ativos de dados. Nível: avançado.

* **datahub-project/datahub** — [GitHub](https://github.com/datahub-project/datahub)
  O que ensina para a IA: plataforma de metadata, observabilidade e contexto de IA.
  Uso: pensar descoberta de dados em escala organizacional. Nível: avançado.

* **OpenLineage/OpenLineage** — [GitHub](https://github.com/OpenLineage/OpenLineage)
  O que ensina para a IA: padrão aberto para coleta de lineage.
  Uso: instrumentar pipelines e jobs com lineage consistente. Nível: avançado.

### Categoria: Data Quality
* **great-expectations/great_expectations** — [GitHub](https://github.com/great-expectations/great_expectations)
  O que ensina para a IA: validação declarativa de dados e checks de qualidade.
  Uso: validar qualidade de tabelas e datasets. Nível: intermediário.

---

## Fase 5 — Busca, conhecimento e retrieval

### Categoria: Search / Retrieval / Knowledge
* **meilisearch/meilisearch** — [GitHub](https://github.com/meilisearch/meilisearch)
  O que ensina para a IA: motor de busca textual rápido com foco em developer experience.
  Uso: modelar busca clássica textual e autocomplete. Nível: intermediário.

* **qdrant/qdrant** — [GitHub](https://github.com/qdrant/qdrant)
  O que ensina para a IA: banco vetorial com filtragem para busca semântica e RAG.
  Uso: semantic search e retrieval vetorial em produção. Nível: avançado.

---

## Fase 6 — Produto, growth e release controlada

### Categoria: Feature Flags / Experimentação
* **Unleash/unleash** — [GitHub](https://github.com/unleash/unleash)
  O que ensina para a IA: feature management, gradual rollout e kill switch.
  Uso: controle de release e flags por ambiente. Nível: avançado.

* **growthbook/growthbook** — [GitHub](https://github.com/growthbook/growthbook)
  O que ensina para a IA: experimentação e A/B tests vinculados ao desenvolvimento.
  Uso: product rollout voltado a métricas e analytics. Nível: avançado.

### Categoria: FinOps / Cost Management
* **opencost/opencost** — [GitHub](https://github.com/opencost/opencost)
  O que ensina para a IA: visibilidade de custos de Kubernetes e cloud spend.
  Uso: modelar transparência de gastos e custo por serviço. Nível: avançado.

---

## Fase 7 — Comércio, billing e operações de produto

### Categoria: Billing / Subscriptions
* **killbill/killbill** — [GitHub](https://github.com/killbill/killbill)
  O que ensina para a IA: billing, subscriptions e faturamento recorrente.
  Uso: modelar ciclos de cobrança, invoices e transações financeiras recorrentes. Nível: avançado.

* **medusajs/medusa** — [GitHub](https://github.com/medusajs/medusa)
  O que ensina para a IA: commerce open source e API-first server.
  Uso: modelagem composable de E-commerce, ordens e carrinhos. Nível: avançado.

### Categoria: Scheduling / Booking / Operations
* **calcom/cal.com** — [GitHub](https://github.com/calcom/cal.com)
  O que ensina para a IA: infra de agendamento de alto padrão.
  Uso: lógica de booking de equipes e gestão de slots self-hosted. Nível: intermediário.

---

## Fase 8 — Colaboração, realtime e trabalho em equipe

### Categoria: Collaboration / Realtime
* **mattermost/mattermost** — [GitHub](https://github.com/mattermost/mattermost)
  O que ensina para a IA: chatops, workflows e colaboração unificada.
  Uso: modelar chat corporativo e operações baseadas em discussões. Nível: avançado.

* **signalapp/Signal-Server** — [GitHub](https://github.com/signalapp/Signal-Server)
  O que ensina para a IA: mensageria criptografada e entrega privada segura.
  Uso: estudos arquiteturais de E2EE (End-to-End Encryption). Nível: avançado.
