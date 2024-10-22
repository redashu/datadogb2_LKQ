### Datadog -- Things to Remember 

<img src="dd1.png">

### datadog observations on non app server based webapps 

<img src="dd2.png">

### Logging options 

<img src="log1.png">

### check httpd app server status

```
ec2-user@ip-172-31-36-157 ~]$ sudo   -i
[root@ip-172-31-36-157 ~]# 
[root@ip-172-31-36-157 ~]# whoami
root
[root@ip-172-31-36-157 ~]# 
[root@ip-172-31-36-157 ~]# systemctl status  httpd
○ httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: man:httpd.service(8)
[root@ip-172-31-36-157 ~]# systemctl start  httpd

===>> making enable on boot 
[root@ip-172-31-36-157 ~]# systemctl enable   httpd
Created symlink /etc/systemd/system/multi-user.target.wants/httpd.service → /usr/lib/systemd/system/httpd.service.

===>
[root@ip-172-31-36-157 ~]# systemctl status  httpd
● httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; preset: disabled)
     Active: active (running) since Tue 2024-10-22 12:37:34 UTC; 13s ago
       Docs: man:httpd.service(8)
   Main PID: 3178 (httpd)
     Status: "Total requests: 0; Idle/Busy workers 100/0;Requests/sec: 0; Bytes served/sec:   0 B/sec"
      Tasks: 177 (limit: 4658)
```

### log location of httpd server

```
root@ip-172-31-36-157 ~]# cd  /var/log/httpd/
[root@ip-172-31-36-157 httpd]# ls
access_log  error_log
[root@ip-172-31-36-157 httpd]# 


```

### datadog as logging solution 

<img src="dlog1.png">

### datadog store logs in Indexed format (db table format schema)

<img src="stored.png">


### enable datadog for apache httpd 

### change ing datadog.yaml file 
```
logs_enabled: true
```

### enable apache integration 

```
nano /etc/datadog-agent/conf.d/apache.d/ashu_httpd.yaml

===>
#Log section
logs:

    # - type : (mandatory) type of log input source (tcp / udp / file)
    #   port / path : (mandatory) Set port if type is tcp or udp. Set path if type is file
    #   service : (mandatory) name of the service owning the log
    #   source : (mandatory) attribute that defines which integration is sending the log
    #   sourcecategory : (optional) Multiple value attribute. Can be used to refine the source attribute
    #   tags: (optional) add tags to each log collected

  - type: file
    path: /var/log/httpd/access_log
    source: apache
    sourcecategory: http_web_access
    service: ashuservice

  - type: file
    path: /var/log/httpd/error_log
    source: apache
    sourcecategory: http_web_access
    service: ashuservice
```

### set permission 

```
chmod 755 /var/log/httpd
```
### restart service and verify it 

```
systemctl restart datadog-agent 

===>
datadog-agent status  # please check Log-agent section from bottom 

```