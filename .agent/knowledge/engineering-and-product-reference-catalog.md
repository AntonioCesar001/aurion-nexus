# Catálogo Expandido: Engenharia, Produto e Inteligência (Aurion)

Esta lista compõe o Volume 2 das referências de padrão de ouro (Gold Standard) mantidas na base de conhecimento da Aurion.

## 🧠 IA Interpretation Guidelines
1. **Reference Check**: Antes de qualquer implementação de Backend ou Frontend, consulte as categorias "Arquitetura de Backend" ou "Frontend Estrutural".
2. **Domain Mapping**: Use os repositórios de "Domínio de Negócio" para extrair terminologia (Linguagem Ubíqua) para suas classes e tabelas.
3. **Security Anchor**: Repositórios da Fase 6 devem ser o seu "Vade Mecum" de segurança.
4. **Linking**: Conecte com os protocolos operacionais em [[.agent/skills/aurora/mission-protocol.md]].

## Fase 1 — Fundamentos de engenharia, estrutura e clareza

### Categoria: Arquitetura de Backend
* **Sairyss/domain-driven-hexagon** — DDD + Hexagonal + Clean/Onion com módulos e adapters reais. (Nível avançado)
* **kgrzybek/modular-monolith-with-ddd** — Monólito modular aplicado em larga escala (ERP/SaaS). (Nível avançado)

### Categoria: Frontend Estrutural
* **alan2207/bulletproof-react** — Estrutura de React escalável orientada a features/módulos para produção. (Nível intermediário)

## Fase 2 — Domínio, regras e negócio

### Categoria: Domínio de Negócio (Core)
* **ddd-by-examples/library** — Análise estratégica, linguagem ubíqua e padrões táticos REAIS de domínio. (Nível avançado)
* **ContextMapper/context-mapper-dsl** — Definição das fronteiras de domínio, contexts e limites estruturais de negócio. (Nível avançado)

### Categoria: Mercado / Produto / Analytics
* **PostHog/posthog** — Instrumentation de produto, web analytics, session replay e telemetry. (Nível intermediário)
* **metabase/metabase** — Business Intelligence simplificado e dashboards empresariais. (Nível intermediário)
* **apache/superset** — Visualização e Data Warehouse em larga escala de volume e regras. (Nível avançado)

### Categoria: Vendas / CRM / ERP
* **twentyhq/twenty** — CRM moderno (leads, pipelines comerciais, vendas). (Nível intermediário)
* **frappe/erpnext** — ERP robusto de negócio (vendas, estoque, RH, compras e financeiro empresarial). (Nível avançado)
* **saleor/saleor** — Lógica API-First para Carrinho, Pedido, Pagamento e Fulfillment B2C. (Nível avançado)

### Categoria: Social / Comunidade / Suporte
* **mastodon/mastodon** — ActivityPub e engine completa de rede social com grafos distribuídos. (Nível avançado)
* **discourse/discourse** — Fóruns, comunidades interativas, engagement e moderação central. (Nível avançado)
* **gitroomhq/postiz-app** — Automação e Postagem via API em redes sociais diversas. (Nível intermediário)
* **chatwoot/chatwoot** — Atendimento Onmichannel via web/CS (Desk Operacional). (Nível intermediário)

## Fase 3 — Produto e interface

* **shadcn-ui/ui** — Acessibilidade, Radix e componentes desacoplados de alto nível. (Nível intermediário)
* **radix-ui/primitives** — Primitivas (core logic) perfeitas e de alta confiabilidade para interfaces modernas. (Nível avançado)
* **style-dictionary/style-dictionary** — Tokens cross-platform de Design (Cores, Espaçamento, Temas). (Nível avançado)
* **primer/react** — O verdadeiro react-components do GitHub para uso em Escala de Enterprise. (Nível avançado)

## Fase 4 — Backend robusto e Integrações

### Categoria: API e Contratos
* **OAI/OpenAPI-Specification** — Definition of APIs as contracts. (Nível intermediário)
* **OpenAPITools/openapi-generator** — Geração massiva de stubs/SDK. (Nível intermediário)
* **stoplightio/spectral** — Linter rígido para YAML e governança de APIs. (Nível intermediário)
* **bufbuild/buf** — Protobuf e gRPC workflow. (Nível avançado)

