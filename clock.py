# Write your solution here:
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        if len(str(self.seconds)) < 2:
            show_seconds = f"0"+str(self.seconds)
        else:
            show_seconds = self.seconds

        if len(str(self.minutes)) < 2:
            show_minutes = f"0"+str(self.minutes)
        else:
            show_minutes = self.minutes

        if len(str(self.hours)) < 2:
            show_hours = f"0"+str(self.hours)
        else:
            show_hours = self.hours

        return f"{show_hours}:{show_minutes}:{show_seconds}"

    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0
                if self.hours == 24:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0

    def set(self, h:int, m:int):
        self.hours = h
        self.minutes = m
        self.seconds = 0