FROM apify/actor-python:3.11

COPY requirements.txt ./
# Copy into the container


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium --with-deps
COPY . ./

# Run
CMD python3 main.py