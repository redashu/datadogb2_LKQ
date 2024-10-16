## Revision 

## datadog info 

<img src="i.png">

### datadog agent info 

<img src="di1.png">

### datadog agent -- GOlang vs Python 

<img src="go.png">

## datadog sit URL 

<img src="site.png">

[click_here](https://docs.datadoghq.com/getting_started/site/)

### verify datadog agent ON linux machine 

```
whoami
ec2-user
[ec2-user@ip-172-31-36-157 ~]$ sudo -i
[root@ip-172-31-36-157 ~]# whoami
root
[root@ip-172-31-36-157 ~]# 


====>
 systemctl status datadog-agent
● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Wed 2024-10-16 12:58:30 UTC; 3min 16s ago
   Main PID: 2081 (agent)
```

### by Default hostname of machine (linux|mac|windows)

```
hostname
ip-172-31-36-157.ap-south-1.compute.internal
[root@ip-172-31-36-157 ~]# 
```

## Metrics info 

<img src="met1.png">

### name of metrics in Datadog 

<img src="ddm.png">

### metrics name info 

<img src="ddm2.png">

### overall metrics info 

<img src="m1.png">

### default 6 cpu metrics in datadog agent

<img src="ddc.png">

## system.cpu.system (kernel space --process)

<img src="proc1.png">

### cpuIowait 

<img src="iocpu.png">

## Grouping and filtering in datadog 

<img src="ddif.png">

## Tags 

<img src="tag1.png">

## reserver tags as key 

[click_here](https://docs.datadoghq.com/getting_started/tagging/)

<img src="rkey.png">

### ways to tag datadog host infra

<img src="hosti.png">

### datadog.yaml to update datadog agent tags

```
tags:
  - "ashu:windows_10"
  - "os_provider:microsoft"
  - "db:mssql"

```

### changing in linux vm datadog tags

```
ec2-user@ip-172-31-36-157 ~]$ whoami
ec2-user
[ec2-user@ip-172-31-36-157 ~]$ sudo -i
[root@ip-172-31-36-157 ~]# whoami
root
[root@ip-172-31-36-157 ~]# 

```
### changing in yaml file 

```
nano /etc/datadog-agent/datadog.yaml 

====>
tags:
  - "os_privider:linux"
  - "app_server:httpd"
  - "vm_location:aws_cloud"

===>
datadog-agent configcheck 

===>
systemctl restart datadog-agent
[root@ip-172-31-36-157 ~]# systemctl status  datadog-agent
● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Wed 2024-10-16 15:58:48 UTC; 6s ago
   Main PID: 32613 (agent)
      Tasks: 8 (limit: 4658)
```
## verify tags 

```

```