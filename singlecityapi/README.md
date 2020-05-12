# flask-docker
- `Flask`: Web app framework. You could take any other WSGI framework
- `Gunicorn`: Production grade App server for Python
- `Whitenoise`: Serving static files (js, css, images etc)
- `Docker`: Contenarize codebase + all of the above tech to ship


## Ship

In few steps, you can run on local, your cohort's local, AWS, Azure, anywhere.

Docker Container -> Container Registry -> Cloud

Make sure you set your ENV variable in the Docker file.

First build container:
* `docker build . -t flask-docker:latest`

Test local container:
* Run: `docker run -p 5000:5000 flask-docker:latest`
* Open: `http://localhost:5000`

If you want to deploy in the cloud:
* Tag it: `docker tag flask-docker:latest container_registry.com/flask-docker:latest`
* Push to remote container registry: `docker push container_registry.com/flask-docker:latest`
* Run in remote server: `docker run -d -p 50:5000 flask-docker:latest`

See `Dockerfile` ✨🍰✨
