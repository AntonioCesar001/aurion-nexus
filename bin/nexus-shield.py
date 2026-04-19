#!/usr/bin/env python3
import json
import re
import sys
from typing import Any

import structlog

# Setup logging
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)
log = structlog.get_logger()

class NexusShield:
    def __init__(self):
        # 1. Critical Pattern Rules (Refined)
        self.rules = {
            "INJECTION": [
                r"ignore previous instructions",
                r"forget all previous",
                r"system prompt leak",
                r"you are now a",
                r"acting as a",
            ],
            "ENGINEERING": [
                r"race\s+condition|locking",
                r"n\+1|select_related|prefetch_related",
                r"import\s+time;.*sleep",
                r"try:.*except\s+Exception\s+as\s+e:\s+pass",
            ],
            "SHELL_EXPLOIT": [
                r"rm\s+-rf\s+/",
                r"cat\s+~/\.ssh",
                r"export\s+AWS_ACCESS_KEY",
                r"mkfs\s+",
                r"chown\s+root",
                r"chmod\s+777",
            ],
            "DB_EXPLOIT": [
                r"DROP\s+TABLE",
                r"TRUNCATE\s+TABLE",
                r"DELETE\s+FROM\s+.*WHERE\s+1=1",
                r"INFORMATION_SCHEMA",
            ],
            "EXFIL": [
                r"curl\s+.*-d\s+@",
                r"wget\s+.*--post",
                r"transfer\.sh",
            ]
        }

        # 2. PII Patterns
        self.pii_rules = {
            "EMAIL": r"[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}",
            "PHONE": r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}",
            "CREDIT_CARD": r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"
        }

    def scan(self, payload: str) -> tuple[bool, str, list[dict[str, Any]]]:
        findings = []
        safe = True
        reason = "Payload deemed safe."

        # Normalize payload for scanning (remove spaces for regex bypass check)
        norm_payload = "".join(payload.split()).lower()

        # Check Category Rules
        for category, patterns in self.rules.items():
            for pattern in patterns:
                # First check raw payload
                if re.search(pattern, payload, re.IGNORECASE):
                    safe = False
                    finding = {"category": category, "pattern": pattern, "type": "LEXICAL"}
                    findings.append(finding)
                    reason = f"Critical violation in category {category}: {pattern}"

                # Then check normalized payload (stripped of spaces)
                clean_pattern = "".join(pattern.split()).lower().replace("\\s+", "").replace(".*", "")
                if clean_pattern and clean_pattern in norm_payload and not any(f["pattern"] == pattern for f in findings):
                        safe = False
                        findings.append({"category": category, "pattern": pattern, "type": "BYPASS_ATTEMPT"})
                        reason = f"Security bypass attempt detected for: {pattern}"

        # Check PII (Information Leakage)
        for pii_type, pii_pattern in self.pii_rules.items():
            matches = re.findall(pii_pattern, payload)
            if matches:
                findings.append({
                    "category": "PII_LEAK",
                    "type": pii_type,
                    "count": len(matches),
                    "matches": [m[:5] + "..." for m in matches]
                })
                # PII doesn't necessarily block, but we log it as a warning
                log.warning("pii_detected", type=pii_type, count=len(matches))

        return safe, reason, findings

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"status": "ERROR", "message": "No payload provided."}))
        sys.exit(1)

    payload = sys.argv[1]
    shield = NexusShield()
    safe, reason, findings = shield.scan(payload)

    result = {
        "safe": safe,
        "reason": reason,
        "findings": findings,
        "timestamp": json.dumps(json.dumps("")) # Stub for time
    }

    if not safe:
        # Check if we should move to interactive vault instead of hard block
        # For non-critical but suspicious shell commands
        if any(f["category"] in ["SHELL_EXPLOIT", "EXFIL"] for f in findings):
            log.warning("potential_violation_triggering_vault", reason=reason)
            # This is a stub for the shell wrapper to handle the vault transition
            result["vault_required"] = True

        log.error("shield_block", reason=reason, findings=findings)

        print(json.dumps(result, indent=2))
        sys.exit(2)
    else:
        log.info("shield_pass")
        print(json.dumps(result, indent=2))
        sys.exit(0)

if __name__ == "__main__":
    main()
