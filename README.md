# Grafana Crypto Charts
![image](https://user-images.githubusercontent.com/89855562/134243318-0cf33d0f-d98f-46ad-83b0-241b5dc7f52a.png)

To create the same dashboard you need:
1. Install Grafana [Grafana and prometheus](https://github.com/CyberObiOne/node-monitoring-setup)
2. Python3

Install prometheus_client for python

```
pip3 install prometheus_client
pip3 install json
pip3 install requests
```

Edit /etc/prometheus/prometheus.yml and add following lines:

```
 - job_name: 'akash'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:8001']
```
8001 port is the same as in akash_stats.py file


Restart prometheus 

```
systemctl restart prometheus.service
```

Run akash_stats.py file

```
python3 akash_stats.py
```

All metrics will be imported to prometheus and you can use them in Grafana now.

You can easily add your metrics to api_calls.py file and than add to akash_stats.py
