FROM python:3.10.4-slim-bullseye

# Set Environment varibales
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /docking
WORKDIR /docking
ADD . /docking


# Install dependencies
# COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Copy Project
# COPY . .