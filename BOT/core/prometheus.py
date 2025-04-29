from prometheus_api_client import PrometheusConnect
from datetime import datetime, timedelta

class PrometheusClient:
    def __init__(self, url):
        self.prom = PrometheusConnect(url=url, disable_ssl=True)
        
    def get_metric(self, metric_name, duration="1h"):
        metric_data = self.prom.get_metric_range_data(
            metric_name=metric_name,
            start_time=datetime.now() - timedelta(minutes=int(duration[:-1])*60),
            end_time=datetime.now()
        )
        return metric_data