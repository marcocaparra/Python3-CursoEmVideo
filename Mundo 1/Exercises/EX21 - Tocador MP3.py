# EX21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# ----------------------------------------------------------
print('======== EXERCÍCIO 21 ========')

import pygame
pygame.init()
pygame.mixer.music.load('EX21 - VAI CORINTHIANS.mp3')
pygame.mixer.music.play()
pygame.event.wait()