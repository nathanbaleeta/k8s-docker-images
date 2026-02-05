# Define ARG variables for the build
ARG TRINO_VERSION="479"

# Use production ready docker hardened images - https://hub.docker.com/hardened-images/catalog/dhi/trino
FROM dhi.io/trino:${TRINO_VERSION}

# Switch back to the default trino user. Use nonroot user as security best practice
USER trino:trino
