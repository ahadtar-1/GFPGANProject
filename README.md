# GFPGANProject

This project implements GFPGAN for the purpose of upsampling and enhacing faces in images. The whole project is built in a dockerized environment.

# Set up and Installation
### Clone repository

The repository can be downloaded in the local system through cloning the repository. The link provided can be entered in the terminal inorder for downloading the project.

```
# Clone repository
https://github.com/ahadtar-1/GFPGANTask.git

# Changing the current directory to the project
cd GFPGANProject
```

### Case 1 - Run Project using Docker Image

The docker image required for this project is available on Docker hub and can be pulled. The project will be up and running once it is pulled and the command to run the docker container is entered.

```
# Pull docker image
docker pull ahadtar1/flaskapp:latest
```
```
# Run application
docker run -it ahadtar1/flaskapp
```

### Case 2 - Build Docker Image and Run Project

The docker file is provided in the project which builds an image. The project will be up and running once the commands for building the image and container are entered.

```
# Build docker image
docker build -t flaskapp:latest . 
```
```
# Run application
docker run -it flaskapp
```

### Case 3 - Run Project without Docker

The project can be run in a non dockerized environment. For that purpose a conda environment should be created (**python 3.9**) to preserve the existant packages and dependencies in the system. The requirements file should then be run in the environment to import the required dependencies for the project. Once packages are imported the project can be run.

```
# Creating conda environment
conda create --name py39 python=3.9

# Activating environment
source activate py39

# Importing required dependencies and packages
pip install -r requirements.txt
```

```
# Run application
python3 app.py
```
