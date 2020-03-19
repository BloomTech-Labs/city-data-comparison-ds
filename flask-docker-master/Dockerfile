FROM python:3.6
MAINTAINER Matthew Sessions "matthewlsessions@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ACCESS_KEY=jkekal6d6e5si3i2ld66d4dl
ENV MONGO_URI=mongodb+srv://citrus_user:sM9MrUjDKMzbzYVs@cluster0-ak1hs.mongodb.net/test?retryWrites=true&w=majority
ENV MONGO_UR2=mongodb+srv://SingleCity:oS8yLMDT3iKodnlx@singlecity-ldwwd.mongodb.net/test?retryWrites=true&w=majority
ENV SQLALCHEMY_DATABASE_URI=postgresql://postgres:lkjhgfdsa@dsapi.co7exmpaol7l.us-east-2.rds.amazonaws.com/dscitydata
ENV DYNAMO=arn:aws:dynamodb:us-east-2:595494748733:table/sc_data
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]
