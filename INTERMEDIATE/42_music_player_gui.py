"""
42: Music Player GUI
A basic audio GUI built with pygame mixer.
"""
def init_music_player():
    try:
        import pygame
        pygame.mixer.init()
        print("Pygame audio mixer initialized.")
    except ImportError:
        print("pygame not installed.")

if __name__ == "__main__":
    init_music_player()
