<<<<<<< HEAD
class Time():
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute

    def normalizetime(self):
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        if self.hour == 24:
            self.day += 1
            self.hour = 0

    def print_time(self):
        print(f"Day: {self.day} {self.hour:02}:{self.minute:02}")

def gtime(time_speed, pause):
    import time
    cr_time = Time(00,00,00)
    while pause != True:
        time.sleep(1 // time_speed)
        cr_time.minute += 1
        cr_time.normalizetime()
        cr_time.print_time()

if __name__ == "__main__":
    time_speed = 1
    pause = False
    gtime(time_speed, pause)
=======
import time
import ctypes
import pygame
>>>>>>> 21f762d544fb293ab5100765ad1851efc3257e77
