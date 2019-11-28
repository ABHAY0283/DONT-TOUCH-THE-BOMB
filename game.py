import os
import pygame
import pygame.locals

from button import *
import globs

width  = 864
height = 480

images = {
	'player': pygame.image.load(os.path.join("data","sprites","player.png")),

	'sky': pygame.image.load(os.path.join("data","tiles","sky.png")),
	'border': pygame.image.load(os.path.join("data","tiles","border.png"))
}

globs.init()

def grid(x,y):
	return (x*32,y*32)

# Temporary class for testing purposes.
class drawHelper:
	@staticmethod
	def frame(screen):
		#N
		for x in range(27):
			screen.blit(images['border'], grid(x,0))
		#S
		for x in range(27):
			screen.blit(images['border'], grid(x,14))
		#W
		for y in range(1,14):
			screen.blit(images['border'], grid(0,y))
		#E
		for y in range(1,14):
			screen.blit(images['border'], grid(26,y))

	@staticmethod
	def sky(screen):
		#sky
		for x in range(27):
			for y in range(15):
				screen.blit(images['sky'], (grid(x,y)))


class Player(pygame.sprite.Sprite):
	def __init__(self, pos = grid(1,1)):
		self.speed = 8
		self.xspeed = 0
		self.yspeed = 0
		self.rect = images['player'].get_rect(topleft=pos)

	def event(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.yspeed = 0 - self.speed
		if keys[pygame.K_DOWN]:
			self.yspeed = self.speed
		if keys[pygame.K_LEFT]:
			self.xspeed = 0 - self.speed
		if keys[pygame.K_RIGHT]:
			self.xspeed = self.speed

	def move(self):
		self.rect.centerx += self.xspeed
		self.rect.centery += self.yspeed
		
		if not self.xspeed == 0:
			if self.xspeed > 0:
				self.xspeed -= 1
			else:
				self.xspeed += 1
		if not self.yspeed == 0:
			if self.yspeed > 0:
				self.yspeed -= 1
			else:
				self.yspeed += 1

	def draw(self, screen):
		screen.blit(images['player'], self.rect)


def main():
	print("game init")
	pygame.init()
	icon = pygame.image.load("icon_32x32.png")
	pygame.display.set_icon(icon)
	pygame.display.set_caption("pygame window")

	screen = pygame.display.set_mode((width, height))
	screen.fill((30,30,30))

	fontFps = pygame.font.Font(None, 30)
	font = pygame.font.Font(globs.fntSavate, 48)

	button1 = startBtn(grid(11,5), "Start")
	button2 = exitBtn(grid(11,8), "Exit")

	running = True

	clock = pygame.time.Clock()

	player = Player(grid(2,2))

	pygame.mixer.init()
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.load(os.path.join('data','music','titlescreen_final.ogg'))
	pygame.mixer.music.play(-1)

	# main loop
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			button1.event_handler(event)
			button2.event_handler(event)

		if globs.inGame:
			#sky
			drawHelper.sky(screen)

			#player
			player.event()
			player.move()
			player.draw(screen)

			#ground
			drawHelper.frame(screen)
		else:
			#sky
			drawHelper.sky(screen)

			#player
			screen.blit(images['player'], grid(2,11))

			#ground
			drawHelper.frame(screen)

			#title
			title_shadow = font.render("DONT TOUCN THE BOMB", True, pygame.Color(50,50,50))
			title_size_x = 578
			title_size_y = 49
			title_shadow = pygame.transform.smoothscale(title_shadow, (title_size_x // 5,title_size_y // 5))
			title_shadow = pygame.transform.smoothscale(title_shadow, (title_size_x, title_size_y))
			screen.blit(title_shadow, (155,60))
			title = font.render("DONT TOUCH THE BOMB", True, pygame.Color('black'))
			screen.blit(title, (145,50))
			button1.draw(screen)
			button2.draw(screen)

		fps = fontFps.render(str(int(clock.get_fps())), True, pygame.Color('white'))
		screen.blit(fps, (5, 5))

		pygame.display.flip()
		clock.tick(60)
	#end


if __name__ == "__main__":
	main()
