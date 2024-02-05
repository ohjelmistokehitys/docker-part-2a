# Part 1 section 5: Interacting with the container via volumes and ports

The theory for the following exercises is presented at https://devopswithdocker.com/part-1/section-5.


## Exercise 1.9: Volumes *(10 %)*

> In this exercise we won't create a new Dockerfile.
>
> Image `devopsdockeruh/simple-web-service` creates a timestamp every two seconds to `/usr/src/app/text.log` when it's not given a command. Start the
> container with bind mount so that the logs are created into your filesystem.
>
> Submit the command you used to complete the exercise.
>
> **Hint:** read the note that was made just before this exercise!
>
> Source: https://devopswithdocker.com/part-1/section-5#exercise-19

**Save the command(s) you used to complete the exercise in the file [ex-1-09.txt](./ex-1-09.txt).**


## Exercise 1.10: Ports open *(10 %)*

> In this exercise, we won't create a new Dockerfile.
>
> The image `devopsdockeruh/simple-web-service` will start a web service in port `8080` when given the argument "server". In [Exercise 1.8](https://devopswithdocker.com/part-1/section-3#exercises-17---18) you already did a image that can be used to run the web service without any argument.
>
> Use now the -p flag to access the contents with your browser. The output to your browser should be something like:
> `{ message: "You connected to the following path: ...`
>
> Submit your used commands for this exercise.
>
> Source: https://devopswithdocker.com/part-1/section-5#exercise-110

**Save the command(s) you used to complete the exercise in the file [ex-1-10.txt](./ex-1-10.txt).**
