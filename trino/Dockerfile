# Define ARG variables for the build
ARG TRINO_VERSION="475"

# Use the official Trino image as a base
FROM trinodb/trino:${TRINO_VERSION}

# Switch to root user to perform installation steps
USER root

# (Optional) Copy catalog property files if needed 
COPY catalog/ /etc/trino/catalog/
COPY plugin/ /usr/lib/trino/plugin/

# Switch back to the default trino user
USER trino:trino
