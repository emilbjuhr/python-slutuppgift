from main import add_alarm
from alarm_class import Alarm

def test_add_alarm():
    new_alarm = Alarm(90, "CPU", "Emils Alarm")
    assert add_alarm(new_alarm) == new_alarm