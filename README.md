# Grafana Crypto Charts
![image](https://user-images.githubusercontent.com/89855562/136545701-33d3d2b0-9721-4188-8e63-3eba4276577a.png)

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
 - job_name: 'your_name'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:8001']
```
8001 port is the same as in blockchain_stats.py file (juno,akash,etc)


Restart prometheus 

```
systemctl restart prometheus.service
```

Run blockchain_stats.py file
!!! Don't forgot to update LCD_ENDPOINT with your API endpoints. 

```
python3 blockchain_stats.py (juno,akash,etc)
```

All metrics will be imported to prometheus and you can use them in Grafana now.

You can easily add your metrics to api_calls.py file and than add to blockchain_stats.py (juno,akash,etc)

Also you can export my dashboard configurations (.json file in blockchain name folder) and apply them for your needs.
