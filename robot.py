import pygame;
from pygame.sprite import Sprite;
from random import randint;
# from sounds import sounds
class Robot(Sprite):
	def __init__(self, screen, game_settings, level):
		super(Robot,self).__init__();
		self.speed = game_settings.robot_speed;
		self.health = game_settings.robot_health;
		self.level = level
		self.image = pygame.image.load('./images/r1_idle.png')
		self.factory_row = randint(0,4);
		self.name = ''

		self.image = pygame.transform.scale(self.image,(80,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();

		self.rect.centery = game_settings.squares["rows"][self.factory_row]
		self.rect.right = self.screen_rect.right;
		game_settings.robot_in_row[self.factory_row] += 1;
		self.game_settings = game_settings
		self.x = float(self.rect.x);
		self.moving = True;
		self.started_attacking = 0;
		self.damage_time = 2;
		
		if self.level==2:
			self.image = pygame.image.load('./images/r2_walk1.png')
			self.image = pygame.transform.scale(self.image,(110,120));
			self.speed = self.speed + 3
			self.health = 4 * self.health
		elif self.level==3:
			self.image = pygame.image.load('./images/r3_walk1.png')
			self.image = pygame.transform.scale(self.image,(110,120));
			self.speed = self.speed * 4
			self.health = self.health * 8
		elif self.level==4:
			self.image = pygame.image.load('./images/boss.png')
			self.image = pygame.transform.scale(self.image,(200,315));
			self.health = self.health * 15
			temp_tuple=(1,3)
			self.factory_row = temp_tuple[(randint(0,1))]
			temp_tuple2 = (0.5, 0.7, 0.9, 1, 1.3, 1.5, 2)
			self.speed = temp_tuple2[(randint(0,6))]
			self.name = 'boss'
			# self.rect.right -= 500
		
		else:
			self.image = pygame.transform.scale(self.image,(110,120));		
	
	def update_me(self):
		#if self.level ==4 and self.health <= 300:
		#	self.image = pygame.image.load('./images/boss1-2.png')
		#	self.image = pygame.transform.scale(self.image,(393,414));
		if self.health <= 1:
			if self.level==2:
				self.image = pygame.image.load('./images/r2_death.png')
				self.image = pygame.transform.scale(self.image,(140,110));
			elif self.level==3:
				self.image = pygame.image.load('./images/r3_death.png')
				self.image = pygame.transform.scale(self.image,(140,110));				
			elif self.level==1:
				self.image = pygame.image.load('./images/r1_death.png')
				self.image = pygame.transform.scale(self.image,(140,110));
				self.rect.centery = self.game_settings.squares["rows"][self.factory_row]
		else:
			if self.moving:
				self.x -= self.speed * 1;
				self.rect.x = self.x;			
				if self.x % 3 == 1:
					if self.level==2:
						self.image = pygame.image.load('./images/r2_walk2.png')
						self.image = pygame.transform.scale(self.image,(110,120));
					elif self.level==3:
						self.image = pygame.image.load('./images/r3_walk2.png')
						self.image = pygame.transform.scale(self.image,(110,120));	
					elif self.level==1:
						self.image = pygame.image.load('./images/r1_walk1.png')
						self.image = pygame.transform.scale(self.image,(110,120));
				else:
					if self.level==2:
						self.image = pygame.image.load('./images/r2_walk3.png')
						self.image = pygame.transform.scale(self.image,(110,120));
					elif self.level==3:
						self.image = pygame.image.load('./images/r3_walk3.png')
						self.image = pygame.transform.scale(self.image,(110,120));	
					elif self.level==1:
						self.image = pygame.image.load('./images/r1_walk2.png')
						self.image = pygame.transform.scale(self.image,(110,120));

			else: 
				self.x += 1;
				self.rect.x = self.x;
				if self.x % 3 == 1:
					if self.level==2:
						self.image = pygame.image.load('./images/r2_walk1.png')
						self.image = pygame.transform.scale(self.image,(110,120));
					elif self.level==3:
						self.image = pygame.image.load('./images/r3_walk1.png')
						self.image = pygame.transform.scale(self.image,(110,120));	
					elif self.level==1:
						self.image = pygame.image.load('./images/r1_walk2.png')
						self.image = pygame.transform.scale(self.image,(110,120));
				else:
					# self.image = pygame.image.load('./images/r1_walk1.png')
					# self.image = pygame.transform.scale(self.image,(110,120));			
					if self.level==2:
						self.image = pygame.image.load('./images/r2_walk3.png')
						self.image = pygame.transform.scale(self.image,(140,120));
					elif self.level==3:
						self.image = pygame.image.load('./images/r3_walk3.png')
						self.image = pygame.transform.scale(self.image,(140,120));	
					elif self.level==1:
						self.image = pygame.image.load('./images/r1_walk3.png')
						self.image = pygame.transform.scale(self.image,(140,120));

	def draw_me(self):
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		self.health -= damage;
		#ouch_sound = pygame.mixer.Sound('./images/attacked.wav')
		#ouch_sound.play();
		#if self.health == 1:
		#	bg_music = pygame.mixer.Sound('./images/ouch.wav');
		#	bg_music.play();
		if self.level == 1 and self.health > 1:
			self.x += 1;
		elif self.level == 2 and self.health > 1:
			self.x += 1;
		if self.level == 4:
			print (self.health)