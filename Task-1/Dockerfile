# Use Ubuntu base image
FROM ubuntu:22.04

# Update and install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy all Python files and requirements
COPY requirements.txt .
COPY vulnerable_server.py .
COPY defended_server.py .
COPY attack_runner.py .
COPY jwt_demo.py .

# Install requirements (no external packages needed)
RUN pip3 install -r requirements.txt --break-system-packages || true

# Default command runs the attack demonstration
CMD ["python3", "attack_runner.py"]
