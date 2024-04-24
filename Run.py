from General import *
from ArrayPreparing import *
from SortingAlgorithms import *

DISPLAY.fill((255, 255, 255))
main_arr = Unsorted() # only array used in entire run
main_arr.draw_arr()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pygame.draw.rect(DISPLAY, RED, pygame.Rect(0, 100, 250, SCREEN_HEIGHT - 100))
		
	Button("New Array", 24).button(
		30, 200, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		Unsorted().new_arr)

	pygame.draw.rect(DISPLAY, BLACK, pygame.Rect(0, 0, SCREEN_WIDTH, 100))
	Text("Pygame Sorting Algorithm Visualizer", YELLOW, (500, 30), 40).display()
	
	MultipleLine(
		["Welcome to the Pygame", "Algorithm Visualizer. ", "Press a button to start."], 
		BLUE, (10, 115), 23).display()
		
	Button("Merge Sort", 24).button(
		30, 350, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		MergeSort(main_arr.unsort_arr).button)

	Button("Insertion Sort", 24).button(
		30, 400, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		InsertionSort(main_arr.unsort_arr).button)

	Button("Quicksort", 24).button(
		30, 450, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		QuickSort(main_arr.unsort_arr).button)

	Button("Heap Sort", 24).button(
		30, 500, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		HeapSort(main_arr.unsort_arr).button)

	Button("Bubble Sort", 24).button(
		30, 550, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		BubbleSort(main_arr.unsort_arr).button)
		
	Button("Exit Program", 24).button(
		30, 700, 
		190, 50, 
		(0, 190, 0), (0, 255, 0), 
		quit)

	pygame.display.update()

pygame.quit()
