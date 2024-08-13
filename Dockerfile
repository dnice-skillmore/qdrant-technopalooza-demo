# Use the official Qdrant image as the base
FROM qdrant/qdrant:latest

# Expose necessary ports
EXPOSE 6333 6334

# Optional: Run additional commands or copy configuration files
COPY /custom_config.yaml /qdrant/config

# Command to run Qdrant (this is already in the base image)
CMD ["./qdrant", "--config-path", "/qdrant/config/custom_config.yaml"]


###########################################
#     Build image with custom config      #
###########################################

# Build image
# docker build --tag 'qdrant' .

# Run image
# docker run -p 6333:6333 --name qdrant --detach 'qdrant'


###########################################
#     Build image with default config     #
###########################################

# docker run -d --name qdrant -p 6333:6333 qdrant/qdrant