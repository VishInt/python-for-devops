import psutil  # import the lib from pypi

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the cpu threshold (%): ")) 

    current_cpu = psutil.cpu_percent(interval=1)
    print("current cpu % : ", current_cpu)

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    else:
        print("CPU in safe state...")

def check_memory_threshold():
    memory_threshold = int(input("Enter the memory threshold (%): "))

    current_memory = psutil.virtual_memory().percent
    print("Current memory:  ", current_memory)

    if current_memory > memory_threshold:
        print("Memory alert Email sent...")
    else:
        print("Memory in safe state....")

def check_disk_threshold():
    disk_threshold = int(input("Enter the Disk threshold (%): "))

    current_disk = psutil.disk_usage('/').percent

    print("current_disk %: ", current_disk)

    if current_disk > disk_threshold:
        print("Disk alert Email sent....")
    else:
        print("Disk in safe state....")

check_cpu_threshold()
check_memory_threshold()
check_disk_threshold()

