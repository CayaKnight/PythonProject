import pygame
from pygame.sprite import Sprite

#creates icons for the hotbar on screen
class Turret_Icon(Sprite):
	def __init__(self,game_settings,icon,slot,chosen):
		super(Turret_Icon, self).__init__();		
		self.image = pygame.image.load('./images/'+icon);
		if icon == 'Generator.png':
			self.image = pygame.transform.scale(self.image,(80,82));
		elif icon == 'shooter_attack.png':
			self.image = pygame.transform.scale(self.image,(80,82))			
		else: self.image = pygame.transform.scale(self.image,(80,82));	
		self.rect = self.image.get_rect();
		self.rect.left = 350+(110 * slot);
		self.rect.top = 40;
		self.slot = slot;
		self.chosen = chosen;