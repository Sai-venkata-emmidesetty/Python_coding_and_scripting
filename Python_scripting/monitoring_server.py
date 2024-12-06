#We have on premises Linux server which needs some wondering 
#enabled being a devops engineer only you have access to the server
#how would you set up a basic watering script on this on-premises server

import psutil

# CPU times
print(psutil.cpu_times())

# Avg CPU load
print(psutil.getloadavg())

# Memory
print(psutil.virtual_memory())

# Swap memory
print(psutil.swap_memory())

# Disk usage
print(psutil.disk_usage('/'))

# Disk I/O utilization
print(psutil.disk_io_counters(perdisk=False))

# Temp
print(psutil.sensors_temperatures())


#"psutil" -> can be installed in your server using-> "pip install pypi" and then give "pip install psutil"