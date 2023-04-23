# Use the official Python image as base
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port
EXPOSE 5000

# Start the application
CMD ["flask", "run", "--host=0.0.0.0"]
