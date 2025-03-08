FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5001 for the Flask app
EXPOSE 5001

# Define environment variable for Flask (optional)
ENV FLASK_APP=app.py

# Run the application
CMD ["python3", "app.py"]
