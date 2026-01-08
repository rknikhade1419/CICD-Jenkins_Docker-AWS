# Use an official Python runtime as a base image
FROM python:3.9-slim
# Set working directory in container
WORKDIR /app
# Copy requirements file
COPY requirement.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code
COPY app.py .
# Expose port
EXPOSE 5000
# Set environment variable
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
