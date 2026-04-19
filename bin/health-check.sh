#!/bin/bash
# Aurion Nexus: Health Engine
# Verifies the integrity of the sovereign core.

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$DIR")"
cd "$PROJECT_ROOT" || exit 1

echo -e "${BLUE}🌌 Starting Aurion Nexus Health Check...${NC}"

# 1. Check Secrets
echo -n "Checking secrets/ directory... "
if [ -d "secrets" ]; then
    ENV_COUNT=$(ls secrets/*.env 2>/dev/null | wc -l)
    if [ "$ENV_COUNT" -gt 0 ]; then
        echo -e "${GREEN}PASS (${ENV_COUNT} env files found)${NC}"
    else
        echo -e "${RED}FAIL (No .env files found in secrets/)${NC}"
    fi
else
    echo -e "${RED}FAIL (Directory secrets/ not found)${NC}"
fi

# 2. Check Core Skills
echo -n "Verifying Core Skills... "
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
fi

# 3. Check Skills Manifest
echo -n "Checking Skills Manifest... "
if [ -f ".agent/skills-manifest.md" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL (.agent/skills-manifest.md not found)${NC}"
fi

# 4. Check MCP Config (Placeholder for real connectivity check)
echo -n "Checking MCP Infrastructure... "
# In a real scenario, we would trigger an MCP tool to report status.
# For now, we verify the presence of the manifest entry.
grep -q "mcp-health" .agent/skills-manifest.md
if [ $? -eq 0 ]; then
    echo -e "${GREEN}READY (mcp-health registered)${NC}"
else
    echo -e "${RED}WARNING (mcp-health not registered)${NC}"
fi

echo -e "${BLUE}--- Health Check Complete ---${NC}"
