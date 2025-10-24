import psutil # To get system usage
import time # To create delays
import keyboard  # For detecting key presses
from alarm_class import Alarm

def add_alarm(alarm):
    alarm_list.append(alarm)
    print(f"Skapat alarm: \n{alarm}")
    return alarm

def get_activate_at_number(number_text):
    while True:
        try:
            number = int(input(number_text))
            if number < 1 or number > 100:
                raise ValueError
        except ValueError:
            print("Det måste vara ett nummer mellan 1-100")
        else:
            return number
        
def monitor_activate_at_alarms():
    for alarm in alarm_list:
        if alarm.alarm_type == "CPU" and cpu >= alarm.alarm_active_at:
            print(f"VARNING! {alarm} har aktiverats")
        elif alarm.alarm_type == "Minne" and mem.percent >= alarm.alarm_active_at:
            print(f"VARNING! {alarm} har aktiverats")
        elif alarm.alarm_type == "Disk" and disk.percent >= alarm.alarm_active_at:
            print(f"VARNING! {alarm} har aktiverats")

def read_alarms_from_file():
    alarm_list=[]
    try:
        with open("alarm_list_data.json", "r") as alarm_file:
            alarm_lines = alarm_file.readlines()
            for alarm in alarm_lines:
                alarm_info = alarm.strip().split(",")
                alarm_type = alarm_info[0]
                alarm_name = alarm_info[1]
                alarm_active_at = int(alarm_info[2])
                new_alarm = Alarm(
                    alarm_active_at,
                    alarm_type,
                    alarm_name
                    )
                alarm_list.append(new_alarm)
        return alarm_list
    except FileNotFoundError:
        print("Ingen sparad alarm lista hittades.")
        return []

def write_alarms_to_file(alarm_list):
    try:    
        with open("alarm_list_data.json", "w") as alarm_file:
            for alarm in alarm_list:
                alarm_line = f"{alarm.alarm_type},{alarm.alarm_name},{alarm.alarm_active_at}\n"
                alarm_file.write(alarm_line)
    except FileNotFoundError:
        print("Kunde inte spara alarm lista.")

def print_monitor_data():
    print(f"{cpu} % CPU-användning")
    print(f"{mem.percent} % Minnes-användning")
    print(f"{disk.percent} % Disk-användning")
    print("Tryck Enter för att avsluta övervakning")
    print("----")

def show_alarm_creation_menu():
    print("1: CPU")
    print("2: Minne")
    print("3: Disk")
    print("4: Tillbaka till huvudmeny")

def show_main_menu():
    print()
    print("1: Visa systemstatus")
    print("2: Skapa alarm")
    print("3: Alarm lista")
    print("4: Starta larmövervakning")
    print("5: Avsluta program")

start = True
alarm_list = read_alarms_from_file()

# Main menu loop
def main():
    global cpu, mem, disk
    cpu = psutil.cpu_percent(interval=1,percpu=False)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    start = True
    alarm_list = read_alarms_from_file()
    
    while(start):
        done_monitoring = False
        alarm_menu = True
        
        show_main_menu()
        vaild_input = False
        while(not vaild_input):
            menu_input = input("Välj ett alternativ: ")
            match menu_input:
                case "1":
                    while(not done_monitoring):
                        print_monitor_data()
                        time.sleep(2)
                        if keyboard.is_pressed('enter'):
                            done_monitoring = True
                    vaild_input = True
                case "2":
                    while (alarm_menu):
                        show_alarm_creation_menu()
                        alarm_input = False
                        while(not alarm_input):
                            create_alarm_input = input("Välj ett alternativ: ")
                            match create_alarm_input:
                                case "1":
                                    alarm_name = input("Ange ett namn för larmet: ")
                                    alarm_type = "CPU"
                                    alarm_active_at = get_activate_at_number("Ange vid vilken procent du vill bli larmad: ")
                                    new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                    add_alarm(new_alarm)
                                    alarm_input = True
                                case "2":
                                    alarm_name = input("Ange ett namn för larmet: ")
                                    alarm_type = "Minne"
                                    alarm_active_at = get_activate_at_number("Ange vid vilken procent du vill bli larmad: ")
                                    new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                    add_alarm(new_alarm)
                                    alarm_input = True
                                case "3":
                                    alarm_name = input("Ange ett namn för larmet: ")
                                    alarm_type = "Disk"
                                    alarm_active_at = get_activate_at_number("Ange vid vilken procent du vill bli larmad: ")
                                    new_alarm = Alarm(alarm_active_at, alarm_type, alarm_name)
                                    add_alarm(new_alarm)
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
                    while done_monitoring == False:
                        monitor_activate_at_alarms()
                        print("Tryck Enter för att avsluta larmövervakning")
                        print("----")
                        time.sleep(2)
                        if keyboard.is_pressed('enter'):
                            done_monitoring = True
                    vaild_input = True
                case "5":
                    write_alarms_to_file(alarm_list)
                    quit()
                case _:
                    print("Det måste vara 1-5")
if __name__=="__main__":
    main()
