## Application Design and Build

### Overview

Topics:

- Images
- Jobs and CronJobs
- Multi-Container Pods
- Init containers
- Container Storage

### Building Container Images

- What is a container image
- Role of Docker and Dockerfile

#### What is a Container Image

An Image is a lightweight, standalone file that contains the software and executable needed to run a container.

A Dockerfile defines what is container in the image.

The `docker build` command builds an image using the Dockerfile.

#### Building the image

Run:

```bash
docker build -t my-website:0.0.1 .
```

The `-t` flag allows you to tag the image.

The `.` flag looks within the current directory.

Then run:

```bash
docker run --rm --name my-website -d -p 8080:80 my-website:0.0.1
```

The `-rm` flag deletes the container once it is stopped.

The `-name` flag gives it a name.

The `-d` flag runs it in detached mode.

The `-p 8080:80` flag exposes port 80 to port 8080.

You can test the container by running `curl localhost:8080`.

Then run `docker stop my-website` to stop the container.

#### Saving the image

Run:

```bash
docker save -o ./my-website:0.0.1.tar my-website:0.0.1
```

The `-o` flag sets the location.

### Running Jobs and Cronjobs

- What is a Job?
- What is a Cronjob?

#### What is a Job

Jobs are designed to run a containerised task successfully to completion.

#### What is a CronJob

Cronjobs run Jobs periodically according to a schedule.

#### Example job

This container below will run the code and stop.

The option `restartPolicy: Never` means it will never restart.

The option `backoffLimit: 4` means it will try a retry 4 times if it fails.

The option `activeDeadlineSeconds: 10` means kubernetes will only let it run for 10 seconds.

```YAML
apiVersion: batch/v1
kind: Job
metadata:
  name: my-job
spec:
  template:
    spec:
      containers:
      - name: print
      image: busybox:stable
      command: ["echo", "This is a test!"]
    restartPolicy: Never
  backoffLimit: 4
  activeDeadlineSeconds: 10
```

```bash

```

```bash

```

```bash

```

```bash

```
