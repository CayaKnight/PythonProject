import pygame;

class Settings():
	def __init__(self):
		# Set the screen size dynamically
		display_info = pygame.display.Info();
		self.screen_size = (round((display_info.current_w*.6)), round((display_info.current_h*.7)));
		
		#prints screen size (this was mostly for my own use)
		print(self.screen_size)
		self.bg_color = (82,111,53);
		
		#sets default robot speed and heatlh
		self.robot_speed = 2;
		self.robot_health = 8;
		self.wave_num = 3
		
		#sets game to active
		self.game_active = True;
		self.game_lost = False
		
		self.chosen_turret = 1;
		
		#initializes battery amount
		self.total_battery = 0;
		
		#battery amount set for playtesting
		self.total_battery = 50000
		
		#keeps track of statistical values
		self.robots_killed = 0;
		self.bosses_killed = 0;
		self.battery_used = 0
		self.shooters_made= 0
		self.doubles_made= 0
		self.gatling_made= 0 
		self.toxic_made=0
		self.turrets_lost=0

		# square stuff
		self.squares = {
			"start_left": 200,
			"start_top": 200,
			"square_width": 80,
			"square_height": 79,
			"rows": [
				245,
				390,
				515,
				640,
				730
			]
		};
		
		self.highlighted_square = 0;
		
		#initializes robots on playing field
		self.robot_in_row = [
			0,
			0,
			0,
			0,
			0
		]	