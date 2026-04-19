# Catálogo Avançado de Borda, Plataformas (BaaS/CMS), Storage e Inteligência Artificial (MLOps/LLMOps)

Este documento fornece referências arquiteturais sólidas (Gold Standards) para a camada de infraestrutura avançada e operações de IA.

## 🧠 IA Interpretation Guidelines
1. **Model Evolution**: O agente deve consultar o repositório se precisar implementar uma nova técnica de RAG ou compressão de contexto.
2. **Safety First**: Repositórios de AI Safety (ex: Garak, NeMo) devem ser consultados pelo agente **Shield** antes de deploys em produção.
3. **Skill Link**: Cross-reference com o catálogo de skills em [[.agent/skills/catalog/(security)/README.md]].

## Fase 1 — Fundação adicional de arquitetura e borda

### Categoria: API Gateway / Edge / Reverse Proxy
* **envoyproxy/gateway** — [GitHub](https://github.com/envoyproxy/gateway)
  *O que ensina para a IA*: gerenciamento do Envoy como gateway standalone ou em Kubernetes via Gateway API.
  *Uso*: modelar entrada de tráfego, políticas de gateway e exposição segura de serviços cloud-native. Nível: avançado.

* **traefik/traefik** — [GitHub](https://github.com/traefik/traefik)
  *O que ensina para a IA*: reverse proxy e load balancer cloud-native com descoberta dinâmica de serviços.
  *Uso*: projetar roteamento dinâmico integrado ao Docker/K8s sem configuração manual pesada. Nível: intermediário.

### Categoria: DevSecOps / Scan de infraestrutura e supply chain
* **aquasecurity/trivy** — [GitHub](https://github.com/aquasecurity/trivy)
  *O que ensina para a IA*: scanning de vulnerabilidades, misconfigurations e secrets em imagens e repositórios.
  *Uso*: scanning integrado a pipelines CI/CD e auditoria de infraestrutura/containers. Nível: avançado.

* **bridgecrewio/checkov** — [GitHub](https://github.com/bridgecrewio/checkov)
  *O que ensina para a IA*: análise estática de infraestrutura como código (IaC) e SCA.
  *Uso*: validar manifestos Terraform, CloudFormation e CI/CD policies. Nível: avançado.

---

## Fase 2 — Plataformas de aplicação, conteúdo e backends prontos

### Categoria: Backend as a Service / App Platform
* **appwrite/appwrite** — [GitHub](https://github.com/appwrite/appwrite)
  *Uso*: acelerar produtos (auth, DB, storage, functions) baseados numa plataforma BaaS já desenhada. Nível: intermediário.

* **supabase/supabase** — [GitHub](https://github.com/supabase/supabase)
  *Uso*: plataforma de desenvolvimento conectada a PostgreSQL para aplicativos que usam conexões realtime e RLS nativo. Nível: intermediário.

* **pocketbase/pocketbase** — [GitHub](https://github.com/pocketbase/pocketbase)
  *Uso*: produtos leves ou de rápido protótipo baseados em um único binário com SQLite e Realtime nativos. Nível: iniciante.

### Categoria: Headless CMS / Content Platform / Admin-first backends
* **directus/directus** — [GitHub](https://github.com/directus/directus)
  *Uso*: envelopar bancos de dados existentes num Headless CMS robusto com painel admin e APIs. Nível: intermediário.

* **strapi/strapi** — [GitHub](https://github.com/strapi/strapi)
  *Uso*: publicar e arquitetar conteúdo estruturado onde os dados precisam estar separados rigorosamente do Frontend. Nível: intermediário.

### Categoria: Low-code / Internal tools / Business apps
* **nocobase/nocobase** — [GitHub](https://github.com/nocobase/nocobase)
  *Uso*: desenhar fluxos empresariais extensíveis orientados a plugins. Nível: intermediário.

* **Budibase/budibase** — [GitHub](https://github.com/Budibase/budibase)
  *Uso*: criar painéis de automação de processos internos atrelados aos bancos e IAs. Nível: intermediário.

---

## Fase 3 — Dados operacionais, storage e performance de base

### Categoria: Cache / In-memory data / realtime data structures
* **redis/redis** — [GitHub](https://github.com/redis/redis)
  *Uso*: fundamental para mensageria in-memory, controle de cache distribuído, pools de sessões e rate limits rápidos. Nível: avançado.

* **valkey-io/valkey** — [GitHub](https://github.com/valkey-io/valkey)
  *Uso*: alternativa puramente open source ao ecossistema Redis lidando com alto fluxo de chave-valor (Key-Value/KV). Nível: avançado.

### Categoria: Object Storage / File Infrastructure
* **minio/minio** — [GitHub](https://github.com/minio/minio)
  *Uso*: projetar Object Storage com protocolo compatível do S3 self-hosted rápido e clusterizado. Nível: avançado.

* **seaweedfs/seaweedfs** — [GitHub](https://github.com/seaweedfs/seaweedfs)
  *Uso*: desenhar arquiteturas de file storage escalonado p/ arquivos ou datasets multibilionários (Data Lakes, IA datasets). Nível: avançado.

---

## Fase 4 — IA aplicada, MLOps e LLMOps

### Categoria: MLOps / Model lifecycle
* **mlflow/mlflow** — [GitHub](https://github.com/mlflow/mlflow)
  *Uso*: controle do ciclo de treinamento e versionamento estrito (Lifecycle) dos pesos e parâmetros. Nível: avançado.

* **kubeflow/kubeflow** — [GitHub](https://github.com/kubeflow/kubeflow)
  *Uso*: administrar os pipelines MLOps nativamente dentro de um cluster K8s. Nível: avançado.

* **bentoml/BentoML** — [GitHub](https://github.com/bentoml/BentoML)
  *Uso*: arquiteturar o "Serving API" permitindo deploys consistentes de modelos na forma de rotas de inferência. Nível: avançado.

### Categoria: LLMOps / Observabilidade e avaliação de IA
* **langfuse/langfuse** — [GitHub](https://github.com/langfuse/langfuse)
  *Uso*: projetar tracking, traces e telemetria profunda sobre inputs/outputs do uso de LLMs (Token Metrics e custos). Nível: avançado.

* **Arize-ai/phoenix** — [GitHub](https://github.com/Arize-ai/phoenix)
  *Uso*: focar especificamente nas avaliações e observabilidade preditiva sobre pipelines de IA generativa e RAG. Nível: avançado.

### Categoria: Frameworks de RAG / agentic AI
* **deepset-ai/haystack** — [GitHub](https://github.com/deepset-ai/haystack)
  *Uso*: modularização completa do fluxo agentic onde peças de input e query são transparentemente conectadas. Nível: avançado.

* **run-llama/llama_index** — [GitHub](https://github.com/run-llama/llama_index)
  *Uso*: manipulação massiva e estruturação do parser e extração focado na indexação para os agentes de busca. Nível: avançado.

* **open-webui/open-webui** — [GitHub](https://github.com/open-webui/open-webui)
  *Uso*: empacotar ecossistemas LLM self-hosted em uma interface segura com conexões nativas p/ RAG offline. Nível: intermediário.
