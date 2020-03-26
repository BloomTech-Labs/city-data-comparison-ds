FROM python:3.6
MAINTAINER Matthew Sessions "matthewlsessions@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV ACCESS_KEY=jkekal6d6e5si3i2ld66d4dl
ENV MONGO_URI=mongodb+srv://SingleCity:oS8yLMDT3iKodnlx@singlecity-ldwwd.mongodb.net/test?retryWrites=true&w=majority
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]
