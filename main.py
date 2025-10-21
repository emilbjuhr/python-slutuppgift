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

import psutil # To get system usage
import time # To create delays
import msvcrt # Only for Windows, for detecting key presses
from alarm_class import Alarm


def add_alarm(alarm):
    alarm_list.append(alarm)
    print(f"Skapat alarm: \n{alarm}")
    return alarm

def get_number(number_text):
    while True:
        try:
            number = int(input(number_text))
            if number < 1 or number > 100:
                raise ValueError
        except ValueError:
            print("Det måste vara ett nummer mellan 1-100")
        else:
            return number
        
def monitor_alarms():
    if alarm.alarm_type == "CPU" and cpu >= alarm.alarm_active_at:
        print(f"VARNING! {alarm} har aktiverats")
    elif alarm.alarm_type == "Minne" and mem.percent >= alarm.alarm_active_at:
        print(f"VARNING! {alarm} har aktiverats")
    elif alarm.alarm_type == "Disk" and disk.percent >= alarm.alarm_active_at:
        print(f"VARNING! {alarm} har aktiverats")

start = True
alarm_list=[]

# Main menu loop
while(start):
    done_monitoring = False
    alarm_menu = True

    print()
    print("1: Starta övervakning")
    print("2: Skapa alarm")
    print("3: Alarm lista")
    print("4: Starta larmövervakning")
    print("5: Avsluta program")
    vaild_input = False
    while(not vaild_input):
        menu_input = input("Välj ett alternativ: ")
        match menu_input:
            case "1":
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
                vaild_input = True
            case "2":
                while (alarm_menu):
                    print("1: CPU")
                    print("2: Minne")
                    print("3: Disk")
                    print("4: Tillbaka till huvudmeny")
                    alarm_input = False
                    while(not alarm_input):
                        create_alarm_input = input("Välj ett alternativ: ")
                        match create_alarm_input:
                            case "1":
                                alarm_name = input("Ange ett namn för larmet: ")
                                alarm_type = "CPU"
                                alarm_active_at = get_number("Ange vid vilken procent du vill bli larmad: ")
                                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                alarm_added = add_alarm(new_alarm)
                                alarm_input = True
                            case "2":
                                alarm_name = input("Ange ett namn för larmet: ")
                                alarm_type = "Minne"
                                alarm_active_at = get_number("Ange vid vilken procent du vill bli larmad: ")
                                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                alarm_added = add_alarm(new_alarm)
                                alarm_input = True
                            case "3":
                                alarm_name = input("Ange ett namn för larmet: ")
                                alarm_type = "Disk"
                                alarm_active_at = get_number("Ange vid vilken procent du vill bli larmad: ")
                                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                alarm_added = add_alarm(new_alarm)
                                alarm_input = True
                            case "4":
                                alarm_menu = False
                                alarm_input = True
                            case _:
                                print("Det måste vara 1-4")
                vaild_input = True
            case "3":
                sorted_alarms = sorted(alarm_list, key=lambda a: a.alarm_type)
                list(map(print, sorted_alarms))
                input("Tryck Enter för att gå tillbaka till huvudmenyn")
                vaild_input = True
            case "4":
                mem = psutil.virtual_memory()
                cpu = psutil.cpu_percent(interval=1,percpu=False)
                disk = psutil.disk_usage("/")
                while done_monitoring == False:
                    for alarm in alarm_list:
                        monitor_alarms()
                    print("Tryck Enter för att avsluta larmövervakning")
                    print("----")
                    time.sleep(10)
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b'\r':
                            done_monitoring = True
                vaild_input = True
            case "5":
                start = False
            case _:
                print("Det måste vara 1-5")