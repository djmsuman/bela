# Use an official Python runtime as a parent image
FROM python:3.14-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files (if it exists)
COPY pyproject.toml poetry.lock* ./

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the Django application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
