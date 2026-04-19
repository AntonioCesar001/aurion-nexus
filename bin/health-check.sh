#!/bin/bash
# Aurion Nexus: Health Engine
# Verifies the integrity of the sovereign core.

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$DIR")"
cd "$PROJECT_ROOT" || exit 1

ERRORS=0

echo -e "${BLUE}🌌 Starting Aurion Nexus Health Check...${NC}"

# 1. Check Governance Files
echo -n "Checking governance files... "
REQUIRED_FILES=("SOUL.md" "RULES.md" "CHRONICLE.md" "CLAUDE.md")
MISSING=0
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo -n -e "${RED}[Missing: $file] ${NC}"

        MISSING=$((MISSING+1))
    fi
done
if [ "$MISSING" -eq 0 ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo ""
    ERRORS=$((ERRORS+MISSING))
fi

# 2. Check Skills Manifest
echo -n "Checking skills manifest... "
if [ -f ".agent/skills-manifest.md" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL (.agent/skills-manifest.md not found)${NC}"
    ERRORS=$((ERRORS+1))
fi

# 3. Check Knowledge Catalogs
echo -n "Checking knowledge catalogs... "
CATALOG_COUNT=$(ls .agent/knowledge/*.md 2>/dev/null | wc -l | tr -d ' ')
if [ "$CATALOG_COUNT" -gt 0 ]; then
    echo -e "${GREEN}PASS (${CATALOG_COUNT} catalogs loaded)${NC}"
else
    echo -e "${RED}FAIL (no catalogs in .agent/knowledge/)${NC}"
    ERRORS=$((ERRORS+1))
fi

# 4. Check Hooks
echo -n "Checking agent hooks... "
HOOK_COUNT=$(ls .agent/hooks/*.sh 2>/dev/null | wc -l | tr -d ' ')
if [ "$HOOK_COUNT" -gt 0 ]; then
    echo -e "${GREEN}PASS (${HOOK_COUNT} hooks registered)${NC}"
else
    echo -e "${RED}WARNING (no hooks in .agent/hooks/)${NC}"
fi

# 6. Check WikiMind connectivity
echo -n "Checking WikiMind connectivity... "
if curl -fsS http://127.0.0.1:7842/health >/dev/null 2>&1; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${YELLOW}WARNING (WikiMind Core not reachable on 7842)${NC}"
fi

# 7. Check Environment
echo -n "Checking Python version... "
PYTHON_VER=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${CYAN}${PYTHON_VER}${NC}"

echo -e "${BLUE}--- Health Check Complete (${ERRORS} issues) ---${NC}"

exit $ERRORS
