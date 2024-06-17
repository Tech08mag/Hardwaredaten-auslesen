import platform,json,psutil,cpuinfo

def getSystemInfo():
    systemInfo = {}

    pName = platform.uname().system

    if "darwin" in pName.lower():
        pName = "macOS"

    # System Informationen

    systemInfo["os"] = pName
    systemInfo["osVersion"] = platform.uname().release
    systemInfo["osArch"] = platform.uname().machine

    # CPU Informationen

    systemInfo["cpu"] = cpuinfo.get_cpu_info()["brand_raw"]
    systemInfo["cpuCores"] = psutil.cpu_count(logical=False)
    systemInfo["cpuThreads"] = psutil.cpu_count(logical=True)

    # RAM Informationen

    ram = psutil.virtual_memory()

    systemInfo["ram"] = ram.total / 1024**3

    systemInfo["ramUsed"] = (ram.total - ram.available) / 1024**3
    systemInfo["ramAvailable"] = ram.available / 1024**3
    systemInfo["ramPercent"] = ram.percent

    # Disk Informationen

    disk = psutil.disk_usage("/")

    systemInfo["disk"] = disk.total / 1024**3
    systemInfo["diskUsed"] = (disk.total - disk.free) / 1024**3
    systemInfo["diskFree"] = disk.free / 1024**3
    systemInfo["diskPercent"] = disk.percent

    return systemInfo

if __name__ == '__main__':
    info = getSystemInfo()

    print(json.dumps(info, indent=4))