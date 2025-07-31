# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Node.js (required by Reflex)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose port 80 for web traffic
EXPOSE 80

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the Reflex application in frontend-only mode on port 80
CMD ["reflex", "run", "--env", "prod", "--frontend-only", "--frontend-host", "0.0.0.0", "--frontend-port", "80"]