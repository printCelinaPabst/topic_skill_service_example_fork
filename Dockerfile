FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PORT=5000
# Container mit eigener Verzeichnisstruktur
WORKDIR /app

#Abhängigkeiten kopieren in eine neue Datei die im Image ist
COPY requirements.txt requirements.txt

#Befehl um die requiremnets ause requirements.txt zu installieren
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

#Befehl, Container wird Anfrage auf bestimmten Port erwarten
EXPOSE 5000

#damit die Anwendung läuft und Anfragen akzeptiert und bearbeitet werden können
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]
