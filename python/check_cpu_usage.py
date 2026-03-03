import psutil

def check_cpu_threshold():
    print('Current cpu threshold: ',psutil.disk_partitions())

check_cpu_threshold()

#