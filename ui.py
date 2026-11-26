import pygame
#needed to create the temproary latex images whcih will be blitted to the screen
import matplotlib.pyplot as pyplt
import math

formula = r"$x = 5 \times 2^{2}$"
fig = pyplt.figure()
fig.text(0.1, 0.5, formula, fontsize=24)
fig.savefig("TeX.png")
pyplt.close(fig)

pygame.init()
x=1000
y=750
canvas=pygame.display.set_mode((x, y))
pygame.display.set_caption("OpenSpeech-NEA")
b=pygame.image.load("TeX.png").convert()
canvas.blit(b,(0,0))
pygame.display.flip()
Run=True
while Run==True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            Run=False
pygame.quit()
