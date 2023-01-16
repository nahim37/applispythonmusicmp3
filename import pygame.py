import pygame
file = "C:/Users/alim/Desktop/Projet python/Mymusic.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()