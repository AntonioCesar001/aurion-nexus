#!/bin/bash
# Hook triggered before an agent is dispatched or starts execution.

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$DIR")")"
SHIELD_BIN="$PROJECT_ROOT/bin/nexus-shield"

PAYLOAD=$1

if [ -f "$SHIELD_BIN" ]; then
    "$SHIELD_BIN" "$PAYLOAD"
    STATUS=$?
    if [ $STATUS -ne 0 ]; then
        echo "Pre-execution hook failed. Agent dispatched blocked."
        exit $STATUS
    fi
else
    echo "Warning: nexus-shield not found. Pre-execution scan skipped."
fi
exit 0
