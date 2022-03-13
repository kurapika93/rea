#!/bin/sh   
clear; 
read -p "username: " username
read -p "password: " password
if [[ $username == "qa" && $password == "engineer" ]];
then 
echo "login success"
else
echo "login failed"
fi