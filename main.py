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
import time
import msvcrt

done_monitoring = False
start = True

while(start):
    print("1: Starta övervakning")
    print("2: Skapa larm")
    print("3: Konfigurera larm")
    print("4: Larm lista")
    print("5: Avsluta program")

    menu_input = input("Välj ett alternativ: ")

    if menu_input == "1":
        while(not done_monitoring):
            cpu_usage = psutil.cpu_percent(interval=1,percpu=False)
            print(f"{cpu_usage} % CPU-användning")
            mem = psutil.virtual_memory()
            print(f"{mem.percent} % Minnes-användning")
            disk_usage = psutil.disk_usage("/")
            print(f"{disk_usage.percent} % Disk-användning")
            print("Tryck Enter för att avsluta övervakning")
            print("----")
            time.sleep(2)
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\r':
                    done_monitoring = True

    
    elif menu_input == "2":
        pass

    elif menu_input == "3":
        pass

    elif menu_input == "4":
        pass

    elif menu_input == "5":
        print("Avslutar programmet")
        start = False
