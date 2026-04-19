# Catálogo de Referência de Engenharia para Agentes (Aurion)

Esta lista contém referências absolutas de arquitetura, padrões e engenharia mantidas para orçamentar agentes e sub-agentes no ecossistema Aurion Nexus quando eles precisarem ancorar suas escolhas arquiteturais em repositórios "Gold Standard" do Open Source. 

## Fase 1 — Fundação adicional da engenharia

### Categoria: Arquitetura de Backend — segunda camada
* **ardalis/CleanArchitecture** — [GitHub](https://github.com/ardalis/cleanarchitecture)
  - **O que ensina para a IA**: Clean Architecture como estrutura de solução, com dependência invertida e separação forte entre núcleo e infraestrutura.
  - **Uso**: Referência direta e objetiva para Clean Architecture. Usar quando a IA precisar aprender uma forma disciplinada de estruturar aplicação antes de entrar em DDD. Nível avançado.

* **CodelyTV/typescript-ddd-example** — [GitHub](https://github.com/CodelyTV/typescript-ddd-example)
  - **O que ensina para a IA**: DDD + Hexagonal + CQRS + EDA em TypeScript.
  - **Uso**: Muito próximo do ecossistema Node/TS. Usar para exemplos concretos de DDD sem inventar estrutura do zero. Nível avançado.

### Categoria: Documentação de Arquitetura e System Design
* **donnemartin/system-design-primer** — [GitHub](https://github.com/donnemartin/system-design-primer)
  - **O que ensina para a IA**: Bíblia completa de escalabilidade, load balancing, caching e trade-offs de bancos de dados.
  - **Uso**: Referência fundamental para desenhar sistemas que precisam escalar para milhões de usuários (Sovereign Scale). Usar para justificar sharding, filas e resiliência. Nível: Especialista.

* **mehdihadeli/awesome-software-architecture** — [GitHub](https://github.com/mehdihadeli/awesome-software-architecture)
  - **O que ensina para a IA**: Mapa completo de arquiteturas, padrões, e trade-offs. 
  - **Uso**: Excelente para consultar e justificar escolhas entre estilos arquiteturais. Nível intermediário.

## Fase 2 — Produto, interface e experiência

### Categoria: Frontend
* **mantinedev/mantine** — [GitHub](https://github.com/mantinedev/mantine)
  - **Uso**: Construir dashboards complexos e sistemas empresariais no React sem perder qualidade visual. "app-first".

* **storybookjs/design-system** — [GitHub](https://github.com/storybookjs/design-system)
  - **Uso**: Governança de UI, catálogos de componentes, documentação de ativos front-end mantidos por longos ciclos.

### Categoria: Mobile / Clientes
* **expo/expo** — [GitHub](https://github.com/expo/expo) (JavaScript universal)
* **flutter/flutter** — [GitHub](https://github.com/flutter/flutter) (Toolkit independente focado em Múltiplas Plataformas)
* **ionic-team/ionic-framework** — [GitHub](https://github.com/ionic-team/ionic-framework) (Apps Nativos e PWAs derivados de Web Components)

## Fase 3 — Dados, descoberta e conhecimento

### Categoria: Busca / Search / Retrieval / RAG
* **meilisearch/meilisearch** — [GitHub](https://github.com/meilisearch/meilisearch) (Busca textual e autocomplete ágil e híbrida)
* **qdrant/qdrant** — [GitHub](https://github.com/qdrant/qdrant) (Banco vetorial "Gold Standard" em RAG no open source)
* **onyx-dot-app/onyx** — [GitHub](https://github.com/onyx-dot-app/onyx) (Camada de aplicação para LLMs voltada a empresas corporativas, Knowledge Platform profunda)

### Categoria: Analytics / Data Pipelines
* **airbytehq/airbyte** — [GitHub](https://github.com/airbytehq/airbyte) (Conectores ELT entre APIs em massa)
* **dbt-labs/dbt-core** — [GitHub](https://github.com/dbt-labs/dbt-core) (Transformação e testes de Data Analytics)

## Fase 4 — Releases, commerce e growth

### Categoria: Release Management e Experimentos
* **Unleash/unleash** — [GitHub](https://github.com/unleash/unleash) (Feature Management / Kill Switches)
* **growthbook/growthbook** — [GitHub](https://github.com/growthbook/growthbook) (Testes A/B interligados ao desenvolvimento)

### Categoria: Billing
* **killbill/killbill** — [GitHub](https://github.com/killbill/killbill) (Pagamentos recorrentes e relatórios)
* **medusajs/medusa** — [GitHub](https://github.com/medusajs/medusa) (Módulos de E-commerce composable, Checkout logic)

## Fase 5 — Colaboração e Realtime

* **mattermost/mattermost** — [GitHub](https://github.com/mattermost/mattermost) (Chat corporativo, segurança interna e automação de dev)
* **signalapp/Signal-Server** — [GitHub](https://github.com/signalapp/Signal-Server) (Comunicação voltada estritamente à segurança extrema)
* **AppFlowy-IO/AppFlowy** — [GitHub](https://github.com/AppFlowy-IO/AppFlowy) (Workspace colaborativo privado "Notion-like")

## Fase 6 — Qualidade, segurança e supply chain

* **vitest-dev/vitest** — [GitHub](https://github.com/vitest-dev/vitest) (Framework moderno para TS)
* **testing-library/react-testing-library** — [GitHub](https://github.com/testing-library/react-testing-library) (Behavior-driven UI test)
* **apache/casbin** — [GitHub](https://github.com/apache/casbin) (Role/ACL in loco)
* **authzed/spicedb** — [GitHub](https://github.com/authzed/spicedb) (Zanzibar Fine-Grained Authorization)
* **in-toto/in-toto** — [GitHub](https://github.com/in-toto/in-toto) (Segurança extrema em Supply Chain)
* **ossf/scorecard** — [GitHub](https://github.com/ossf/scorecard) (Auditoria estática de Repo Maturity)

## Fase 7 — Observabilidade e Assíncrono

### Categoria: Observabilidade dos 4 pilares (Grafana Stack)
* **open-telemetry/opentelemetry-js** — Instrumentação para APIs
* **grafana/loki** — Logs Estruturados
* **grafana/tempo** — Tracing distribuído
* **grafana/pyroscope** — Profiling de RAM/CPU em background (quarta dimensão)

### Categoria: Filas, CDC e Mensageria
* **nats-io/nats-server** — pub/sub mega ágil no Edge
* **apache/pulsar** — Filas robustas concorrente do Kafka
* **debezium/debezium** — CDC ("Change Data Capture") outbox real do banco SQL direto para tópicos event-driven

### Categoria: Workflows e Orquestração
* **PrefectHQ/prefect** — Workflows de Data Python Event-driven
* **argoproj/argo-workflows** — Containers/DAG pipelines (Cloud/Kubernetes)
* **kestra-io/kestra** — Scheduling orquestrado declarative (YAML/UI)
* **conductor-oss/conductor** — SAGAs complexos para microserviços (Netflix architecture)

## Fase 8 — Entrega GitOps e Plataforma

* **argoproj/argo-cd** — Integração "GitOps" (Mudança declarativa da Cloud via Repo Commit)
* **nektos/act** — Validar Github Actions e Pipelines localmente (Dry / Docker)
