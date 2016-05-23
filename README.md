##Scaner of Bob
This a distributed network infotmation collection tool base on Celery.
This a beta version.Now it just can use network host infomation detect base on nmap.
##Usage
It require root privlege.
```
sudo celery worker -A tasks --loglevel=info
```
And you can use celery flower monitor it
```
celery flower --broker=redis://127.0.0.1/0
```
server.py provide the RESTful API to manage the task.
```
python server.py
```
Create task
```
curl -i -H "Content-Type: application/json" -X POST -d '{"target": "127.0.0.1"}' http://127.0.0.1:5000/portmap/api/v1.0/task
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 125
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 12 May 2016 08:21:24 GMT

{
  "task": {
    "status": "PENDING",
    "target": "127.0.0.1",
    "task_id": "83acd56a-ce8d-44e4-91a3-d034ebf3ec6c"
  }
}
```
Get task status
```
curl -i http://127.0.0.1:5000/portmap/api/v1.0/task/result/83acd56a-ce8d-44e4-91a3-d034ebf3ec6c
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 99
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 12 May 2016 08:21:46 GMT

{
  "tasks": {
    "status": "PENDING",
    "task_id": "83acd56a-ce8d-44e4-91a3-d034ebf3ec6c"
  }
}
```
##Feature
Now.提供批量的主机信息探测