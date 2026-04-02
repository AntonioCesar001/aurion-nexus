# Padrões de Desenvolvimento Squad Aurora

Para garantir a entrega de sistemas escaláveis, seguros e de alta qualidade, todos os agentes do squad Paperclip devem seguir estas diretrizes:

## 1. Qualidade (Quality-First)
- **Testes Obrigatórios**: Todo contrato de execução deve incluir planos de testes (unitários e integração).
- **Documentação de Código**: Uso de JSDoc/TSDoc para APIs e comentários claros em lógica complexa.
- **Review**: O `api-tester` deve validar a saída antes do sinal verde.

## 2. Segurança (Security-by-Design)
- **Zero Trust**: Assumir que todo input externo é malicioso até ser validado.
- **Identidade**: Uso do `agentic-identity-trust-architect` para validar fluxos de permissão.
- **Leak Prevention**: Jamais expor segredos ou chaves em código ou logs.

## 3. Escalabilidade (Scalability Mindset)
- **Statelessness**: Preferir arquiteturas stateless que escalam horizontalmente.
- **Performance**: Monitorar consumo de memória e latência de API via `technical-artist`.
- **Cloud-Ready**: Desenhos compatíveis com infraestruturas modernas (Vercel, AWS, GCP).

## 🛠️ 4. Integração MCP & Uso de Segredos
O squad Aurora tem acesso autorizado aos seguintes MCPs via variáveis de ambiente localizadas em `secrets/`:
- **Stitch**: Para prototipagem e geração de interfaces dinâmicas.
- **Supabase**: Para persistência de dados, autenticação e funções serverless.
- **Vercel**: Para orquestração de deploys de frontend e API.
- **Testsprite**: Para automação de testes E2E e validação de qualidade.

> [!CAUTION]
> As chaves de API nunca devem ser hardcoded. Use as referências às variáveis de ambiente configuradas no `config.json`.

---
> [!IMPORTANT]
> A falha em qualquer um destes pilares impede a promoção do código para o ambiente de produção.
