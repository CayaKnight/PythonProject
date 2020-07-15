import pygame;
from pygame.sprite import Sprite

class Square(Sprite):
	def __init__(self, screen, game_settings,h,w):
		super(Square, self).__init__();
		self.screen = screen
		self.screen_rect = self.screen.get_rect();

		self.width = game_settings.squares["square_width"]+20;
		self.height = game_settings.squares["square_height"]+30;
		self.rect = pygame.Rect(0,0,self.width, self.height);

		# h is the number of heights to use
		# w is the number of widths to use
		self.rect.left = (w * self.width) + game_settings.squares["start_left"];
		self.rect.top = (h * self.height) + game_settings.squares["start_top"];

		self.square_number = (h*9) + (w+1);
		self.row_number = h;
		self.column = w;
		
		#creates empty square
		self.turret_here = False;