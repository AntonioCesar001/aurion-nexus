# 📖 Guia de Operação: OpenClaw vs PaperclipAI

Este guia ensina como você deve interagir com as duas forças que compõem o **Aurion Nexus**.

## 🏗️ 1. O Time AURION (OpenClaw)
**Função**: Refinamento Estratégico e Planejamento.
**O que você deve fazer aqui**:
1. Abro o arquivo `Aurion-Interface.md`.
2. Insira sua ideia bruta na seção `[INPUT]`.
3. O time **Aurion** (via OpenClaw) vai gerar um **Contrato de Execução**.
4. Você deve revisar e aprovar esse contrato.

> [!TIP]
> Use o time Aurion sempre que a ideia ainda não estiver clara ou precisar de validação técnica.

---

## 🚀 2. O Time AURORA (PaperclipAI)
**Função**: Execução Técnica e Construção.
**O que você deve fazer aqui**:
1. Acesse o dashboard do **PaperclipAI** em `http://localhost:3100`.
2. Transforme o "Contrato de Execução" aprovado em uma **Missão** dentro do Paperclip.
3. O squad **Aurora** (via Paperclip) começará a codar, testar e fazer o deploy.
4. Você monitora os custos e o progresso em tempo real pelo dashboard.

> [!IMPORTANT]
> O Paperclip gerencia o Aurora para que você não precise lidar com pull requests ou logs de erro técnicos.

---

## 🔄 Fluxo de Trabalho Integrado
1. **Você** dá a ideia -> **Aurion (OpenClaw)** planeja.
2. **Aurion** entrega o plano -> **Paperclip** recebe o comando.
3. **Paperclip** aciona **Aurora** -> **Aurora** constrói.
4. **Projeto entregue.**

---

## 🎨 3. Design-Driven Quality Gates (Impeccable)
Para garantir que o produto final seja **premium**, usamos o framework **Impeccable**:
1. **Auditoria**: Use `/audit` para verificar acessibilidade e performance.
2. **Crítica**: Use `/critique` para revisar a hierarquia visual e clareza.
3. **Polimento**: Use `/polish` antes de considerar a missão concluída.

> [!NOTE]
> Se o design parecer "gerado por IA" (AI Slop), ele deve ser refinado até parecer um trabalho de design profissional.

---

## 🛠️ Comandos Úteis
- **Design Audit**: `/audit [página]`
- **UX Critique**: `/critique [componente]`
- **Verificar Status do Paperclip**: `npx paperclipai dashboard`
- **Listar Agentes Aurora**: `npx paperclipai agent list`

