# Use Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the project files
COPY . .

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
