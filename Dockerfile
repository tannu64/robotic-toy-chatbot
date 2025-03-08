# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY src/ ./src/
COPY config/ ./config/
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports if necessary (e.g., for APIs or logs)
EXPOSE 5000

# Set environment variables (optional)
ENV CONFIG_PATH=config/dev_config.yaml

# Command to run the application
CMD ["python", "src/main.py", "config/dev_config.yaml"]
