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
    # Funkcja ocenia efektywność elektrowni na podstawie pogody
    effectiveness = {
        "solarna": {"sunny": 10, "windy": 6, "cloudy": 3, "rainy": 2},
        "wiatrowa": {"sunny": 5, "windy": 10, "cloudy": 7, "rainy": 5},
        "wodna": {"sunny": 4, "windy": 6, "cloudy": 7, "rainy": 9},
        "atomowa": {"sunny": 7, "windy": 7, "cloudy": 7, "rainy": 7},
        "weglowa": {"sunny": 3, "windy": 5, "cloudy": 8, "rainy": 7},
        "gazowa": {"sunny": 8, "windy": 7, "cloudy": 5, "rainy": 5},
    }
    return effectiveness[e.type][w.type]

def draw_bar(surface, x, y, width, height, value, max_value, color):
    pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 2)
    pygame.draw.rect(surface, color, (x, y, (width * value) / max_value, height))


if __name__ == "__main__":
    import time
    import pygame
    import random


    wthr = [
        Weather("sunny"),
        Weather("cloudy"),
        Weather("windy"),
        Weather("rainy")
    ]

    cr_time = Time(0, 0, 0)
    time_speed = 2
    pause = False
    music_playing = True
    elektrownia = Elektrownia("solarna", 7, 5, 8)

    pygame.init()
    pygame.mixer.init()
    X, Y = 1280, 720
    white = (255, 255, 255)
    blue = (0, 0, 128)
    pygame.display.set_caption("Simulation")


    pauza = pygame.image.load("Pauza.png")
    wyjscie = pygame.image.load("Exit.png")
    wyjscie_rect = wyjscie.get_rect(center=(X//2 + 150, Y//2 + 60))
    wyjscie_clicked = False
    dzwiek = pygame.image.load("Sound.png")
    Nie_dzwiek = pygame.image.load("Not_sound.png")
    dzwiek_rect = dzwiek.get_rect(center=(X//2 - 150, Y//2 + 60))


    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)

    pygame.mixer.music.load("muzyka.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    time_counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Pauza gry
                    pause = not pause
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wyjscie_rect.collidepoint(event.pos) and pause == True:  
                    wyjscie_clicked = True  
                elif dzwiek_rect.collidepoint(event.pos) and pause == True: 
                    if music_playing:
                        pygame.mixer.music.pause()
                        music_playing = False
                    else:
                        pygame.mixer.music.unpause()
                        music_playing = True
            
        # Czyszczenie ekranu
        display_surface.fill(blue)

        # Zmiana czasu co 1 sekundę (opóźnienie przy pomocy time_counter)
        if not pause:
            time_counter += clock.get_time()  # Zliczanie czasu, w milisekundach
            if time_counter >= 1000:  # Jeżeli minęła sekunda (1000ms)
                cr_time.minute += 1
                cr_time.normalizetime()
                time_counter = 0  # Resetowanie licznika czasu
            if cr_time.minute % 10 == 0:
                current_weather = random.choice(wthr)


        # Wyświetlanie czasu
        time_text = font.render(cr_time.print_time(), True, white, blue)
        textRect = time_text.get_rect(center=(X // 2, 50))
        display_surface.blit(time_text, textRect)
        weather_text = font.render(f"Weather: {current_weather.type}", True, (255, 255, 255))
        efficiency_text = font.render(
            f"Efficiency: {ocen_efektywnosc(elektrownia, current_weather)}%",
            True, (255, 255, 255)
        )
        display_surface.blit(time_text, (50, 50))
        display_surface.blit(weather_text, (50, 80))
        display_surface.blit(efficiency_text, (50, 110))
        # Rysowanie obrazu pauzy, jeśli gra jest w pauzie

        ekologia = (elektrownia.eko + elektrownia.dlugo) / 2 * 10
        reputacja = (ocen_efektywnosc(elektrownia, current_weather) * 10) - elektrownia.koszt

        draw_bar(display_surface, 50, Y - 100, X - 100, 30, ekologia, 100, (34, 139, 34))  # Ekologia
        draw_bar(display_surface, 50, Y - 150, X - 100, 30, reputacja, 100, (255, 165, 0))  # Reputacja 
        

        if pause:
            pauza_rect = pauza.get_rect(center=(X // 2, Y // 2))  # Wyśrodkowanie obrazu
            display_surface.blit(pauza, pauza_rect)
            display_surface.blit(wyjscie, wyjscie_rect)
            if music_playing:
                display_surface.blit(dzwiek, dzwiek_rect)
            else:
                display_surface.blit(Nie_dzwiek, dzwiek_rect)
            if wyjscie_clicked:
                running = False

        # Aktualizacja ekranu
        pygame.display.flip()
        clock.tick(30)  # Ustawienie liczby klatek na sekundę

    pygame.quit()


