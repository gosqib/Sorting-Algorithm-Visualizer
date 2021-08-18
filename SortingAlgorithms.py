from typing import Any, Callable, List, Tuple, Union
from General import *
from ArrayPreparing import *
import pygame
pygame.init()

class MergeSort(Unsorted):
	def __init__(self, not_sor: List[int]) -> None:
		super().__init__(unsort_arr=not_sor)

	# taking as args cause slicing is more work
	def merge_sort(self, arr, lef, rig):
		if lef < rig:
			mid = (lef + rig) // 2
			self.merge_sort(arr, lef, mid)
			self.merge_sort(arr, mid + 1, rig)

			# the two separate array parts being merged
			lef_mid = lef
			mid_rig = mid + 1
			# sorted items in new list to have lazy end visualization
			temp = []
			while lef_mid <= mid and mid_rig <= rig:
				
				# colours to show which parts of arrays being compared
				self.col_arr[lef_mid] = RED
				self.col_arr[mid_rig] = RED
				self.renew()
				self.col_arr[lef_mid] = GREEN
				self.col_arr[mid_rig] = GREEN
				
				if arr[lef_mid] < arr[mid_rig]:
					temp.append(arr[lef_mid])
					lef_mid += 1

				else:
					temp.append(arr[mid_rig])
					mid_rig += 1

			while lef_mid <= mid:                
				temp.append(arr[lef_mid])
				lef_mid += 1

			while mid_rig <= rig:
				temp.append(arr[mid_rig])
				mid_rig += 1

			counter = 0
			# show final array by giving temp values to original array
			for i in range(lef, rig + 1): 
				arr[i] = temp[counter]
				counter += 1
				
				# show final array sort process
				self.col_arr[i] = BLUE
				self.renew()
				self.col_arr[i] = GREEN

	def button(self):
		self.merge_sort(self.unsort_arr, 0, len(self.unsort_arr) - 1)
		self.renew()



class InsertionSort(Unsorted):
	def __init__(self, unsort_arr: List[int]) -> None:
		super().__init__(unsort_arr=unsort_arr)

	def insertion_sort(self):
		for step in range(1, len(self.unsort_arr)):
			vault = self.unsort_arr[step]
			prev = step - 1

			while prev >= 0 and vault < self.unsort_arr[prev]:
				self.unsort_arr[prev + 1] = self.unsort_arr[prev]

				# change colour to show movement of items being compared
				self.col_arr[prev] = BLUE
				self.renew()
				self.col_arr[prev] = GREEN
				self.unsort_arr[prev] = vault
				prev -= 1
		

	# only for consistency of buttons
	def button(self):
		self.insertion_sort()
		# final renew to turn last blue line green (turned green after renew called)
		self.renew()



class QuickSort(Unsorted):
	def __init__(self, unsort_arr: List[int]) -> None:
		super().__init__(unsort_arr=unsort_arr)

	def partition(self, arr, low, high):
		pivot = arr[high]
		gre_ele = low - 1

		for i in range(low, high):
			# animation
			self.col_arr[i] = BLUE
			self.renew()
			self.col_arr[i] = GREEN

			if arr[i] <= pivot:
				gre_ele += 1
				arr[gre_ele], arr[i] = arr[i], arr[gre_ele]

		arr[gre_ele + 1], arr[high] = arr[high], arr[gre_ele + 1]

		return gre_ele + 1

	def quicksort(self, arr, low, high):
		if low < high:
			par = self.partition(arr, low, high)

			self.quicksort(arr, low, par - 1)
			self.quicksort(arr, par + 1, high)

	def button(self):
		self.quicksort(self.unsort_arr, 0, len(self.unsort_arr) - 1)
		# same reason as last button
		self.renew()



class HeapSort(Unsorted):
	def __init__(self, unsort_arr: List[int]) -> None:
		super().__init__(unsort_arr=unsort_arr)

	def heapify(self, arr, n, i):
		largest = i
		l = 2 * i + 1
		r = 2 * i + 2

		# animation
		self.col_arr[i] = BLUE
		self.renew()
		self.col_arr[i] = GREEN

		if l < n and arr[i] < arr[l]:
			largest = l

		if r < n and arr[largest] < arr[r]:
			largest = r

		if largest != i:
			arr[i], arr[largest] = arr[largest], arr[i]
			self.heapify(arr, n, largest)

	# no arguments cause it can take the main array from inside the class
	def heap_sort(self):
		n = len(self.unsort_arr)

		for i in range(n//2, -1, -1):
			self.heapify(self.unsort_arr, n, i)

		for i in range(n-1, 0, -1):
			self.unsort_arr[i], self.unsort_arr[0] = self.unsort_arr[0], self.unsort_arr[i]

			self.heapify(self.unsort_arr, i, 0)

	def button(self):
		self.heap_sort()
		self.renew()



class BubbleSort(Unsorted):
	def __init__(self, unsort_arr: List[int]) -> None:
		super().__init__(unsort_arr=unsort_arr)

	def bubble_sort(self):
		for i in range(len(self.unsort_arr)):

			swapped = False
			
			for j in range(len(self.unsort_arr) - i - 1):
				self.col_arr[j] = BLUE
				self.renew()
				self.col_arr[j] = GREEN
				if self.unsort_arr[j] > self.unsort_arr[j + 1]:
					self.unsort_arr[j], self.unsort_arr[j + 1] = self.unsort_arr[j + 1], self.unsort_arr[j]
					swapped = True

			if not swapped:
				break

	def button(self):
		self.bubble_sort()
		self.renew()



