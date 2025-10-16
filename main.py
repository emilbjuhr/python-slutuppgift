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

class Alarm:
    alarm_list=[]

    def __init__(self, alarm_active_at, alarm_type, alarm_name=None):
        self.alarm_active_at = alarm_active_at
        self.alarm_type = alarm_type
        self.alarm_name = alarm_name

    def __str__(self):
        return f" {self.alarm_type}-alarm: {self.alarm_name} aktiveras vid {self.alarm_active_at}%"
    
    def add_alarm(alarm):
        Alarm.alarm_list.append(alarm)
        print(f"Skapat alarm: \n{alarm}")
        return alarm

#When an alarm reach the set % it will type out a message
def monitor(alarm_list):

    pass


start = True

# Main menu loop
while(start):
    done_monitoring = False
    alarm_menu = True

    print()
    print("1: Starta övervakning")
    print("2: Skapa alarm")
    print("3: Alarm lista")
    print("4: Konfigurera alarm")
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
        while (alarm_menu):
            print("1: CPU")
            print("2: Minne")
            print("3: Disk")
            print("4: Tillbaka till huvudmeny")
            create_alarm = input("Välj vilket typ av larm du vill skapa: ")

            if create_alarm == "1":
                alarm_name = input("Ange ett namn för larmet: ")
                alarm_type = "CPU"
                alarm_active_at = input("Ange vid vilken procent du vill bli larmad: ")
                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                alarm_added = Alarm.add_alarm(new_alarm)

            elif create_alarm == "2":
                alarm_name = input("Ange ett namn för larmet: ")
                alarm_type = "Minne"
                alarm_active_at = input("Ange vid vilken procent du vill bli larmad: ")
                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                alarm_added = Alarm.add_alarm(new_alarm)
                
            elif create_alarm == "3":
                alarm_name = input("Ange ett namn för larmet: ")
                alarm_type = "Disk"
                alarm_active_at = input("Ange vid vilken procent du vill bli larmad: ")
                new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                alarm_added = Alarm.add_alarm(new_alarm)

            elif create_alarm == "4":
                alarm_menu = False
                pass

    elif menu_input == "3":
        for alarm in Alarm.alarm_list:
            print(alarm)
        input("Tryck Enter för att gå tillbaka till huvudmenyn")


    elif menu_input == "4":
        pass

    elif menu_input == "5":
        print("Avslutar programmet")
        start = False