import os
import pygame
import globs

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class Button:
	def __init__(self, position, text):
		# create 3 images
		self.images = [
			pygame.image.load(os.path.join("data","menu","button.png")),
			pygame.image.load(os.path.join("data","menu","buttonHover.png")),
			pygame.image.load(os.path.join("data","menu","buttonClick.png")),
		]

		self.size = (128,64)

		self.menuBtnFnt = pygame.font.Font(globs.fntSavate, 18)
		self.captionSurf = self.menuBtnFnt.render(text, True, BLACK)
		self.captionRect = self.captionSurf.get_rect()
		self.captionRect.center = int(position[0] + self.size[0] / 2), int(position[1] + self.size[1] / 2)

		# get image size and position
		self.rect = pygame.Rect(position, self.size)

		# select first image
		self.index = 0

	def draw(self, screen):
		# draw selected image
		screen.blit(self.images[self.index], self.rect)
		screen.blit(self.captionSurf, self.captionRect)

	def event_handler(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if self.rect.collidepoint(event.pos):
					self.index = 2

		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if self.rect.collidepoint(event.pos):
					self.index = 1
					self.onClick()

		if event.type == pygame.MOUSEMOTION:
			if self.rect.collidepoint(event.pos):
				self.index = 1
			else:
				self.index = 0

	def onClick(self):
		raise UserWarning("Button doesn't have onClick function")


class startBtn(Button):
	def onClick(self):
		globs.inGame = True

class exitBtn(Button):
	def onClick(self):
		exit()