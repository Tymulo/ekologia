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

if __name__ == "__main__":
    import time
    import ctypes
    import pygame

    cr_time = Time(0, 0, 0)
    time_speed = 2
    pause = False

    pygame.init()
    X, Y = 500, 500
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    pygame.display.set_caption("Simulation")
    display_surface = pygame.display.set_mode((X, Y))
    font = pygame.font.Font('freesansbold.ttf', 18)

    text_x, text_y = 250, 250

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
        # else:
        #     pygame.draw.rect()
        time_text = font.render(cr_time.print_time(), True, white, blue)
        textRect = time_text.get_rect(center = (text_x, text_y))

        display_surface.fill(blue)
        display_surface.blit(time_text, textRect)
        pygame.display.flip()

    pygame.quit()

