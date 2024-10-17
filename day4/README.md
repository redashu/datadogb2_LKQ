### datadog data collection and retention periods in data types 
<img src="d1.png">

### datadog agent is module based system 

<img src="d2.png">

### checking datadog status in linux infra 

```
ec2-user@ip-172-31-36-157 ~]$ whoami
ec2-user
[ec2-user@ip-172-31-36-157 ~]$ 
[ec2-user@ip-172-31-36-157 ~]$ sudo -i
[root@ip-172-31-36-157 ~]# whoami
root
[root@ip-172-31-36-157 ~]# systemctl status datadog-agent
● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Thu 2024-10-17 12:46:41 UTC; 1min 38s ago
   Main PID: 2067 (agent)
      Tasks: 8 (limit: 4658)

```

### datadog agent Host infra -- default components 

<img src="default1.png">

### INstalling docker in linux vm 

```
yum install docker -y 

===> 
systemctl  start docker 
systemctl  status docker 

```

### Creating 2 webapp containers 

```
docker run -itd --name ashuwebapp2 -p 1235:80 nginx 
docker run -itd --name ashuwebapp1 -p 1234:80 nginx 

===>
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
d5648f1fde47   nginx     "/docker-entrypoint.…"   48 seconds ago       Up 47 seconds       0.0.0.0:1235->80/tcp, :::1235->80/tcp   ashuwebapp2
6076b4ec3892   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:1234->80/tcp, :::1234->80/tcp   ashuwebapp1
[root@ip-172-31-36-157 ~]# 



```
