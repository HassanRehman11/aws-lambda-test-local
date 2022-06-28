FROM python:3.7-buster

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install awslambdaric && \
    pip3 install boto3 

RUN pip3 install requests

COPY app.py ./
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD ["app.handler"]