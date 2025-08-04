FROM python:3.11-slim

WORKDIR /app

# === ADD THIS BLOCK: Install OS dependencies for OpenCV ===
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first, using cache if requirements.txt is unchanged
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your code
COPY . .

# Use a default command; override in docker-compose if needed

