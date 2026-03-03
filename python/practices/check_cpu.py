
import psutil
def check_cpu_threshold():
    cpu_threshold = int(input("Enter cpu threshold: "))
    current_cpu__threshold = psutil.cpu_percent(interval =1)

    print("current cpu usages: ",current_cpu__threshold)
    if current_cpu__threshold >cpu_threshold:
        print("Sent email cpu alert")

    else:
        print("cpu is safe state ")



check_cpu_threshold()