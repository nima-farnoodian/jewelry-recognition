# Download Python from DockerHub
FROM python:3.8.3

# Set working directory in the Docker container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies from the requirements document
RUN pip install -r requirements.txt

# Copy the Flask app code to the working directory
COPY source/ .

# Expose ports
EXPOSE 5050

# Call application
CMD ["python3", "ai-api.py", "serve"]