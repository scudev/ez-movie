sudo docker-compose down
sudo docker image rm server_ezm-backend
sudo docker-compose up -d
sudo docker logs -f ezm-backend
