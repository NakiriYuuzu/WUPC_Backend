FROM python:3.10-slim-buster

# Set environment variables
ENV DB_HOST db

# Set the working directory
RUN mkdir /app
WORKDIR /app

# Dependencies
RUN apt-get update && apt-get install -y build-essential libmariadb-dev-compat

# Copy the requirements.txt file and install dependencies
COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache
#    && pip install gunicorn \ this is for ngix \

# Copy the rest of the application code
COPY . .

# Expose port 80
EXPOSE 80

# Make entrypoint.sh executable
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]