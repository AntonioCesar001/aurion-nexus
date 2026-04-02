#!/bin/bash
# 🌌 Antigravity Skill Installer
# Este script equipa o diretório atual com as skills do Aurion e da Aurora.

SOURCE_DIR="/home/shoxsx/code/openclaw Aurion"
AGENT_DIR="$PWD/.agent"
SKILLS_DIR="$AGENT_DIR/skills"

echo "🚀 Equipando projeto com Skills do Aurion e da Aurora..."

# 1. Criar diretórios
mkdir -p "$SKILLS_DIR/aurora" "$SKILLS_DIR/aurion"

# 2. Vincular Skills (Symlinks para manter atualizado)
echo "🔗 Vinculando skills operacionais (Aurora)..."
find "$SOURCE_DIR/projects/aurion-nexus/docs/aurora/skills" -mindepth 1 -maxdepth 1 -type d -exec ln -snf "{}" "$SKILLS_DIR/aurora/" \;

echo "🔗 Vinculando blueprints estratégicos (Aurion)..."
ln -snf "$SOURCE_DIR/projects/aurion-nexus/docs/standards/blueprints/"*.md "$SKILLS_DIR/aurion/"

# 3. Criar Router de Persona
echo "📡 Configurando roteador de persona..."
cat <<EOF > "$SKILLS_DIR/router.md"
# SKILL.md — Antigravity Persona Router
## Description
Define como Antigravity lida com os gatilhos Aurion: e Aurora:.
## Routing Rules
### Aurion (Estratégico)
Acknowledge com 🏛️. Prioriza .agent/skills/aurion/. Foco em "Por que" e estratégia.
### Aurora (Operacional)
Acknowledge com 🌌. Prioriza .agent/skills/aurora/. Foco em "Como" e execução.
EOF

# 4. Final Health Check
echo "Running initial health check..."
./bin/health-check.sh

# 5. Criar Manifest
echo "📄 Gerando manifesto de skills..."
cat <<EOF > "$AGENT_DIR/skills-manifest.md"
# Skills Manifest - Antigravity
## 🧭 Routing
- [router](file://$SKILLS_DIR/router.md)
## 🌌 Aurora (Operational)
- Localizado em .agent/skills/aurora/
## 🏛️ Aurion (Strategic)
- Localizado em .agent/skills/aurion/
EOF

# 5. Atualizar AGENTS.md se existir, ou criar novo
if [ ! -f "AGENTS.md" ]; then
    cp "$SOURCE_DIR/projects/aurion-nexus/docs/standards/AGENTS.md" .
    echo "📝 Criado AGENTS.md baseado no template oficial."
else
    if ! grep -q "Persona Protocols" "AGENTS.md"; then
        cat <<EOF >> "AGENTS.md"

### ⚡ Antigravity Integrated Skills
- **Manifest**: [.agent/skills-manifest.md](file://$AGENT_DIR/skills-manifest.md)
- **Aurora**: \`.agent/skills/aurora/\`
- **Aurion**: \`.agent/skills/aurion/\`

### 📡 Persona Protocols
- **Aurion:** (Estratégico)
- **Aurora:** (Operacional)
EOF
        echo "✅ AGENTS.md atualizado com protocolos de persona."
    fi
fi

# 6. Garantir TOOLS.md
if [ ! -f "TOOLS.md" ]; then
    cp "$SOURCE_DIR/projects/aurion-nexus/docs/standards/TOOLS.md" .
fi

echo "------------------------------------------------------------"
echo "✅ SUCESSO! O projeto está agora equipado com o Coletivo Supremo."
echo "💡 Use 'Aurion: ' para estratégia ou 'Aurora: ' para execução."
EOF
