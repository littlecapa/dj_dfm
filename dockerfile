# Specify the base image
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app/dj_dfm

# Copy application files
COPY . /app/dj_dfm

# List all files in /app and /app/dj_dfm during the build process
RUN ls -la /app
RUN ls -la /app/dj_dfm

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the application
CMD ["python", "main.py"]
