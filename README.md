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

