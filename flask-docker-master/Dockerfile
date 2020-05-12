FROM python:3.6
MAINTAINER Matthew Sessions "matthewlsessions@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]
