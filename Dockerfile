FROM ghcr.io/apify/actor-python-playwright:3.11
COPY . ./
COPY requirements.txt ./
# Copy into the container


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Run
CMD ["python", "main.py"]