import matplotlib.pyplot as plt
from datetime import datetime

def create_metric_plot(metric_data, metric_name):
    timestamps = []
    values = []
    
    for sample in metric_data[0]["values"]:
        timestamps.append(datetime.fromtimestamp(sample[0]))
        values.append(float(sample[1]))
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, values)
    plt.title(f"Metric: {metric_name}")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid()
    
    filename = f"{metric_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename)
    plt.close()
    
    return filename