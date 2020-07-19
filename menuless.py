import pygame
import sys
from settings import Settings
from square import Square
from background import Background
import game_functions as gf
from pygame.sprite import Group, groupcollide
from robot import Robot
from turret_icon import Turret_Icon
import time
from generator import Generator
import game

def main():
    game.create()

main()
