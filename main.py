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
        return(f"Day: {self.day} {self.hour:02}:{self.minute:02}")

class Weather:
    def __init__(self, weather_type):
        self.type = weather_type
        self.active = False

def losuj_pogode(x, tab, old_weather):
    w = random.randint(1, 6)
    if w > x:
        n = random.randint(0, 3)
        old_weather.active = False
        tab[4].active = True
        x = 6
    else:
        x -= 1
    return x

class Elektrownia:
    def __init__(self, e_type, eko, koszt, dlugo):
        self.type = e_type
        self.active = False
        self.eko = eko
        self.koszt = koszt
        self.dlugo = dlugo

def ocen_efektywnosc(e, w):
    if e.type == "solarna":
        if w.type == "sundy": return 10
        if w.type == "windy": return 6
        if w.type == "cloudy": return 3
        if w.type == "rainy": return 2
    elif e.type == "wiatrowa":
        if w.type == "windy": return 10
        if w.type == "cloudy": return 7
        if w.type == "sundy": return 5
        if w.type == "rainy": return 5
    elif e.type == "wodna":
        if w.type == "rainy": return 9
        if w.type == "cloudy": return 7
        if w.type == "windy": return 6
        if w.type == "sundy": return 4
    elif e.type == "atomowa":
        return 7  # Same effectiveness for all weather
    elif e.type == "weglowa":
        if w.type == "cloudy": return 8
        if w.type == "rainy": return 7
        if w.type == "windy": return 5
        if w.type == "sundy": return 3
    elif e.type == "gazowa":
        if w.type == "sundy": return 8
        if w.type == "windy": return 7
        if w.type == "rainy": return 5
        if w.type == "cloudy": return 5
    return 3  # Default effectiveness

def paski(k, e, w):
    ekologia = (e.eko + e.dlugo) / 2 * 10
    print(f"Ekologia- {ekologia}%")
    energia = k * 10
    print(f"Energia- {energia}%")
    reputacja = k * (e.eko + e.dlugo) / 2 - e.koszt
    print(f"Reputacja- {reputacja}%")

    
class Button():
    def __init__(self, x, y, scale, image):
        self.x = x
        self.y = y
        self.scale = scale
        self.image = image


# def load_shared_lib(libname):
#     # We assume the shared library is present in the same directory as this script.
#     libpath = os.path.dirname(os.path.realpath(__file__))

#     # Append proper extension to library path (.dll for Windows, .so for Linux)
#     if sys.platform in ("win32", "cygwin"):
#         libpath = os.path.join(libpath, "%s.dll" % libname)
#     else:
#         libpath = os.path.join(libpath, "%s.so" % libname)

#     # Check that library exists (in same folder as this script).
#     if not os.path.exists(libpath):
#         print ("Error - could not find shared library %s; could not find file:" % libname)
#         print (" >> %s" % libpath)
#         return None

#     return ctypes.CDLL(libpath)


if __name__ == "__main__":
    import time
    import ctypes
    import pygame
    import os
    import random
    import sys
    wthr = [
        Weather("sunny"),
        Weather("cloudy"),
        Weather("windy"),
        Weather("rainy")
    ]
    cr_time = Time(0, 0, 0)
    time_speed = 2
    pause = False

    # os.add_dll_directory(os.getcwd())
    # dll_path = os.path.join(os.getcwd(), "pogoda.dll")
    # print(dll_path)
    # if not os.path.exists(dll_path):
    #     raise FileNotFoundError(f"{dll_path} not found")
    # # pogoda = ctypes.cdll.LoadLibrary(dll_path)
    # load_shared_lib("pogoda")

    pygame.init()
    X, Y = 1280, 720
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    gray = (39, 39, 39)
    grayer = (32, 32, 32)
    pygame.display.set_caption("Simulation")
    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)


    text_x, text_y = 60, 10


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
        if not pause:
            time.sleep(1 / abs(time_speed))
            cr_time.minute += 1
            cr_time.normalizetime()
        surf = (200, 200)
        # elif pause == True:
        pygame.draw.rect(display_surface, gray, pygame.Rect(30, 30, 60, 60), 2)
        time_text = font.render(cr_time.print_time(), True, white, blue)
        textRect = time_text.get_rect(center = (text_x, text_y))

        display_surface.fill(blue)
        display_surface.blit(time_text, textRect)
        pygame.display.flip()

    pygame.quit()

