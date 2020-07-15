import sys
import pygame;
import pygame_menu
from settings import Settings;
from square import Square;
from background import Background;
import game_functions as gf;
from pygame.sprite import Group, groupcollide
from robot import Robot;
from turret_icon import Turret_Icon;
import time
from generator import Generator
import gameover
pygame.init();
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("Chrome vs Rust")
def create():
	
	#create background
	background = Background(game_settings);
	
	#create icons for hotbar
	generator_icon = Turret_Icon(game_settings, 'Generator.png', 1, False)
	turretbot_icon = Turret_Icon(game_settings,'shooter_attack.png',2, True);
	double_icon = Turret_Icon(game_settings, 'double_attack.png', 3, False)
	gatling_icon = Turret_Icon(game_settings,'gatling_attack.png',4, False);
	toxic_icon = Turret_Icon(game_settings, 'toxic_attack.png', 5, False)
	icons = [generator_icon,turretbot_icon,gatling_icon,double_icon,toxic_icon]
	
	#initializes needed groups
	robots = Group();
	turrets = Group();
	squares = Group();
	bullets = Group()
	
	for h in range(0,5):
			for w in range(0,9):
					squares.add(Square(screen,game_settings,h, w));
					#add free generator to first square
					if h==0 and w==0:
							for square in squares:
									turrets.add(Generator(screen,square,game_settings))

	run_game(screen,game_settings,squares,background,turrets,bullets,icons,robots)
	
def run_game(screen,game_settings,squares,background,turrets,bullets,icons,robots):
	tick = 0;
	while 1:
		gf.check_events(screen,game_settings, squares, turrets,bullets,icons,tick);
		if game_settings.game_active:
		
		#spawns robots in relation to the current wave
		#lower waves only spawn low level robots
		#high waves spawn more robots and robots are harder to kill
		#amount of hard to kill robots increases with every wave
			tick += 1;
			if game_settings.wave_num ==1:
				if tick % 60 == 0:
					robots.add(Robot(screen,game_settings,1))
			elif game_settings.wave_num == 2:
				if tick % 30 == 0:
					robots.add(Robot(screen,game_settings,1));
				if tick % 150 == 0:
					robots.add(Robot(screen,game_settings,2));
			elif game_settings.wave_num == 3:
				if tick % 20 == 0:
					robots.add(Robot(screen,game_settings,1));
				if tick % 50 == 0:
					robots.add(Robot(screen,game_settings,2));								
				if tick % 250 == 0:
					robots.add(Robot(screen,game_settings,3));
			elif game_settings.wave_num == 4:
				if tick % 10 == 0:
					robots.add(Robot(screen,game_settings,1));
				if tick % 50 == 0:
					robots.add(Robot(screen,game_settings,2));								
				if tick % 100 == 0:
					robots.add(Robot(screen,game_settings,3));	
			elif game_settings.wave_num == 5:
				if tick % 5 == 0:
					robots.add(Robot(screen,game_settings,1));								
				if tick % 20 == 0:
					robots.add(Robot(screen,game_settings,2));
				if tick % 15 == 0:
					robots.add(Robot(screen,game_settings,3));
			elif game_settings.wave_num == 6:
				if tick % 5 == 0:
					robots.add(Robot(screen,game_settings,3));
			elif game_settings.wave_num == 7:
				if tick % 1000 == 0:
					robots.add(Robot(screen,game_settings,4));
					robots.add(Robot(screen,game_settings,4));
				if tick % 10 == 0:
					robots.add(Robot(screen,game_settings,3));								
				if tick % 30 == 0:
					robots.add(Robot(screen,game_settings,2));																		
				if tick % 20 == 0:
					robots.add(Robot(screen,game_settings,1));
			elif game_settings.wave_num >= 8:
				if tick % 300 ==0:
					robots.add(Robot(screen,game_settings,4));
				if tick % 400 ==0:
					robots.add(Robot(screen,game_settings,4));
				if tick % 1000 ==0:
					robots.add(Robot(screen,game_settings,4));		
				if tick % 5 == 0:
					robots.add(Robot(screen,game_settings,3));								
				if tick % 4 == 0:
					robots.add(Robot(screen,game_settings,2));																		
				if tick % 3 == 0:
					robots.add(Robot(screen,game_settings,1));
			#determine if a robot has been hit with a bullet
			robots_hit = groupcollide(robots, bullets, False, False);
			if tick % 1000 == 0:
				for bullet in bullets:
					bullets.remove(bullet);
					
			#if robot has been hit, removes some health
			for robot in robots_hit:
				if robot.factory_row == robots_hit[robot][0].factory_row or robots_hit[robot][0].name == "super_bullet" or robot.name=='boss':
					bullets.remove(robots_hit[robot][0]);
					if robots_hit[robot][0].name=='super_bullet':
						robot.hit(3);
					else: robot.hit(1);
					
					#if robot's health drops below 0, robot is removed from screen
					if(robot.health <= 0) and robot.name == 'boss':
						robots.remove(robot);
						game_settings.robot_in_row[robot.factory_row] -= 1;
						game_settings.bosses_killed += 1
					elif(robot.health <= 0)and robot.name != 'boss':
						robots.remove(robot);
						game_settings.robot_in_row[robot.factory_row] -= 1;
						game_settings.total_battery += 25
						game_settings.battery_used +=25
						game_settings.robots_killed += 1;
			for robot in robots:
				robot.moving = True;
			robots_attacking = groupcollide(turrets, robots, False, False);
			for turret in  robots_attacking:
				trashing_robots = robots_attacking[turret]
				for robot in trashing_robots:
					if not robot.name == 'boss' and robot.factory_row == turret.factory_row:						
						robot.moving = False
						if time.time() - robot.started_attacking > robot.damage_time:
							turret.robot_attack();
							robot.started_attacking = time.time();
							if turret.health <= 0:
								turrets.remove(turret);
								game_settings.turrets_lost+=1
							elif robot.name =='boss':
								turrets.remove(turret);
								game_settings.turrets_lost+=1
			if game_settings.game_lost == True:
								gameover.GameOver()
			#sets the condtions for level progression
			#if a certain amount of robots are kill, level increases
			if game_settings.robots_killed >= 5 and game_settings.wave_num==1:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 10 and game_settings.wave_num==2:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 25 and game_settings.wave_num==3:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 30 and game_settings.wave_num==4:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 40 and game_settings.wave_num==5:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 50 and game_settings.wave_num==6:
				game_settings.wave_num+=1
			if game_settings.robots_killed >= 60 and game_settings.wave_num==7 and game_settings.bosses_killed>=1:
				game_settings.wave_num+=1
			if game_settings.robots_killed == ((game_settings.robots_killed)+ 30) and game_settings.wave_num>=8:
				game_settings.wave_num+=1
			gf.update_screen(screen,game_settings,background,robots,squares,turrets,bullets,tick,icons,game_settings.wave_num);
		pygame.display.flip();