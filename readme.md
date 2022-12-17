# Carford car shop 
Carford car shop system - located in Nork-Town.

It lets you CRUD cars and car owners by following some brilliant rules:
- The person can have up to 3 vehicles.
- The vehicle can have color: 
    - yellow, 
    - blue,
    - gray.

- And one of three models: 
    - hatchback, 
    - sedan, 
    - convertible.
#
## Start Project
#
### dependency: 
Need docker and docker compose, can be install from [documentation](https://docs.docker.com/desktop/)

Make fork or clone repo:
```
git clone git@github.com:<seu_usuario>/Python_Projects.
```
Navigate to the project folder:
```
cd ../Python_Projects/DJANGO_CARFORD
```
Run the command in the terminal to up containers on docker
```
docker compose up
```
### Start Application
#### Launch browser
    http://localhost:8000

After you can run command to create super user admin on DB
```
docker exec -it db6594f04753 python /app/django_carford_proj/manage.py createsuperuser
```


```[tasklist]
### Tasks
- [ ] protect frontend agains IDOR - with Hash
- [ ] Improve frontend
- [ ] Install containers dependencs with pipenv
- [ ] Divede containers - Python, DB and Frontend
- [ ] Extract environment variables
```