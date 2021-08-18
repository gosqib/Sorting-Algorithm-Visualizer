from typing import Any, Callable, List, Tuple, Union
from General import *
import pygame
import random
pygame.init()

# repeat of main loop
# used to reshow ui when refill calls a blank screen
def still_frame() -> None:
	pygame.draw.rect(DISPLAY, RED, pygame.Rect(0, 100, 250, SCREEN_HEIGHT - 100))
		
	Button("New Array", 24).button(
		30, 200, 
		190, 50, 
		(0, 190, 0), (0, 190, 0), 
		)

	pygame.draw.rect(DISPLAY, BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, 100))
	Text("Pygame Sorting Algorithm Visualizer", YELLOW, (500, 30), 40).display()
	
	MultipleLine(
		["Welcome to the Pygame", "Algorithm Visualizer. ", "Press a button to start."], 
		BLUE, (10, 115), 23).display()
		
	Button("Merge Sort", 24).button(
		30, 350, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)

	Button("Insertion Sort", 24).button(
		30, 400, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)

	Button("Quicksort", 24).button(
		30, 450, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)

	Button("Heap Sort", 24).button(
		30, 500, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)

	Button("Bubble Sort", 24).button(
		30, 550, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)
		
	Button("Exit Program", 24).button(
		30, 700, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		)



class Unsorted:
	# done as default to avoid creating new placeholder for brand new arrays vs reworking with old ones
	def __init__(self, unsort_arr: List[int] = [random.randint(5, SCREEN_HEIGHT - 105) for _ in range(150)]) -> None:
		self.unsort_arr = unsort_arr
		self.col_arr = [GREEN] * 150

	def create_arr(self) -> None:
		for i in range(len(self.unsort_arr)):
			self.unsort_arr[i] = random.randint(5, SCREEN_HEIGHT - 105)

	# drew separately from creation to avoid drawing a completely new array when 
	# called for display of algorithmic visualization steps
	def draw_arr(self) -> None:
		for i in range(len(self.unsort_arr)):
			pygame.draw.rect(DISPLAY, self.col_arr[i], pygame.Rect(350 + i * 7, 100, 5, self.unsort_arr[i]))

	def renew(self) -> None:
		DISPLAY.fill(WHITE)
		still_frame()
		self.draw_arr()
		# pygame.time.delay(10) # optional
		pygame.display.update()

	# for button
	def new_arr(self) -> None:
		self.create_arr()
		self.renew()



