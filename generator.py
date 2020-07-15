import pygame;
from pygame.sprite import Sprite;
from turret import Turret;

#creates a generator
class Generator(Turret):
	def __init__(self, screen, square,game_settings):
		pygame.sprite.Sprite.__init__(self)
		self.shoot_speed = 0;
		self.health = 5;
		
		self.image = pygame.image.load('images/Generator.png');
		self.width = 75;
		self.height = 100
		
		self.image = pygame.transform.scale(self.image, (self.width,self.height));
		self.screen = screen;
		self.square = square;
		self.name = "generator";
		self.can_shoot = False;
		self.can_make_battery = True;
		self.last_battery = 0;
		self.battery_speed = 5;
		self.battery_cost = 50;
		super(Generator, self).__init__();
		
		#creates batteries
	def make_battery(self,game_settings):
		game_settings.total_battery += 50;
	def change_image(self, should_shoot):
		if self.can_shoot:
			self.image = pygame.image.load('images/Generator.png');	