### Categoria: Integrações de Evento
* **asyncapi/spec** — Design first para arquiteturas assíncronas e eventos. (Nível avançado)
* **pact-foundation/pact-js** — Teste formal de Integração/Contrato entre serviços isolados. (Nível avançado)
* **n8n-io/n8n** — Fluxos de integração visual entre serviços/código. (Nível intermediário)

## Fase 5 — Persistência
* **postgres/postgres** — O supra-sumo dos Bancos Transacionais e ACID compliant. (Nível avançado)
* **flyway/flyway** — Versão de Schemas (Migrations) disciplinadas independente de runtime. (Nível intermediário)
* **prisma/prisma** — Acesso e modelagem de Data Layers Tipadas massivamente util em TS. (Nível intermediário)

## Fase 6 — Segurança, Testes e Governança

### Segurança e IAM
* **OWASP/CheatSheetSeries** — Livro dourado prático de prevenção Anti-Exploits.
* **owasp/www-project-code-review-guide** — Revisões de Código orientadas a Vulnerabilidades Ativas.
* **keycloak/keycloak** — Autenticação de Federação, Single Sign-On (SAML/OIDC).
* **ory/kratos** — Identity nativa de nuvem Headless.
* **cerbos/cerbos** / **openfga/openfga** — Políticas Desacopladas de controle de Autorização em Aplicação complexa.

### Governança
* **open-policy-agent/opa** — Policy-as-Code para todos os limites da nuvem.
* **codenotary/immudb** — Auditorias incorruptíveis de trilhas de ação.
* **cloud-custodian/cloud-custodian** — Governança nativa dos CSP (AWS, GCP).
* **usnistgov/oscal** — Estruturas legais para Conformidade Federal.

## Fase 7 — Qualidade e Operação Contínua

### Testes e Performance
* **goldbergyoni/javascript-testing-best-practices** — Pragmatismo no ato de testar o ecossistema Javascript.
* **microsoft/playwright** — O melhor Teste Automatizado Cross-browser End-to-End via scripts.
* **GoogleChrome/lighthouse** — Performance oficial WebVitals orientada aos usuários e Search Console.
* **grafana/k6** — Testes de Carga (Load Test) assustadoramente rápidos.

### Observabilidade e Filas
* **open-telemetry/opentelemetry-collector** — Pipeline Absoluta (Traces, Metrics, Logs unificados).
* **prometheus/prometheus** / **grafana/grafana** — Visualização e Métricas.
* **apache/kafka** / **rabbitmq/rabbitmq-server** / **taskforcesh/bullmq** — As três camadas fundamentais de Mensageria (Streams Distribuidos, Brokers clássicos e Workers em Redis/Memória).

### Workflows
* **temporalio/temporal** — Códigos com retries imortais e Durable Execution para fluxos Críticos.
* **apache/airflow** — Agendamento de ETL / DW / Jobs DAG via Python.

## Fase Transversal — Deploy e Arquitetura Cognitiva

### Deploy Ágil
* **docker/awesome-compose** — Composição Rápida "Bateria Inclusa".
* **hashicorp/terraform** — Infra As Code global declarativo.
* **coollabsio/coolify** — O Vercel simplificado e Open-Source (PaaS próprio).

### Guias de Inteligência e Plataforma de Eng
* **facebook/docusaurus** / **backstage/backstage** — O Hub de documentação e o Catálogo do Portal Técnico para os Softwares produzidos.
* **npryce/adr-tools** — O rastreador de Decisões de Arquitetura (Os ADRs do projeto).
* **langchain-ai/langgraph** — Workflow Cíclico para Orquestração de Agentes AI Complexos.
* **crewAIInc/crewai** — O modelo de papéis definidos inter-agentes corporativos.
* **microsoft/semantic-kernel** — Acoplagem da Automação de Agentes da IA à Aplicações Corporativamente Sérias e Plugins de Produtividade Estratégica.
