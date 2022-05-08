# Dé importiamo le lib
import random
import sys
import pygame
from pygame.locals import *

# Peffò
window_width = 600
window_height = 430

# Altezza e Larghezza
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
framepersecond = 75
pipeimage = 'dif_hard/images/pipe.png'
background_image = 'dif_hard/images/background.png'
birdplayer_image = 'dif_hard/images/bird.png'
sealevel_image = 'dif_hard/images/base.png'


def flappygame():
	your_score = 0
	horizontal = int(window_width/5)
	vertical = int(window_width/2)
	ground = 0
	mytempheight = 100

	# Facciamo le pippe verdi
	first_pipe = createPipe()
	second_pipe = createPipe()

	# Listiamo le pippe in basso
	down_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[1]['y']},
		{'x': window_width+300-mytempheight+(window_width/2),
		'y': second_pipe[1]['y']},
	]

	# Listiamo le pippe in alto
	up_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[0]['y']},
		{'x': window_width+200-mytempheight+(window_width/2),
		'y': second_pipe[0]['y']},
	]

	# Pippe asse X
	pipeVelX = -4

	# Velocità uccellino
	bird_velocity_y = -9
	bird_Max_Vel_Y = 10
	bird_Min_Vel_Y = -8
	birdAccY = 1

	bird_flap_velocity = -8
	bird_flapped = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				if vertical > 0:
					bird_velocity_y = bird_flap_velocity
					bird_flapped = True

		# TVero
		# Se l'uccellino s'ammazza
		game_over = isGameOver(horizontal,
							vertical,
							up_pipes,
							down_pipes)
		if game_over:
			return

		# Controllar los punteggios
		playerMidPos = horizontal + game_images['flappybird'].get_width()/2
		for pipe in up_pipes:
			pipeMidPos = pipe['x'] + game_images['pipeimage'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos + 4:
				your_score += 1
				print(f"Il tuo punteggio è {your_score}")

		if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
			bird_velocity_y += birdAccY

		if bird_flapped:
			bird_flapped = False
		playerHeight = game_images['flappybird'].get_height()
		vertical = vertical + \
			min(bird_velocity_y, elevation - vertical - playerHeight)

		# Pippa a sinistra
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			upperPipe['x'] += pipeVelX
			lowerPipe['x'] += pipeVelX

		# Aggiung pippe
		# Maremma ciua
		if 0 < up_pipes[0]['x'] < 5:
			newpipe = createPipe()
			up_pipes.append(newpipe[0])
			down_pipes.append(newpipe[1])

		# Se la pippa va via levala
		if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
			up_pipes.pop(0)
			down_pipes.pop(0)

		# Lets blit our game images now
		window.blit(game_images['background'], (0, 0))
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			window.blit(game_images['pipeimage'][0],
						(upperPipe['x'], upperPipe['y']))
			window.blit(game_images['pipeimage'][1],
						(lowerPipe['x'], lowerPipe['y']))

		window.blit(game_images['sea_level'], (ground, elevation))
		window.blit(game_images['flappybird'], (horizontal, vertical))

		# Dé
		numbers = [int(x) for x in list(str(your_score))]
		width = 0

		# Luca Molinaro
		for num in numbers:
			width += game_images['scoreimages'][num].get_width()
		Xoffset = (window_width - width)/1.1

		# One Piece
		for num in numbers:
			window.blit(game_images['scoreimages'][num],
						(Xoffset, window_width*0.02))
			Xoffset += game_images['scoreimages'][num].get_width()

		# Naruto
		pygame.display.update()
		framepersecond_clock.tick(framepersecond)


def isGameOver(horizontal, vertical, up_pipes, down_pipes):
	if vertical > elevation - 25 or vertical < 0:
		return True

	for pipe in up_pipes:
		pipeHeight = game_images['pipeimage'][0].get_height()
		if(vertical < pipeHeight + pipe['y'] and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
			return True

	for pipe in down_pipes:
		if (vertical + game_images['flappybird'].get_height() > pipe['y']) and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
			return True
	return False


def createPipe():
	offset = window_height/3
	pipeHeight = game_images['pipeimage'][0].get_height()
	y2 = offset + \
		random.randrange(
			0, int(window_height - game_images['sea_level'].get_height() - 1.2 * offset))
	pipeX = window_width + 10
	y1 = pipeHeight - y2 + offset
	pipe = [
		# upper Pipe
		{'x': pipeX, 'y': -y1},

		# lower Pipe
		{'x': pipeX, 'y': y2}
	]
	return pipe


# program where the game starts
if __name__ == "__main__":

		# For initializing modules of pygame library
	pygame.init()
	framepersecond_clock = pygame.time.Clock()

	# Sets the title on top of game window
	pygame.display.set_caption("Up'n Down ver.220508.1 - hai.network")

	# Load all the images which we will use in the game

	# images for displaying score
	game_images['scoreimages'] = (
		pygame.image.load('dif_hard/images/0.png').convert_alpha(),
		pygame.image.load('dif_hard/images/1.png').convert_alpha(),
		pygame.image.load('dif_hard/images/2.png').convert_alpha(),
		pygame.image.load('dif_hard/images/3.png').convert_alpha(),
		pygame.image.load('dif_hard/images/4.png').convert_alpha(),
		pygame.image.load('dif_hard/images/5.png').convert_alpha(),
		pygame.image.load('dif_hard/images/6.png').convert_alpha(),
		pygame.image.load('dif_hard/images/7.png').convert_alpha(),
		pygame.image.load('dif_hard/images/8.png').convert_alpha(),
		pygame.image.load('dif_hard/images/9.png').convert_alpha()
	)
	game_images['flappybird'] = pygame.image.load(
		birdplayer_image).convert_alpha()
	game_images['sea_level'] = pygame.image.load(
		sealevel_image).convert_alpha()
	game_images['background'] = pygame.image.load(
		background_image).convert_alpha()
	game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(
		pipeimage).convert_alpha(), 180), pygame.image.load(
	pipeimage).convert_alpha())

	print("Benvenutx in Up'n Down! by hai.network")
	print("Premere la barra spaziatrice per iniziare...")

	# Here starts the main game

	while True:

		# sets the coordinates of flappy bird

		horizontal = int(window_width/5)
		vertical = int(
			(window_height - game_images['flappybird'].get_height())/2)
		ground = 0
		while True:
			for event in pygame.event.get():

				# if user clicks on cross button, close the game
				if event.type == QUIT or (event.type == KEYDOWN and \
										event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				# If the user presses space or
				# up key, start the game for them
				elif event.type == KEYDOWN and (event.key == K_SPACE or\
												event.key == K_UP):
					flappygame()

				# if user doesn't press anykey Nothing happen
				else:
					window.blit(game_images['background'], (0, 0))
					window.blit(game_images['flappybird'],
								(horizontal, vertical))
					window.blit(game_images['sea_level'], (ground, elevation))
					pygame.display.update()
					framepersecond_clock.tick(framepersecond)
