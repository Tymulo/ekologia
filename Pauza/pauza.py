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
        return f"Day: {self.day} {self.hour:02}:{self.minute:02}"


if __name__ == "__main__":
    import time
    import pygame

    # Obiekt czasu
    cr_time = Time(0, 0, 0)
    time_speed = 2  # Można dostosować prędkość zmiany czasu
    pause = False
    music_playing = True  # Flaga do kontrolowania muzyki

    # Inicjalizacja Pygame
    pygame.init()
    pygame.mixer.init()
    X, Y = 1280, 720
    white = (255, 255, 255)
    blue = (0, 0, 128)
    pygame.display.set_caption("Simulation")

    # Obrazy
    pauza = pygame.image.load("Pauza.png")
    wyjscie = pygame.image.load("Exit.png")
    wyjscie_rect = wyjscie.get_rect(center=(X//2 + 150, Y//2 + 60))
    wyjscie_clicked = False
    dzwiek = pygame.image.load("Sound.png")
    Nie_dzwiek = pygame.image.load("Not_sound.png")
    dzwiek_rect = dzwiek.get_rect(center=(X//2 - 150, Y//2 + 60))

    # Powierzchnia i czcionka
    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)

    # Inicjalizacja muzyki
    pygame.mixer.music.load("muzyka.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Muzyka w pętli

    clock = pygame.time.Clock()
    time_counter = 0  # Zmienna do liczenia upływu czasu

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

        # Wyświetlanie czasu
        time_text = font.render(cr_time.print_time(), True, white, blue)
        textRect = time_text.get_rect(center=(X // 2, 50))
        display_surface.blit(time_text, textRect)

        # Rysowanie obrazu pauzy, jeśli gra jest w pauzie
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



