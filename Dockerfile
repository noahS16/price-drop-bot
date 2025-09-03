FROM apify/actor-python:3.11

# Copy into the container
COPY . ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps

# Run
CMD ["python", "main.py"]