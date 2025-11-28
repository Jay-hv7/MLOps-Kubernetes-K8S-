# Use Python 3.7 because PyCaret 1.0.0 requires it
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Install system dependencies (required for some PyCaret models)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
ENV PORT 8080

# Run the application
CMD ["gunicorn", "app:app", "--config=config.py"]
