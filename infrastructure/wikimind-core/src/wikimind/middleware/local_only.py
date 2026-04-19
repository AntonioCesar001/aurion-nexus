"""Middleware to restrict API access to localhost only.

Prevents remote network entities from interacting with the WikiMind gateway
unless explicitly allowed via the WIKIMIND_ALLOW_REMOTE environment variable.
"""

import os
import structlog
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

log = structlog.get_logger()

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1"}

class LocalOnlyMiddleware(BaseHTTPMiddleware):
    """Enforce localhost-only access for security hardening."""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Verify client IP and block non-local requests."""
        allow_remote = os.environ.get("WIKIMIND_ALLOW_REMOTE", "false").lower() == "true"
        
        if allow_remote:
            return await call_next(request)

        client_host = request.client.host if request.client else "unknown"
        
        if client_host not in ALLOWED_HOSTS:
            log.warning("THREAT DETECTED: Blocked remote access attempt",
                        client_host=client_host,
                        path=request.url.path)
            
            return JSONResponse(
                status_code=403,
                content={
                    "error": {
                        "code": "REMOTE_ACCESS_FORBIDDEN",
                        "message": "Security Policy: Gateway is restricted to Localhost. Use WIKIMIND_ALLOW_REMOTE=true if intended.",
                    }
                },
            )

        return await call_next(request)
