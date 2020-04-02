# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load('C:/Users/ianan/Music/Dreamland.mp3')
# pygame.mixer.music.play()
# input('Pressione ENTER para finalizar o programa! \n')

import playsound

p = input('Por favor digite o nome de um arquivo de música incluindo a sua extensão: ')
playsound.playsound('C:/Users/ianan/Music/{}'.format(p))
