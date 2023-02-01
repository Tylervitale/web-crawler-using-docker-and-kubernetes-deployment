# Use an existing image as the base image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy the current directory to the working directory
COPY . . 

# Install the required packages
RUN pip install -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "web-crawler.py"]

