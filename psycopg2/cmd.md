## pythonアプリコンテナ起動

```
docker run --volume $PWD/app:/app -itd --name=pytest pytest /bin/bash
```


## PostgreSQLコンテナ起動

```
docker run -d -e POSTGRES_PASSWORD=secret -v ~/docker/postgres:/var/lib/postgresql/data --name testc -p 5432:5432 postgres:10-alpine
```