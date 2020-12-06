FROM python:3.8-slim
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
ENV FLASK_CONFIG=production
RUN pip3 install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python3"]
CMD ["run.py"]