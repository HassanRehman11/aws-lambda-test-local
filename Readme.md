# Local test of AWS Lambda function via ECR

Follow the documentation for installing the aws-lambda-rie <br/>
https://docs.aws.amazon.com/lambda/latest/dg/images-test.html

## Building docker file
sudo docker build . -t test_aws

## Running docker image
sudo docker run -v ~/.aws-lambda-rie:/aws-lambda -p 9700:8080 --entrypoint aws-lambda/aws-lambda-rie test_aws /usr/local/bin/python -m awslambdaric app.handler

## Test Lambda Function
curl -XPOST http://localhost:9700/2015-03-31/functions/function/invocations -d '{"task":"list_zodiac"}' <br/>
curl -XPOST http://localhost:9700/2015-03-31/functions/function/invocations -d '{"task":"get_horoscope","sign":"virgo","day":"tomorrow"}'
