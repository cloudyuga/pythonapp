FROM python:2.7
RUN mkdir -p /app/program/output
WORKDIR /app
COPY . /app
ENTRYPOINT ["python"]
