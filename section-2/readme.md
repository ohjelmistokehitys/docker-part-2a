# Part 1 section 6: Utilizing tools from the Registry

The theory for the following exercises is presented at https://devopswithdocker.com/part-1/section-6.

To complete these exercises, you'll need to clone, fork or download sample projects from [https://github.com/docker-hy/material-applications](https://github.com/docker-hy/material-applications). You don't need to include the sample projects in your exercise repository when returning the exercises.

📣 Notice that all the information presented in the example projects are not needed in all the exercises. Don't just copypaste, but consider which commands are useful and where.

📣 **You don't need to install any of the tools or applications used by the sample projects locally.** All installations are supposed to happen in the containers during the build process.


## Exercise 1.11: Spring *(20 %)*

> Create a Dockerfile for an old Java Spring project that can be found from the [course repository](https://github.com/docker-hy/material-applications/tree/main/spring-example-project).
>
> The setup should be straightforward with the README instructions. Tips to get you started:
>
> Use [openjdk image](https://hub.docker.com/_/openjdk) `FROM openjdk:_tag_` to get Java instead of installing it manually. Pick the tag by using the README and Docker Hub page.
>
> You've completed the exercise when you see a 'Success' message in your browser.
>
> Submit the Dockerfile you used to build the container.
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-111-114

**Save your solution for this exercise in the file [spring.Dockerfile](./spring.Dockerfile).**

💡 The Dockerfiles in these exercises have custom names, so you will need to [specify which file to use when building the container images](https://docs.docker.com/engine/reference/commandline/image_build/#file). In this exercise, you'll need to use the file called [spring.Dockerfile](./server.Dockerfile), so your build command could be something like:

```sh
docker build . --file spring.Dockerfile --tag spring-example
```


## Exercises 1.12-1.14

> The following three exercises will start a larger project that we will configure in parts 2 and 3. They will require you to use everything you've learned up until now. If you need to modify a Dockerfile in some later exercises, feel free to do it on top of the Dockerfiles you create here.
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-111-114


## Exercise 1.12: Hello, frontend! *(20 %)*

> A good developer creates well-written READMEs. Such that they can be used to create Dockerfiles with ease.
>
> Clone, fork or download the project from
> [https://github.com/docker-hy/material-applications/tree/main/example-frontend](https://github.com/docker-hy/material-applications/tree/main/example-frontend).
>
> Create a Dockerfile for the project (example-frontend) and give a command so that the project runs in a Docker container with port 5000
> exposed and published so when you start the container and navigate to [http://localhost:5000](http://localhost:5000)
> you will see message if you're successful.
>
> * note that the port 5000 is reserved in the more recent OSX versions (Monterey, Big Sur), so you have to use some other host port
>
> _As in other exercises, do not alter the code of the project_
>
> * TIP: The project has install instructions in README.
>
> * TIP: Note that the app starts to accept connections when "Accepting connections at http://localhost:5000" has been printed to the screen, this takes a few seconds
>
> * TIP: You do not have to install anything new on your computer (instead, the installation should be done inside the containers).
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-111-114

**Save your solution for this exercise in the file [frontend.Dockerfile](./frontend.Dockerfile). Also, save the message you received in the browser in the file [ex-1-12.txt](./ex-1-12.txt).**

📣 **Note!** Based on the Haaga-Helia teacher's experience, the dependencies of the frontend project are very picky about the Node.js version and the environment in general. We strongly recommend using **node:16** base image in this exercise to prevent unnecessary compatibility issues (`FROM node:16`).


## Exercise 1.13: Hello, backend! *(20 %)*

> Clone, fork or download a project from
> [https://github.com/docker-hy/material-applications/tree/main/example-backend](https://github.com/docker-hy/material-applications/tree/main/example-backend).
>
> Create a Dockerfile for the project (example-backend). Start the container with port 8080 published.
>
> When you start the container and navigate to [http://localhost:8080/ping](http://localhost:8080/ping) you should get a "pong" as response.
>
> _Do not alter the code of the project_
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-111-114

**Save your solution for this exercise in the file [backend.Dockerfile](./backend.Dockerfile).**

💡 The backend in this exercise is written in [Go (golang)](https://go.dev/). **You won't need to learn Go or install any Go related tooling**. Instead, use an official [Go base image](https://hub.docker.com/_/golang) and **follow the instructions in the readme** to install and start the backend.


## Exercise 1.14: Environment *(20 %)*

> Start both frontend-example and backend-example with correct ports exposed and add ENV to Dockerfile with necessary information from both READMEs
> ([front](https://github.com/docker-hy/material-applications/tree/main/example-frontend), [back](https://github.com/docker-hy/material-applications/tree/main/example-backend)).
>
> Ignore the backend configurations until frontend sends requests to `_backend_url_/ping` when you press the button.
>
> You know that the configuration is ready when the button for 1.14 of frontend-example responds and turns green.
>
> _Do not alter the code of either project_
>
> Submit the edited Dockerfiles and commands used to run.
>
> ![Backend and Frontend](./back-and-front.png)
>
> The frontend will first talk to your browser. Then the code will be executed from your browser and that will send a message to backend.
>
> ![More information about connection between frontend and backend](./about-connection-front-back.png)
>
> * TIP: When configuring web applications keep browser developer console ALWAYS open, F12 or cmd+shift+I when the browser window is open. Information about configuring cross origin requests is in README of the backend project.
>
> * TIP: Developer console has multiple views, most important ones are Console and Network. Exploring the Network tab can give you a lot of information on where messages are being sent and what is received as response!
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-111-114

**To complete this exercise, you need to make changes in the [backend.Dockerfile](./backend.Dockerfile) and [frontend.Dockerfile](./frontend.Dockerfile) files. Also, save the response text you see when you successfully click the "press to test!" button in the frontend in the file [ex-1-14.txt](./ex-1-14.txt).**

💡 The challenge in this exercise is in enabling the frontend and the backend communicate with each other even when they are served from different origins, in this case different ports. "For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts." [(MDN web docs)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

> *"Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources"*
>
> [Cross-Origin Resource Sharing (CORS). MDN web docs.](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

You will need to configure the frontend to make connections to the backend using the correct address and port. The backend needs to expect connections from the correct frontend URL. Both applications can be configured to work together with environment variables and you do not need to make changes in their code.


💡 *In case things are not working as supposed, triple check the environment variables. If you are using the default ports, the frontend should be served from port 5000 and make connections to the backend at port 8080. Backend should be served from port 8080 and allow connections from `http://localhost:5000`. In CORS you cannot mix ip addresses and hostnames (`127.0.0.1` is not the same as `localhost`). Also, `http://localhost` is not the same as `http://localhost:5000`.*

-------------

## Extra exercises 1.15-1.16

The following exercises are extra and not a part of the Haaga-Helia course.


## Exercise 1.15: Homework

> Create Dockerfile for an application or any other dockerised project in any of your own repositories and publish it to Docker Hub. This can be any project, except the clones or forks of backend-example or frontend-example.
>
> For this exercise to be complete you have to provide the link to the project in Docker Hub, make sure you at least have a basic description and instructions for how to run the application in a [README](https://help.github.com/en/articles/about-readmes) that's available through your submission.
>
> https://devopswithdocker.com/part-1/section-6/#exercises-115-116

There are no automated tests for this extra exercise. You don't need to submit anything, but if you wish, you can add a new file with information about your Docker Hub experience.


## Exercise 1.16: Cloud deployment

> It is time to wrap up this part and run a containerized app in the cloud.
>
> You can take any web-app, eg. an example or exercise from this part, your own app, or even the course material (see [devopsdockeruh/coursepage](https://hub.docker.com/r/devopsdockeruh/coursepage)) and deploy it to some cloud provider.
>
> There are plenty of alternatives, and most provide a free tier. Here are some alternatives that are quite simple to use:
>
> - [fly.io](https://fly.io) (easy to use but needs a credit card even in the free tier)
> - [render.com](https://render.com) (bad documentation, you most likely need google)
> - [heroku.com](https://heroku.com) (has a free student plan through [GitHub Student Developer Pack](https://www.heroku.com/github-students))
>
> If you know a good cloud service for the purposes of this exercise, please tell us (yes, we know about Amazon AWS, Google Cloud and Azure already... ).
>
> Submit the Dockerfile, a brief description of what you did, and a link to the running app.
>
> Source: https://devopswithdocker.com/part-1/section-6/#exercises-115-116

There are no automated tests for this extra exercise. You don't need to submit anything, but if you wish, you can add a new file with information about your deployment experience.
