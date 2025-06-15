# Building Stage
FROM python:3.11-slim AS build
WORKDIR /app

# Downloading dependencies
COPY requirements.txt .

# Insatlling dependencies
RUN pip install --upgrade pip && pip install  -r requirements.txt
COPY . .


# Main Stage
# Used Distroless Image for minimal image size 
FROM gcr.io/distroless/python3
WORKDIR /app

# Copy dependencies and application files from build stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app /app

# Set python dependencies path
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Opening port for application
EXPOSE 80

# Execution Command
CMD ["gandalf.py"]
