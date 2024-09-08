FROM python:3.12.5-alpine3.19

WORKDIR /ComplaintGenerator

# Copy the current directory contents into the container at /app
COPY . /ComplaintGenerator

# Copy the templates folder
COPY ./templates /ComplaintGenerator/templates
COPY ./static /ComplaintGenerator/static

# Install any dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main.py

# Run flask app
CMD ["flask", "run", "--host=0.0.0.0"]

