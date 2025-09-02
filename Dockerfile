FROM python:3.14-rc-slim

# Container mit eigener Verzeichnisstruktur
WORKDIR /app

#Abhängigkeiten kopieren in eine neue Datei die im Image ist
COPY requirements.txt requirements.txt

#Befehl um die requiremnets ause requirements.txt zu installieren
RUN pip install -r requirements.txt

COPY . .

#Befehl, Container wird Anfrage auf bestimmten Port erwarten
EXPOSE 5000

#damit die Anwendung läuft und Anfragen akzeptiert und bearbeitet werden können
CMD [ "flask", "run", "--host", "0.0.0.0"]
