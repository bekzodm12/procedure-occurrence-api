# Procedure Occurrence API

## Swagger Documentation

The endpoint description is available on OpenAPI (Swagger) via the following link:

https://app.swaggerhub.com/apis/MAKHMUDOVB/ProcedureOccurrenceAPI/1.0.0

## Deployment

The service is deployed using Docker. The Dockerfile is available in the repository to build image and run a Docker container.

```
docker build --tag flask-app .

docker run -d -p 5000:5000 flask-app
```

The app is run in a detached mode and can be accessed on a web browser using http://localhost:5000 base development URL.