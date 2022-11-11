Docker

Why?
    1. Reproducible
    2. Portable
    3. Standard
    4. Version-Controlled
    5. Single Responsibility Principle


Terms:
    Image           The blueprint
    Container       An instance of an image
    Docker-file     Image recipe
    Commit          Version controlled
    DockerHub       Public image repo (hub.docker.com)
    Layer           Mod to an existing image
                    Each Instruction row is a layer
                    (RUN/COPY and ADD create permanent layers -
                     other commands add temp layers and dont increase build size)
    Container Layer The writable layer that is created when making a container


Example Dockerfile*:
    ## Base Image: ref https://hub.docker.com/_/ubuntu/
    FROM ubuntu:16.04                   # use official and small as possible images

    ## Host Access
    EXPOSE 7745                         # Signpost to reader what ports are needed
                                        # By default, EXPOSE assumes TCP.
                                        # You can also specify UDP: EXPOSE 80/udp

    ## Meta-data
    LABEL author="Gilad Amar" \
          version="1.0.0"

    ## User permissions                 # Use least permissions neccesary - avoid sudo
    RUN addgroup -S new_group &&\
        adduser -S new_user -G new_group
    USER new_user

    ## File System
    WORKDIR /home
    VOLUME /home                        # Where to mount host dir
                                        # (specified by docker run)
    COPY host_fpath docker_fpath        # Add files from host to image
                                        # ADD [--chown=user:group] <src>... <dest> -  to change permissions
                                        # Use COPY rather than ADD for explicit file-copy
                                        # ADD can do tar extration and has url support (rather user wget or curl)

    ## Environment variables
    ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \   # Wrap lines with \
        HOME=/home \
        SHELL=/bin/bash \
        PATH /usr/local/nginx/bin:$PATH
        PYTHONUNBUFFERED 1              # Dont buffer output but push to console output
        PYTHONDONTWRITEBYTECODE 1       # Don't write out pyc files

    ## Setup
    RUN pip install numpy               # Run when building container
                                        # Combine RUN apt update, install and del apt cache for best performance
                                        # RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
                                        # It's a good idea to specify system package versions when doing this
    

    ## Execute
    CMD ["executable", "param1", "param2"]

* host dir cannot be supplied in image file, only on execution
* Port exposing is done on execution
* Only one CMD line allowed
* Docker auto shuts down if there is nothing to do,
  so CMD ["/bin/bash"] is often used to keep it open
* use "" not ''
* Escape \ as \\ (esp. for Windows fpaths)
* For Jupyter Notebook:
    CMD jupyter notebook --no-browser --allow-root --port=7745 --NotebookApp.token='tutorial'
* a .dockerignore file (similar to .gitignore) tells which files not to copy across
* place more frequently changed files , eg source code, as the lowest layers so cache can be maximally used e.g.
  Install rarely updated requirements before copying across code files
    ...
    COPY requirements.txt .
    RUN pip install -r requirements.txt # install dependencies
    COPY src/ .
    CMD [ "python", "./server.py" ]

Multi-stage builds (security and image size) - good for deployment
    # first stage
    FROM python:3.8 AS builder
    COPY requirements.txt .

    # install dependencies to the local user directory (eg. /root/.local)
    RUN pip install --user -r requirements.txt

    # second unnamed stage
    FROM python:3.8-slim
    WORKDIR /code

    # copy only the dependencies installation from the 1st stage image
    COPY --from=builder /root/.local/bin /root/.local
    COPY ./src .

    # update PATH environment variable
    ENV PATH=/root/.local:$PATH

    CMD [ "python", "./server.py" ]


Images:
    docker images -a                            # list
    docker image inspect --format='' img_name   # see labels
    docker rmi img_name                         # delete
    docker search search_string                 # look on DockerHub
    docker pull img_name                        # download
    docker build                                # create container
                                                # docker build github.com/this.git
        ** docker build -t image_name -f dockerfile_path host_working_dir
                        --no-cache

    Push to DockerHub:
        docker login
        docker push img_name:tag


Containers:
    docker run --name container_name    # run container
               --rm                     # delete on exit
               --publish 8000:8080      # forward host_port to container_port
               --net=host               # share all ports
               -d/--detach              # run in background
               -it                      # interactive
    docker ps -a                        # list
            -f status-running           # only running
    docker rm id_or_name                # delete
    docker logs #logs                   # view logs
    docker attach id_or_name            # jump in
    docker exec -it container_name bash # run on live container
    docker commit container_name img_name:optional_tag # create image


Volumes:
    docker volume ls                    # list
    docker volume rm volume_name        # delete

--------------------------------------------------------------------------------
TODO
good bases
    ubuntu, python, node...

Management, deployment and scaling:
    Docker-compose
    Kubernetes


Size management:
    docker history <image_name>
        lists size per layer of image

    * use docker ignore

    * use small base image
        e.g. python:3.8-slim not python:3.8

    * DIVE a terminal UI to see size per layers

    * combine layers and clean up
         pip install --user  --no-cache-dir -r requirements.txt \
         && find /root/.local/ -follow -type f ( \
         -name '*.a' -name '*.txt' -name '*.md' -name '*.png' -name '*.jpg' -name '*.jpeg' -name '*.js.map' \
         -name '*.pyc' -name '*.c' -name '*.pxc' -name '*.pyd' \
         ) - delete \
         && find /usr/local/lib/python3.8 -name '__pycache__' | xargs rm -r

    * docker build -f filename.Dockerfile -t image_name --squash
        creates a single layer without you having to write long winded RUNs

    * PYPI wheels not compatible with alpine base images
        wheels dont require compilation

        BUT you can install these deps and then use multi state builds to only copy across the results
            use this: python:3.8-slim-buster

    * clean apt-get installs:
        RUN apt-get install -y && \
        unzip \
        wget

    * COPY only what is required

    * use --no-cache options when installing packages


Cache pip downloads (or other files) between builds for faster builds and reduced bandwidth use
https://pythonspeed.com/articles/docker-buildkit/
1. Ensure the buildkit is used
    $ export DOCKER_BUILDKIT=1

2.Add # syntax=docker/dockerfile:1.2 as the first line of your Dockerfile.

3. Docker-compose will also need this env variable set:
    $ export COMPOSE_DOCKER_CLI_BUILD=1

4. Add a cache moint point in the RUN command e.g.:
    RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

* Build kit can speed up multi-stage builds but doing some in parallel

*Latest versions of Docker may internally prevent apt install from using the cache