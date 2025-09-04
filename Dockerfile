# Base Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system deps for Playwright
RUN apt-get update && \
    apt-get install -y wget curl gnupg libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libgbm1 && \
    rm -rf /var/lib/apt/lists/*

# Install Playwright & Browsers
RUN pip install --no-cache-dir playwright apify-client
RUN playwright install chromium --with-deps
# Copy only requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your code last (so only code changes trigger rebuild)
COPY . .

# Command
CMD ["python", "main.py"]