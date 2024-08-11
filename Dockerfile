# Use the official Qdrant image as the base
FROM qdrant/qdrant:latest

# Optional: Set environment variables
ENV QDRANT__SERVICE__GRPC_PORT=6334

# Expose necessary ports
EXPOSE 6333 6334

# Optional: Run additional commands or copy configuration files
# COPY custom_config.yaml /qdrant/config/custom_config.yaml

# Command to run Qdrant (this is already in the base image)
CMD ["qdrant"]

# docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
# http://localhost:6333/dashboard/

# docker run -d --name qdrant -p 6333:6333 -v /path/to/config.json:/qdrant/config/config.json qdrant/qdrant --config /qdrant/config/config.json
# docker run -d --name qdrant -p 6333:6333 -v /path/to/config.yaml:/qdrant/config/config.yaml qdrant/qdrant --config /qdrant/config/config.yaml