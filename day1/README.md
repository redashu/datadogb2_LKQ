## Monitoring --> Observability 

<img src="obs1.png">

## Problem with Going to self managed Monitoring stack 

<img src="monp.png">

## Intro to SAAS (software as a service ) based Monitoring solutions 

<img src="datadog1.png">

### Introduction to datadog 

<img src="datadog2.png">

### datadog agent 

<img src="da.png">

### official web link of datadog for account creation / docs 

[click_here](https://www.datadoghq.com/)


### datadog agent -- more info 

<img src="dd_info.png">

## dealing with Remote Linux server 

### some basic commands 

```
[ec2-user@ip-172-31-36-157 ~]$ whoami
ec2-user

```

### login to root / admin user 

```
[ec2-user@ip-172-31-36-157 ~]$ sudo -i 
[root@ip-172-31-36-157 ~]# 
[root@ip-172-31-36-157 ~]# whoami
root
[root@ip-172-31-36-157 ~]# 

```

### Installing datadog agent v7 on linux machine 

```
[root@ip-172-31-36-157 ~]# dnf install -y libxcrypt-compat

Last metadata expiration check: 0:32:36 ago on Mon Oct 14 14:06:07 2024.
Dependencies resolved.
===========================================================================================================================================
 Package                             Architecture              Version                                Repository                      Size
===========================================================================================================================================
Installing:
 libxcrypt-compat                    x86_64                    4.4.33-7.amzn2023                      amazonlinux                     92 k

Transaction Summary

```

### installing agent 

```
DD_API_KEY="past-your-key-here" \
DD_SITE="us5.datadoghq.com" \
bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```

### verify installation  and check datadog agent service 

<img src="dir.png">

### checking config file 

```
 cd /etc/datadog-agent/
[root@ip-172-31-36-157 datadog-agent]# 

[root@ip-172-31-36-157 datadog-agent]# ls
auth_token  compliance.d  datadog.yaml          environment   install_info        security-agent.yaml.example  system-probe.yaml.example
checks.d    conf.d        datadog.yaml.example  install.json  runtime-security.d  selinux
[root@ip-172-31-36-157 datadog-agent]# 


```

### status of agent 

```
systemctl   status  datadog-agent 


● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Mon 2024-10-14 14:43:32 UTC; 27min ago
   Main PID: 4408 (agent)
      Tasks: 8 (limit: 4658)
     Memory: 116.6M
        CPU: 15.833s
```

### more datadog agent status management commands 

```
11  systemctl   stop   datadog-agent 
   12  systemctl   status  datadog-agent 
   13  systemctl   start  datadog-agent 
   14  systemctl   status  datadog-agent 
```

