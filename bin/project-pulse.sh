#!/bin/bash
# Aurion Nexus: Context Accelerator
# Generates PULSE.md for fast agent onboarding.

BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}💓 Generating Project Pulse...${NC}"

cat << EOF > PULSE.md
# 💓 PROJECT PULSE — $(date '+%Y-%m-%d %H:%M:%S')

## 🧭 Current Mission Status
$(grep -A 5 "##" CHRONICLE.md | head -n 10)

## ⚖️ Governance Snapshot
- **Soul**: High-Performance Intent-Based Autonomy.
- **Standard**: TDD, Security Gated, Impeccable Design.

## 🛠️ Active Skill Registry
$(grep "^- \*\*\[" .agent/skills-manifest.md | head -n 15)

## 🛡️ Critical Paths
- Secrets: /home/shoxsx/code/openclaw Aurion/secrets/
- Skills: /home/shoxsx/code/openclaw Aurion/.agent/skills/

---
*Pulse generated for immediate context injection.*
EOF

echo -e "${BLUE}PULSE.md created successfully.${NC}"
