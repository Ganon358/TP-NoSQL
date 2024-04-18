#!/bin/bash

current_position=$(pwd)
docker exec -i mongo1 mongoimport --db rs --collection usersCollection --drop --jsonArray < "$current_position/users.json" 