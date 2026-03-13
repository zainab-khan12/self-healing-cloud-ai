import numpy as np

data["Failure"] = np.where(
    (data["cpu_util_percent"] > 90) &
    (data["mem_util_percent"] > 85) &
    (data["disk_io_percent"] > 80),
    1,
    0
)

print(data["Failure"].value_counts())

X = data[['cpu_util_percent','mem_util_percent','net_in','net_out','disk_io_percent']]
y = data['Failure']
