# Part 2 section 2: Docker networking

The theory for the following exercises is presented at https://devopswithdocker.com/part-2/section-2.


**Avoid copying and pasting**

In these exercises you need to use the same containers and images used in the previous exercises. You *could* just copy the Dockerfiles and example applications here, but there are also better options.

If you want, you can reference the existing Dockerfiles in [section-1](../section-1/) folder with a relative path (`../section-1`) from this folder:

```
...
  frontend:
    build:
      context: ../section-1/
      dockerfile: frontend.Dockerfile
...
```

Alternatively, you can use the images that have already been built locally instead of building new ones. As you remember from part 1, you can list your local images with `docker images`:

```
$ docker images
REPOSITORY           TAG      IMAGE ID       SIZE
section-1-frontend   latest   3ec8181f97e0   1.27GB
section-1-backend    latest   421cf3f71507   1.06GB
```

If your frontend was built in the previous exercise with the name `section-1-frontend`, your Docker compose file for the next exercise might have something like this:

```
...
  frontend:
    image: section-1-frontend
...
```

> **Security reminder: Plan your infrastructure and keep to your plan**
>
> In the next exercise, and in some later exercises, I will supply you with an illustration of the infrastructure. Do look at it and use it to write the configuration.
>
> For example, in Exercise 2.4 we don't want to open ports to Redis to the outside world. Do not add a `ports` configuration under Redis! The backend will be able to access the application within the Docker network.
>
> Source: https://devopswithdocker.com/part-2/section-2/


## Exercise 2.4 (10 + 10 %)

> In this exercise you should expand the configuration done in [Exercise 2.3](https://devopswithdocker.com/part-2/section-1#exercises-22---23) and set up the example backend to use the key-value database [Redis](https://redis.com/).
>
> Redis is quite often used as a [cache](https://en.wikipedia.org/wiki/Cache_(computing)) to store data so that future requests for data can be served faster.
>
> The backend uses a slow API to fetch some information. You can test the slow API by requesting `/ping?redis=true` with curl<sup>1</sup>. The frontend app has a button to test this.
>
> So you should improve the performance of the app and configure a Redis container to cache information for the backend. The
> [documentation](https://hub.docker.com/_/redis/) of the Redis image might contain some useful info.
>
> The backend [README](https://github.com/docker-hy/material-applications/tree/main/example-backend) should have all the information that is needed for configuring the backend.
>
> When you've correctly configured the button will turn green.
>
> Submit the docker-compose.yml
>
> ![Backend, frontend and redis](./back-front-and-redis.png)
>
> The [restart: unless-stopped](https://docs.docker.com/compose/compose-file/compose-file-v3/#restart) configuration can help if the Redis takes a while to get ready.
>
> Source: https://devopswithdocker.com/part-2/section-2/#exercise-24
>
> <sup>1</sup> *or by visiting http://localhost:8080/ping?redis=true in your browser*

**Save the Docker compose configuration you write in this exercise in the file [docker-compose-with-redis.yml](./docker-compose-with-redis.yml). Also, copy the message you see in your browser after pressing the "press to test" button successfully in file [ex-2-04.txt](./ex-2-04.txt).**

💡 *If you are stuck, start by adding a [Redis](https://hub.docker.com/_/redis/) service in your Docker compose file. Then, see how you can configure the backend to utilize the Redis container by using an environment variable.*

💡 *As the file in this exercise is named other than the default docker-compose.yml, you will need to specify in your command which file to use. You can do this by adding the `--file` attribute in your command:* `docker compose --file docker-compose-with-redis.yml up`


## Exercise 2.5 (20 %)

> The project [https://github.com/docker-hy/material-applications/tree/main/scaling-exercise](https://github.com/docker-hy/material-applications/tree/main/scaling-exercise) is a barely working application. Go ahead and clone it for yourself (or read note below\*). The project already includes docker-compose.yml so you can start it by running `docker compose up`.
>
> Application should be accessible through [http://localhost:3000](http://localhost:3000). However it doesn't work well enough and I've added a load balancer for scaling. Your task is to scale the `compute` containers so that the button in the application turns green.
>
> This exercise was created with [Sasu Mäkinen](https://github.com/sasumaki)
>
> Source: https://devopswithdocker.com/part-2/section-2/#exercises-25

\* Note that you do not actually need to clone the source code for this exercise. The [scaling-exercise-calculator](https://hub.docker.com/r/devopsdockeruh/scaling-exercise-calculator) and [scaling-exercise-compute](https://hub.docker.com/r/devopsdockeruh/scaling-exercise-compute) as well as the [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy) images have been published in [Docker hub](https://hub.docker.com). We have also added the Docker compose file from that repository here: [docker-compose-scaling.yml](./docker-compose-scaling.yml).

**📝 Additional info about this exercise**

Think about the *calculator* as the frontend and the *compute* as the backend. Unlike the previous examples we've had, now the backend does not have any published ports. Instead, all requests to the backend should come through the *load-balancer* container. You can see the set-up in the [docker-compose-scaling.yml](./docker-compose-scaling.yml) file.

Try starting the services defined in that file with the following command:

```
docker compose --file docker-compose-scaling.yml up
```

When the services are running, the backend should be listening to http://compute.localtest.me or just simply http://localhost. If the backend is working, it should respond with a simple "hello world". Open the frontend in your browser at http://localhost:3000. When you press the green button, you will see the application making slow progress in computation. You will also see logging entries in the console where you started the containers.

The compute service (i.e. backend) has been made slow on purpose. Your task in this exercise is to start the Docker containers so that the `compute` service has multiple containers and the *load-balancer* distributes the requests between them. When you are successful, you will notice the progress bar filling faster in the UI, and also the logging entries from the Docker containers will appear more frequently.

You **should not** need to make any changes in the containers nor the Docker compose file. Instead, you will need to change the command that is used for starting the containers:

```
docker compose --file docker-compose-scaling.yml up  # TODO
```

**Save the commands used in this exercise in the file [ex-2-05.txt](./ex-2-05.txt).**
