import pygame
from pyvidplayer2 import Video, VideoPlayer


# ------------------------ Setup Image Database ------------------------------


#----------------------- Game Setup -----------------------------#

# General Game Setup
pygame.init()
running = True
clock = pygame.time.Clock()

# Game Screen (width,height)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Auausalakau")


# ----------------------- Load Media Sources ---------------------#
player = VideoPlayer(Video("Videos/title screen.mp4"), (0,0,width,height), interactable=False)

#-------------------- Main  -----------------------------#

while running:

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    player.get_video().toggle_pause()
                case pygame.K_l:
                    player.loop = True
                case pygame.K_1:
                    player.queue(Video("Videos/title screen.mp4"))
                    player.skip()
                case pygame.K_2:
                    player.queue(Video("Videos/scene1.mp4"))
                    player.skip()
                case pygame.K_3:
                    player.queue(Video("Videos/scene2.mp4"))
                    player.skip()
                case pygame.K_4:
                    player.queue(Video("Videos/scene2_alternative.mp4"))
                    player.skip()
                case _:
                    pass
                

    # RENDER YOUR GAME HERE
    print("Loop: ", player.loop)

    # update() the display to put your work on screen
    player.update(pygame.event.get())
    player.draw(screen)
    pygame.display.update()

    clock.tick(120)  # limits FPS to 60

player.close()
pygame.quit()