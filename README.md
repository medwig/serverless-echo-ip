# Serverless Echo IP

Creates a lambda-backed microservice API that accepts a GET request and returns the ip of the caller.

## Deploy

Deploy the service with the serverless framework

```
$ npm install -g serverless
$ sls deploy
```

## Use

Call the url listed in the output from `sls deploy`.

```
$ curl https://xxx.execute-api.us-east-2.amazonaws.com/dev/

{"message": "Go Serverless!", "caller_ip": "90.182.2.88"}
```
