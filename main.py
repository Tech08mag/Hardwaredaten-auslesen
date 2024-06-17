import platform, cpuinfo
import psutil

data = psutil.virtual_memory()
cpuData = cpuinfo.get_cpu_info()
system = platform.system() # Ausgabe z.B: Darwin, Linux, Windows
print(system, cpuData, data)