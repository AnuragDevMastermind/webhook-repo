# Use an official Python runtime as a parent image
FROM python:3.9

# Install python3-venv
RUN apt-get update && apt-get install -y python3-venv

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate virtual environment
RUN python3 -m venv venv 
RUN /bin/bash -c "source venv/bin/activate"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 9874

# Run the Flask application
CMD ["python3", "run.py"]
