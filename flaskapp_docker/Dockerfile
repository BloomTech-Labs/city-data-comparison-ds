FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ACCESS_KEY=
ENV MONGO_URI=
ENV SQLALCHEMY_DATABASE_URI=
EXPOSE 5000
CMD ["python", "application.py"]