#!/bin/bash

# Install python2
sudo apt install python2 -y

# Install docker
source ./install_docker.sh

# Start containers
sudo docker-compose up -d

# Install Maven
sudo apt install maven -y

# Setup YCSB workspace
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB

mvn clean package