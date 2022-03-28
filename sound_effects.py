#! /usr/bin/python3

import pygame
from pygame.locals import *

class SoundEffects:
    """Manage Alien Invasion sound effects."""
    def __init__(self, ai_game):
        """Initialize sound effects."""
        self.ai_game = ai_game
        self.screen = ai_game.screen

        # Initialize 44KHz 16-bit stereo sound
        pygame.mixer.pre_init(44100, 16, 2, 1024*4)
        pygame.init()
        pygame.mixer.set_reserved(2)
        self.reserved_channel_0 = pygame.mixer.Channel(0)
        self.reserved_channel_1 = pygame.mixer.Channel(1)

        # Load the sound file
        self.fire_sound = pygame.mixer.Sound("sounds/fire.wav")
        self.theme_sound = pygame.mixer.Sound("sounds/intro_theme.ogg")
        self.bg_theme = pygame.mixer.Sound("sounds/background.ogg")

    def firing_sound(self):
        """Play the sound when a bullet is fired."""
        self.fire_sound.set_volume(4.5)
        playing_fire = self.fire_sound.play()
        self.reserved_channel_1.play(self.fire_sound)

    def intro_sound(self):
        """Play the intro theme sound."""
        self.theme_sound.set_volume(3.0)
        playing_intro = self.theme_sound.play(-1)

    def bg_sound(self):
        """Play the background music."""
        self.bg_theme.set_volume(3.0)
        playing_bg = self.bg_theme.play(-1)
