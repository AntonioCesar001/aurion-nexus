#!/bin/bash
# 🌌 Aurion Nexus Skill Installer
# Este script equipa o diretório atual com as skills do Aurion e da Aurora.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AURION_ROOT="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(pwd -P)"
AGENT_DIR="$PROJECT_ROOT/.agent"
SKILLS_DIR="$AGENT_DIR/skills"
AURORA_SOURCE_DIR="$AURION_ROOT/.agent/skills/aurora"
AURION_SOURCE_DIR="$AURION_ROOT/.agent/skills/aurion"
CLAUDE_SOURCE="$AURION_ROOT/CLAUDE.md"

    if [ "$src" = "$dest" ]; then
        echo "↷ Pulando self-link: $dest"
        return 0
    fi

    # Use relative symlink if possible
    local rel_src
    rel_src=$(python3 -c "import os; print(os.path.relpath('$src', '$(dirname "$dest")'))")
    ln -snf "$rel_src" "$dest"
}


link_aurora_skills() {
    local skill_dir

    echo "🔗 Vinculando skills operacionais (Aurora)..."
    shopt -s nullglob
    for skill_dir in "$AURORA_SOURCE_DIR"/*; do
        [ -d "$skill_dir" ] || continue
        safe_link "$skill_dir" "$SKILLS_DIR/aurora/$(basename "$skill_dir")"
    done
    shopt -u nullglob
}

link_aurion_skills() {
    local skill_file
    local linked_any=0

    echo "🔗 Vinculando blueprints estratégicos (Aurion)..."
    shopt -s nullglob
    for skill_file in "$AURION_SOURCE_DIR"/*.md; do
        # Improved legibility check
        if head -n 1 "$skill_file" | grep -q "^#"; then
             safe_link "$skill_file" "$SKILLS_DIR/aurion/$(basename "$skill_file")"
             linked_any=1
        else
            echo "⚠️  Ignorando fonte estratégica possivelmente inválida: $(basename "$skill_file")"
        fi
    done
    shopt -u nullglob

    if [ "$linked_any" -eq 0 ]; then
        echo "⚠️  Nenhuma skill estratégica legível foi vinculada."
    fi
}


generate_router() {
    echo "📡 Configurando roteador de persona..."
    cat <<EOF > "$SKILLS_DIR/router.md"
# SKILL.md — Antigravity Persona Router

## Description
This script defines how the high-performance agent collective handles system triggers.

## Routing Rules

### 🏛️ Aurion (Strategic)
- **Triggers**: "Aurion:", "Strategy:", "ADR:", "Review:"
- **Protocol**: Socratic Deep Interview.
- **Goal**: Minimize ambiguity, define architecture, and assess maturity using SEIP v2.
- **Skills**: \`.agent/skills/aurion/\`

### 🌌 Aurora (Operational)
- **Triggers**: "Aurora:", "Implement:", "Fix:", "Refactor:", "TDD:"
- **Protocol**: Ralph Loop (Plan → Execute → Verify → Fix).
- **Goal**: Deliver impeccable, production-ready code with 80%+ coverage.
- **Skills**: \`.agent/skills/aurora/\`

## Collaboration Contract
When in doubt, Aurion defines the "What" and "Why", while Aurora defines the "How".
EOF
}


generate_manifest() {
    local skill_dir
    local skill_file

    echo "📄 Gerando manifesto de skills..."
    cat <<EOF > "$AGENT_DIR/skills-manifest.md"
# Skills Manifest - Antigravity
## 🧭 Routing
- [router](file://$SKILLS_DIR/router.md)
## 🌌 Aurora (Operational)
EOF

    shopt -s nullglob
    for skill_dir in "$SKILLS_DIR/aurora"/*; do
        [ -f "$skill_dir/SKILL.md" ] || continue
        printf -- "- **[%s]**(file://%s/SKILL.md)\n" "$(basename "$skill_dir")" "$skill_dir" >> "$AGENT_DIR/skills-manifest.md"
    done
    shopt -u nullglob

    cat <<EOF >> "$AGENT_DIR/skills-manifest.md"
## 🏛️ Aurion (Strategic)
EOF

    shopt -s nullglob
    for skill_file in "$SKILLS_DIR/aurion"/*.md; do
        [ -f "$skill_file" ] || continue
        printf -- "- **[%s]**(file://%s)\n" "$(basename "$skill_file" .md)" "$skill_file" >> "$AGENT_DIR/skills-manifest.md"
    done
    shopt -u nullglob
}

echo "🚀 Equipando projeto com Skills do Aurion e da Aurora..."

mkdir -p "$SKILLS_DIR/aurora" "$SKILLS_DIR/aurion"

link_aurora_skills
link_aurion_skills

if [ -f "$CLAUDE_SOURCE" ]; then
    echo "🔗 Vinculando instruções principais (CLAUDE.md)..."
    safe_link "$CLAUDE_SOURCE" "$PROJECT_ROOT/CLAUDE.md"
fi

generate_router
generate_manifest

echo "Running initial health check..."
"$AURION_ROOT/bin/health-check.sh"

if [ -f "$PROJECT_ROOT/AGENTS.md" ]; then
    if ! grep -q "Persona Protocols" "$PROJECT_ROOT/AGENTS.md"; then
        cat <<EOF >> "$PROJECT_ROOT/AGENTS.md"

### ⚡ Aurion Integrated Skills
- **Manifest**: [.agent/skills-manifest.md](.agent/skills-manifest.md)
- **Aurora**: \`.agent/skills/aurora/\`
- **Aurion**: \`.agent/skills/aurion/\`

### 📡 Persona Protocols
- **Aurion:** (Strategic Architectural Command)
- **Aurora:** (Precision Operational Squad)
EOF
        echo "✅ AGENTS.md atualizado com protocolos de persona."
    fi
fi


if [ ! -f "$PROJECT_ROOT/RULES.md" ]; then
    safe_link "$AURION_ROOT/RULES.md" "$PROJECT_ROOT/RULES.md"
fi

if [ ! -f "$PROJECT_ROOT/SOUL.md" ]; then
    safe_link "$AURION_ROOT/SOUL.md" "$PROJECT_ROOT/SOUL.md"
fi

echo "------------------------------------------------------------"
echo "✅ SUCESSO! O projeto está agora equipado com o Coletivo Supremo."
echo "💡 Use 'Aurion: ' para estratégia ou 'Aurora: ' para execução."
echo "💡 Para Claude Code e Codex, as instruções foram linkadas."
echo "------------------------------------------------------------"
