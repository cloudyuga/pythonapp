# Pythonapp

First git clone the Directory.
```
$ git clone https://github.com/vishalcloudyuga/pythonapp.git
```
Enter into the Directory.
```
$ cd pythonapp
```
Check the contents.
```
$ ls
demo.py  docker-compose.yaml  Dockerfile  program  README.md
```
All the pythons programs are kept into the `program` directory.

if we want to run the program `p1.py` then we will will run it as.
```
$ docker-compose run -e PROG='p1' app
```

if we want to run the program `p2.py` then we will will run it as
```
$ docker-compose run -e PROG='p2' app
```
We are passing `name of program` with out extension as environt variable.

Lets run the program `p9.py` which create Upper case string of the string which we give as input. When it shows p9 on screen enter your strings `Hello world` and `Practice makes perfect` and hit enter twice.
```
$ docker-compose run -e PROG='p9' app
p9
Hello world
Practice makes perfect

```
Now lets check the output of this program. Lets check the Docker volumes.
```
$ docker volume ls
DRIVER              VOLUME NAME
local               pythonapp_db_data
```
this volume we have specified in the `docker-compose` file.
Lets find the exact location of the volume and see the output file generated there.
```
$ docker volume inspect pythonapp_db_data
docker volume inspect pythonapp_db_data
[
    {
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/pythonapp_db_data/_data",
        "Name": "pythonapp_db_data",
        "Options": {},
        "Scope": "local"
    }
]

```
Check the files present in that volume.
```
$ ls /var/lib/docker/volumes/pythonapp_db_data/_data
p1.txt  p2.txt  p9.txt
```
Lets verify the output of program `p9.py` stored in file `p9.txt`.
```
$ cat /var/lib/docker/volumes/pythonapp_db_data/_data/p9.txt
```
