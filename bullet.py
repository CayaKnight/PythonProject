import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
	def __init__(self,screen,turret,tick):
		super(Bullet, self).__init__();
		self.screen =  screen;
		self.screen_rect = self.screen.get_rect();
		self.image = pygame.image.load('./images/bullet.png');
		self.image = pygame.transform.scale(self.image, (30,30));
		self.rect = self.image.get_rect();
		self.rect.centerx = turret.rect.centerx;
		self.rect.top = turret.rect.top + 50;
		self.turret = turret
		self.tick = tick;
		self.name = ''

		self.factory_row = turret.factory_row;

		self.x = self.rect.x+25;
		self.y = self.rect.y;
		
		#set a bullet type to each turret
		if turret.name=='gatling':
			self.image = pygame.image.load('./images/bullet.png');
			self.image = pygame.transform.scale(self.image, (30,30));
			self.rect.top = turret.rect.top + 40;
		elif turret.name=='double':
			self.image = pygame.image.load('./images/double_bullet.png');
			self.image = pygame.transform.scale(self.image, (40,30));
			self.rect.top = turret.rect.top + 40;		
		elif turret.name=='toxic':
			self.image = pygame.image.load('./images/toxic_bullet.png');
			self.image = pygame.transform.scale(self.image, (30,30));
			self.name='super_bullet'
			
	#draws bullet
	def draw_me(self):
		self.screen.blit(self.image,self.rect);

	#updates the bullet's positions
	def update_me(self):
		self.x += 20 * 2;
		self.rect.x = self.x;
		
		#give the toxic turret its bullet spray ability
		if self.turret.name =='toxic':
			if self.tick % 3 ==1:
				self.rect.y += 5
			elif self.tick % 3 ==2:
				self.rect.y -= 5
			# elif self.tick % 3 ==0:	