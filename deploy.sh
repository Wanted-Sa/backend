#!bin/bash

EXIST_BLUE=$(sudo docker compose ps | grep blue-backend)
BASE_DOCKER_HUB_REPO="wogur981208/django-wanted-task-blue:latest"

if [ -z "$EXIST_BLUE" ]; then
    BEFORE_COMPOSE_COLOR="green"
    AFTER_COMPOSE_COLOR="blue"
    DOCKER_HUB_IMAGE_BLUE="wogur981208/django-wanted-task-blue:latest"
    CONTAINER_IMAGES_ID=$(sudo docker images $DOCKER_HUB_IMAGE_BLUE -q)
    
    if [ -n "$CONTAINER_IMAGES_ID" ]; then
        sudo docker rmi $CONTAINER_IMAGES_ID
        echo "$AFTER_COMPOSE_COLOR image remove"
    fi

    echo "blue up"
    sudo docker compose up --build -d blue-backend
    sleep 10
    BLUE_HEALTH=$(sudo docker inspect --format='{{.State.Status}}' blue-backend)
    if [ "$BLUE_HEALTH" != "running" ]; then
        echo "Health check failed for blue-backend"
        exit 1
    fi
else
    BEFORE_COMPOSE_COLOR="blue"
    AFTER_COMPOSE_COLOR="green"
    DOCKER_HUB_IMAGE_GREEN="wogur981208/django-wanted-task-green:latest"
    CONTAINER_IMAGES_ID=$(sudo docker images $DOCKER_HUB_IMAGE_GREEN -q)
    
    if [ -n "$CONTAINER_IMAGES_ID" ]; then
        sudo docker rmi $CONTAINER_IMAGES_ID
        echo "$AFTER_COMPOSE_COLOR image remove"
    fi

    echo "green up"
    sudo docker compose up --build -d green-backend
    sleep 10
    GREEN_HEALTH=$(sudo docker inspect --format='{{.State.Status}}' green-backend)
    if [ "$GREEN_HEALTH" != "running" ]; then
        echo "Health check failed for green-backend"
        exit 1
    fi
fi

echo "Start sleep"
sleep 10
echo "End sleep"

EXIST_AFTER=$(sudo docker compose ps | grep ${AFTER_COMPOSE_COLOR}-backend)

if [ -n "$EXIST_AFTER" ]; then
    if [ "$AFTER_COMPOSE_COLOR" = "blue" ]; then
        sed -i 's/green-backend:8001;/blue-backend:8000;/' ./nginx/default.conf
        sudo docker compose restart nginx
        echo "nginx blue-backend port restart"
    else
        sed -i 's/blue-backend:8000;/green-backend:8001;/' ./nginx/default.conf
        sudo docker compose restart nginx
        echo "nginx green-backend port restart"
    fi
 sudo docker compose stop $BEFORE_COMPOSE_COLOR-backend
 sudo docker compose rm -f $BEFORE_COMPOSE_COLOR-backend
 echo "$BEFORE_COMPOSE_COLOR down"
fi