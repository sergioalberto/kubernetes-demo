# Inherit from the Python Docker image
FROM python:3.7-slim

# Change the working directory
WORKDIR /app/

# Copy the source code to app folder
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Set "python" as the entry point
ENTRYPOINT ["python3"]

# Set the command as the script name
CMD ["app.py"]
