# Operation Linguistic Infiltration 🕵

### Objective

The following project fetches information about all the the programming languages used in the LSST-IT/LSST-Control repository and displays the size of code written in each language. 

## Docker Image Repository Location:
   https://hub.docker.com/repository/docker/dtapiacl/docker-lang:v1.0
* To pull the Docker image: <br>
  ** docker pull dtapiacl/docker-lang:v1.0
* To run the Docker image: <br>
  * docker run docker-lang:v1.0

## Guide to run the code and unit test:
* To run the code:<br>
  **python3 fetch_languages.py**

* To run the test:<br>
  **python3 -m unittest test_fetch_languages.py**