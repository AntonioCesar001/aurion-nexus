import os

import structlog
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.semconv.resource import ResourceAttributes

# Setup logging
log = structlog.get_logger()

def setup_tracing(service_name: str = "aurion-nexus"):
    """Initialize OpenTelemetry tracer with OTLP and Console exporters."""
    resource = Resource(attributes={
        ResourceAttributes.SERVICE_NAME: service_name,
        "environment": "production",
        "sovereign_status": "peak"
    })

    provider = TracerProvider(resource=resource)

    # Export to Console for local debug
    console_exporter = ConsoleSpanExporter()
    provider.add_span_processor(BatchSpanProcessor(console_exporter))

    # Export to OTLP if configured
    otlp_endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT")
    if otlp_endpoint:
        otlp_exporter = OTLPSpanExporter(endpoint=otlp_endpoint)
        provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
        log.info("tracing_otlp_enabled", endpoint=otlp_endpoint)

    trace.set_tracer_provider(provider)
    return trace.get_tracer(service_name)

def get_tracer():
    return trace.get_tracer("aurion-nexus")
