import pygame;
from pygame.sprite import Sprite;
from square import Square

#creates the turret class
#all assets that can be used by the player connect to this class
class Turret(Sprite):
	def __init__(self):
		super(Turret,self).__init__();
		self.screen_rect = self.screen.get_rect();
		self.image = pygame.transform.scale(self.image, (112,109));
		self.rect = self.image.get_rect();
		
		#positions turret with the square
		self.rect.left = self.square.rect.left+15;
		self.rect.top = self.square.rect.top;
		self.factory_row = self.square.row_number
		self.rect.centerx = self.square.rect.centerx

		self.last_shot = 0;
		self.last_battery = 0;
		self.battery_speed = 5;
	
	#creates a turret on screen
	def draw_me(self):
		self.screen.blit(self.image, self.rect);
	
	#if turret is attacked by robot, loses health
	def robot_attack(self):
		self.health -= 1;		