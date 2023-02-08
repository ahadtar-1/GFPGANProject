# GFPGANProject

This project implements GFPGAN for the purpose of upsampling and enhacing faces in images. The whole project is built in a dockerized environment.

# Set up and Installation

### Case 1 - Run Project using Docker Image

The docker image required for this project is available on Docker hub and can be pulled. The project will be up and running once it is pulled and the command to run the docker container is entered.

```bash
git clone https://github.com/ahadtar-1/GFPGANTask.git

cd GFPGANProject

docker pull ahadtar1/flaskapp:latest
```

### Case 2 - Build Docker Image and Run Project

The docker file is provided in the project which builds an image. The project will be up and running once the commands for building the image and container are entered.

```bash
docker build -t ahadtar1/flaskapp:latest . 
```

```bash
docker run -it ahadtar1flaskapp
```

### Case 3 - Run Project without Docker

The project can be run in a non dockerized environment. For that purpose a conda environment should be created (**python 3.9**) to preserve the existant packages and dependencies in the system. The requirements file should then be run in the environment to import the required dependencies for the project. Once packages are imported the project can be run.

```bash
conda create --name py39 python=3.9

source activate py39

pip install -r requirements.txt
```

```bash
python3 app.py
```

# APIs

### Upsampling Image

A post request would be sent to the flask server. It would comprise of an image file. The response sent back from the server would be an upsampled image file of the sent image.

#### API Endpoint

```
0.0.0.0:5000/upsampleimg 
```

#### Payload
```
{
    "file" : testimg.jpg

    key must be the string "file"
    value must be the file
}
```

### Enhance Image

A post request would be sent to the flask server. It would comprise of an image file. The response sent back from the server would be an enhanced image file of the sent image.

#### API Endpoint

```
0.0.0.0:5000/enhanceimg 
```

#### Payload
```
{
    "file" : testimg.jpg

    key must be the string "file"
    value must be the file
}
```
