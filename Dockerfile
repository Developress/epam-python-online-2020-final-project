FROM python:3.8-slim
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENV FLASK_CONFIG=production
RUN pip3 install -r requirements.txt && mkdir instance && echo "import os\nSECRET_KEY = os.getenv('SECRET_KEY')\nSQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')" > instance/config.py
EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["run.py"]