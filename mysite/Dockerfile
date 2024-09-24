# Use an official Python runtime as a parent image
FROM python:3.11.5 as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Start a new stage and copy over the necessary files
FROM python:3.11.5 as production

WORKDIR /app

# Install Redis
RUN apt-get update && apt-get install -y redis-server

# Copy from builder
COPY --from=builder /app /app

# Install dependencies in the production image as well
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Create a shell script to start Redis and Gunicorn
RUN echo "#!/bin/bash" > start.sh
RUN echo "redis-server --daemonize yes" >> start.sh
RUN echo "exec gunicorn --bind :\$PORT --worker-class gevent mysite.wsgi:application" >> start.sh
RUN chmod +x start.sh

# Run the start script when the container launches
CMD ["./start.sh"]