### datadog  revision 

<img src="rev11.png">

### datadog certifications 

[click_here](https://www.datadoghq.com/certification/overview/)

### checking docker and datadog agent status

```
systemctl status datadog-agent
● datadog-agent.service - Datadog Agent
     Loaded: loaded (/usr/lib/systemd/system/datadog-agent.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-10-18 12:39:46 UTC; 1min 46s ago
   Main PID: 2083 (agent)
      Tasks: 8 (limit: 4658)
     Memory: 275.9M

===>
systemctl status docker

```

### datadog agent as container 

<img src="agc.png">

### running datadog agent as container 

```
docker run -d --name dd-agent \
-e DD_API_KEY="put_your_apikey" \
-e DD_SITE="us5.datadoghq.com" \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v /proc/:/host/proc/:ro \
-v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
-v /var/lib/docker/containers:/var/lib/docker/containers:ro \
    --restart always   -v /etc/passwd:/etc/passwd:ro -e DD_PROCESS_CONFIG_PROCESS_COLLECTION_ENABLED=true  gcr.io/datadoghq/agent:7
```

### container creating 

```
docker run -itd --name ashuappnewc11  -p 1234:80 nginx 

```

## not all the metrics being send to DD account 

### after flush temer and aggregation process

<img src="agr.png">

### metrics type understanding 

<img src="mt.png">

### Datadog QL 

<img src="dql.png">

### datadog process details in linux 

```
 sudo -i
[root@ip-172-31-39-244 ~]# docker  ps | grep -i ashu
9b0c8dfa9947   alpine                     "/bin/sh"                2 hours ago   Up 2 hours                                                                   ashualpc1
48ff469fce5b   nginx                      "/docker-entrypoint.…"   2 hours ago   Up 2 hours             0.0.0.0:1234->80/tcp, :::1234->80/tcp                 ashuappnewc11
[root@ip-172-31-39-244 ~]# 
[root@ip-172-31-39-244 ~]# docker inspect ashualpc1 | grep -i pid 
            "Pid": 42732,
            "PidMode": "",
            "PidsLimit": null,
[root@ip-172-31-39-244 ~]# 
[root@ip-172-31-39-244 ~]# cd /proc/42732
[root@ip-172-31-39-244 42732]# ls
arch_status  clear_refs       cwd      gid_map   map_files  mountstats  oom_score      projid_map  setgroups     statm           timers
attr         cmdline          environ  io        maps       net         oom_score_adj  root        smaps         status          timerslack_ns
autogroup    comm             exe      latency   mem        ns          pagemap        sched       smaps_rollup  syscall         uid_map
auxv         coredump_filter  fd       limits    mountinfo  numa_maps   patch_state    schedstat   stack         task            wchan
cgroup       cpuset           fdinfo   loginuid  mounts     oom_adj     personality    sessionid   stat          timens_offsets
[root@ip-172-31-39-244 42732]# 

```
