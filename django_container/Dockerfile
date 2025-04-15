FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update && apt install -y python3-venv
RUN mkdir -p /var/app
RUN python3 -m venv /var/app/.env

WORKDIR /var/app
COPY requirements.txt .
ENV PATH="/var/app/.env/bin:$PATH"
RUN pip install -r requirements.txt
