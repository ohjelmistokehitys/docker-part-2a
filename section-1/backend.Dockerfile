# This Dockerfile was implemented in exercises 1.13 and 1.14
FROM golang:latest

WORKDIR /app
COPY ./material-applications/example-backend /app

RUN go build
RUN go test ./...

ENV PORT=8080
EXPOSE 8080

ENV REQUEST_ORIGIN=http://localhost:5000

CMD [ "./server" ]
