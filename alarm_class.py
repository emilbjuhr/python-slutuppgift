class Alarm:

    def __init__(self, alarm_active_at, alarm_type, alarm_name=None):
        self.alarm_active_at = alarm_active_at
        self.alarm_type = alarm_type
        self.alarm_name = alarm_name

    def __str__(self):
        return f" {self.alarm_type}-alarm: {self.alarm_name} aktiveras vid {self.alarm_active_at}%"
    
    def __repr__(self):
        return f"{self.alarm_type} {self.alarm_name} {self.alarm_active_at}"
    
    