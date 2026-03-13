from datacentertracesdatasets import loadtraces
import pandas as pd

data = loadtraces.get_trace(
    trace_name='alibaba2018',
    trace_type='machine_usage',
    stride_seconds=300
)

print(data.head())
print(data.shape)

data.to_csv("alibaba_metrics.csv",index=False)
