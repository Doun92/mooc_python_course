# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        if len(str(self.seconds)) < 2:
            show_seconds = f"0"+str(self.seconds)
        else:
            show_seconds = self.seconds

        if len(str(self.minutes)) < 2:
            show_minutes = f"0"+str(self.minutes)
        else:
            show_minutes = self.minutes

        return f"{show_minutes}:{show_seconds}"


    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.minutes = 0
                self.seconds = 0                
