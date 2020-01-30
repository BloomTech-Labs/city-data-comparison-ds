FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ACCESS_KEY=jkekal6d6e5si3i2ld66d4dl
ENV MONGO_URI=mongodb+srv://admin:rNuKKxAX3UL59FIt@cluster0-xt3at.mongodb.net/citydata?retryWrites=true&w=majority
ENV SQLALCHEMY_DATABASE_URI=postgresql://postgres:lkjhgfdsa@dsapi.co7exmpaol7l.us-east-2.rds.amazonaws.com/dscitydata
EXPOSE 5000
CMD ["python", "application.py"]