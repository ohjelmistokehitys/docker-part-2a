# This Dockerfile was implemented in exercises 1.12 and 1.14
FROM node:16

WORKDIR /app
COPY ./material-applications/example-frontend /app

RUN npm install
RUN REACT_APP_BACKEND_URL=http://localhost:8080 npm run build

RUN npm install -g serve

EXPOSE 5000

CMD [ "serve", "-s", "-l", "5000", "build" ]
