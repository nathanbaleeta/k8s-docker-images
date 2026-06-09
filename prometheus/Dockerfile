# Define ARG variables for the build
ARG PROMETHEUS_VERSION="3.12.0-debian13"

# Use production ready docker hardened images - https://hub.docker.com/hardened-images/catalog/dhi/trino
FROM dhi.io/prometheus:${PROMETHEUS_VERSION}

# Switch back to the default trino user. Use nonroot user as security best practice
USER prometheus:prometheus
