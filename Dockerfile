# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app/Starterfile

# Copy the current directory contents into the container
COPY . /app/Starterfile

# Install any dependencies (if required)
RUN pip install -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "main.py"]
