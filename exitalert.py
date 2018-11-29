import pygame, my
from ui import ui, label, button
from menu import Menu


class ExitAlert(ui.UI):
	def __init__(self, screen):
		ui.UI.__init__(self, screen)

		copy = screen.copy()
		self.background = pygame.Surface((my.SCREEN_WIDTH, my.SCREEN_HEIGHT), flags=pygame.SRCALPHA)
		self.background.blit(copy, (0, 0))
		self.background.fill((my.LIGHT_GREY[0], my.LIGHT_GREY[1], my.LIGHT_GREY[2], 10))

		self.addWidget(label.Image([0, 0], self.background, centralization=ui.RIGHT | ui.BOTTOM))
		self.addWidget(button.ImageButton(lambda: self.quit(),
										  [my.SCREEN_HALF_WIDTH, my.SCREEN_HALF_HEIGHT - 60],
										  text="Sair",
										  image_surface=ui.IMAGES['button'],
										  image_pressed=ui.IMAGES['button_pressed']))
		self.addWidget(button.ImageButton(lambda: self.backGame(),
										  [my.SCREEN_HALF_WIDTH, my.SCREEN_HALF_HEIGHT],
										  text="Voltar ao jogo",
										  image_surface=ui.IMAGES['button'],
										  image_pressed=ui.IMAGES['button_pressed']))

		self.next = self

	def update(self, events):
		super().update(events)

		return self.next

	def quit(self):
		pygame.quit()

	def backGame(self):
		self.next = Menu(self.screen)
