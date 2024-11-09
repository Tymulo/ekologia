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
    c


    # import pygame
    # pygame.init()
    # X = 500
    # Y = 500
    # white = (255, 255, 255)
    # green = (0, 255, 0)
    # blue = (0, 0, 128)
    
    # display_surface = pygame.display.set_mode((X, Y))
    # pygame.display.set_caption("simulation")
    # font = pygame.font.Font('freesansbold.ttf', 32)
    # text = font.render(gtime(time_speed, pause), True, green, blue)
    # textRect = text.get_rect()
    # textRect.center = (X // 2, Y // 2)
    # exit = False
    # while not exit: 
    #     display_surface.fill(white)
    #     display_surface.blit(text, textRect)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT: 
    #             exit = True
    # pygame.display.update() 

