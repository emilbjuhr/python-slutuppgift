# När programmet körs ska en knapp visas som startar själva programmet.
# När startknappen blir tryckt så kommer en meny som visar följande val:
#1. Starta övervakningsläge
#2. Skapa larm
#3. Konfigurera larm
#4. Larm lista
#5. Avsluta programmet

# Starta övervakningsläge
# Hämta data från def get_cpu_usage(), def get_memory_usage() och def get_disk_usage()
# Visa data i någon form av UI som uppdateras varje sekund 
# Skriv ut att användaren kan trycka enter för att återgår den till huvudmenyn
import psutil

print("----")
psutil.cpu_percent(interval=1,percpu=True)
print(f"{psutil.cpu_percent()} % CPU-användning")
print("----")
psutil.virtual_memory()
mem = psutil.virtual_memory()
print(f"{mem.percent} % Minnes-användning")
print("----")
psutil.disk_usage("/")
disk_usage = psutil.disk_usage("/")
print(f"{disk_usage.percent} % Disk-användning")




'''
start = True

while(start):
    print("1: Starta övervakning")
    print("2: Skapa larm")
    print("3: Konfigurera larm")
    print("4: Larm lista")
    print("5: Avsluta program")

    if input("1"):
        pass
    
    elif input("2"):
        pass

    elif input("3"):
        pass

    elif input("4"):
        pass

    elif input("5"):
        start = False
        print("Avslutar programmet")
'''