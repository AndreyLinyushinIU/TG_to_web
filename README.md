##Installation
1. Install python, pip and required packages
```shell
sudo apt install python3 python3-pip
pip3 install django djangorestframework PyTelegramBotAPI psycopg2-binary
```
2. Install Docker on your machine:
```shell
sudo snap install docker
```
##Running
Run Docker container with PostgreSQL in it:
```shell
docker run -p 5432:5432 --name db_container --rm -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres postgres
```
Running server: 
```shell
python3 manage.py runserver 192.168.1.1:8000
```
Killing Docker container (in case of troubles/restarts). Getting a message
*"docker rm" requires at least 1 argument* is OK.
```shell
docker stop $(docker ps -qa) && docker rm $(docker ps -qa)
```
If getting an error *'listen tcp4 0.0.0.0:5432: bind: address already in use'*
get the list of processes acquiring this port and kill them
```shell
sudo ss -lptn 'sport = :5432'
sudo kill {process id}
```
If any change was applied to models.py files, run the following:
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

When rebuilt react part: 
npm run build
python3 manage.py collectstatic