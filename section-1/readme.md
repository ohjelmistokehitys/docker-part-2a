# Part 2 section 1: Migrating to Docker Compose

The theory for the following exercises is presented at https://devopswithdocker.com/part-2/section-1.



## Exercise 2.1 (20 %)

> Let us now leverage the Docker Compose with the simple webservice that we used in the [Exercise 1.3](https://devopswithdocker.com/part-1/section-2#exercise-13)
>
> Without a command `devopsdockeruh/simple-web-service` will create logs into its `/usr/src/app/text.log`.
>
> Create a docker-compose.yml file that starts `devopsdockeruh/simple-web-service` and saves the logs into your filesystem.
>
> Submit the docker-compose.yml, make sure that it works simply by running `docker compose up` if the log file exists.
>
> Source: https://devopswithdocker.com/part-2/section-1/#exercise-21

**Save the Docker compose configuration you write in this exercise in the file [docker-compose-logging.yml](./docker-compose-logging.yml).** Configure the compose file to write the output in the existing [`logs/text.log` file](./logs/text.log) in the local filesystem.

💡 *As the file in this exercise is named other than the default `docker-compose.yml`, you will need to specify in your command which file to use. You can do this by adding the `--file` attribute in your command:* `docker compose --file docker-compose-logging.yml up`


## Exercise 2.2 (20 %)

> Read about how to add command to docker-compose.yml from the [documentation](https://docs.docker.com/compose/compose-file/compose-file-v3/#command).
>
> The familiar image `devopsdockeruh/simple-web-service` can be used to start a web service.
>
> Create a Docker compose file and use it to start the service **so that you can use it with your browser**.
>
> Submit the Docker compose, make sure that it works simply by running `docker compose --file docker-compose-server.yml up`
>
> Source: https://devopswithdocker.com/part-2/section-1/#exercises-22---23

**Save the Docker compose configuration you write in this exercise in the file [docker-compose-server.yml](./docker-compose-server.yml).**

💡 *As the file in this exercise is named other than the default `docker-compose.yml`, you will need to specify in your command which file to use. You can do this by adding the `--file` attribute in your command:* `docker compose --file docker-compose-server.yml up`


## Exercise 2.3 (20 %)

> As we saw previously, starting an application with two programs was not trivial and the commands got a bit long.
>
> In the [previous part](https://devopswithdocker.com/part-1/section-6) we created Dockerfiles for both [frontend](https://github.com/docker-hy/material-applications/tree/main/example-frontend) and [backend](https://github.com/docker-hy/material-applications/tree/main/example-backend) of the example application. Next, simplify the usage into one docker-compose.yml.
>
> Configure the backend and frontend from [part 1](https://devopswithdocker.com/part-1/section-6#exercises-111-114) to work in Docker Compose.
>
> Submit the docker-compose.yml
>
> Source: https://devopswithdocker.com/part-2/section-1/#exercises-22---23

**Save the Docker compose configuration you write in this exercise in the file [docker-compose-frontend-and-backend.yml](./docker-compose-frontend-and-backend.yml).**

You will also need to update the contents of[ `frontend.Dockerfile`](./frontend.Dockerfile) and [`backend.Dockerfile`](./backend.Dockerfile) to match your solutions in the previous exercises.

💡 *As the file in this exercise is named other than the default `docker-compose.yml`, you will need to specify in your command which file to use. You can do this by adding the `--file` attribute in your command:* `docker compose --file docker-compose-frontend-and-backend.yml up`

