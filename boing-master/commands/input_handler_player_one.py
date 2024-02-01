
import pygame
import sys
from commands.move_up_command import MoveUpCommand
from commands.move_down_command import MoveDownCommand
from pygame import K_UP, KEYUP, KEYDOWN, K_z, K_a, K_DOWN


class InputHandlerPlayerOne:

    k_up_ = MoveUpCommand()
    k_down_ = MoveDownCommand()

    def handle(self, actor):
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                if event.key == K_UP or K_a:
                    self.k_up_.execute(actor)
                elif event.key == K_DOWN or K_z:
                    self.k_down_.execute(actor)

            if event.type == KEYUP:
                actor.stop()