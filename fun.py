#Shuxin's snake game
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.graphics import *

from kivy.clock import Clock


import numpy
import pandas

import random 
import math









class Snake():

	def __init__(self, **kwargs):
		
		self.window_x = kwargs['window'].size[0]
		self.window_y = kwargs['window'].size[1]
		self.center_x = self.window_x/2
		self.center_y = self.window_y/2


		self.draw_pos = [self.center_x, self.center_y]

		self.radius = 15
		self.velocity = [0,0]
		self.food_eaten = 1


		#self.body = {'0' : self.draw_pos}

		self.body = [self.draw_pos]
		




class Food():

	def __init__(self, **kwargs):

		self.window_x = kwargs['window'].size[0]
		self.window_y = kwargs['window'].size[1]
		self.center_x = self.window_x/2
		self.center_y = self.window_y/2


		self.draw_pos = [0,0]
		self.draw_pos[0]=random.randint(0,self.window_x)
		self.draw_pos[1]=random.randint(0,self.window_y)

		self.radius = 15










class Sandbox_Widget(BoxLayout):

	def __init__(self,  window, **kwargs):
		super(Sandbox_Widget, self).__init__(**kwargs)
		
		self.window=window


		Clock.schedule_interval(self.update, 1/30)




		#Window.bind(mouse_pos=self.mouse_pos)
		self.window_x_edge = window.size[0]
		self.window_y_edge = window.size[1]
		self.center = [window.size[0]/2, window.size[1]/2]
		self.window.bind(mouse_pos=self.on_motion)


		self.snake = Snake(window=window) 
		self.food = Food(window=window)
		
		


	




	def check_food_collision(self,  obj1, obj2):

		dx = obj1.draw_pos[0] - obj2.draw_pos[0]
		dy = obj1.draw_pos[1] - obj2.draw_pos[1]
		sum_radius = obj1.radius + obj2.radius

		distance_between = math.sqrt((dx)**2 + (dy)**2)


		if distance_between <= sum_radius:

			return True
			



		
		


	def update(self, time_since_call):
		print(self.snake.body)
		


		self.canvas.clear()
		with self.canvas:


			#draw the food
			Color(1,1,1,1)
			Line(circle=(self.food.draw_pos[0], self.food.draw_pos[1], self.food.radius))


			Color(1,0,0,.9)
		
			
			#print("position before update", next_position)

			# self.snake.body[0][0] += self.snake.velocity[0]
			# self.snake.body[0][1] += self.snake.velocity[1]

			
			
			

			x = self.snake.body[0][0] + self.snake.velocity[0]
			y = self.snake.body[0][1] + self.snake.velocity[1]

			self.snake.draw_pos[0] = x
			self.snake.draw_pos[1] = y
			#print("y", y)

			self.snake.body[0]=[x,y]
			next_position = self.snake.body[0]




			#print("posiotion after update", self.snake.body[0])
			Line(circle=(self.snake.body[0][0], self.snake.body[0][1], self.food.radius))

			if self.check_food_collision(self.snake, self.food):
				
						
						
				x = self.snake.body[-1][0]
				y = self.snake.body[-1][1]
		
				self.snake.body.append([x, y])
				#self.snake.body[str(self.snake.food_eaten )] = [x, y] #use some angle to determine how to offsaet the new body part
				

				del self.food
				self.food = Food(window=self.window)


				#self.snake.food_eaten += 1


				#Line(circle=(self.snake.body[0][0], self.snake.body[0][1], self.food.radius))




			count = 1
			for body_part in self.snake.body[1:]:

				# print(self.snake.body[count])
				# print(next_position)

				tmp = body_part
				self.snake.body[count] = [(next_position[0]+self.snake.velocity[0]*5), (next_position[1]+self.snake.velocity[1]*5)]
				count += 1
				#self.snake.body[count] = body_part

				
				#body_part = next_position
				next_position = tmp
	
				
				

				Line(circle=(body_part[0], body_part[1], self.food.radius))

					
				
					


			
		



		


		

			
			


				

			



	def on_motion(self, window, pos): 
		pass
	



	def on_touch_down(self, touch): 
		pass

	def clear_canvas(self):
		self.canvas.clear()

	def new_color(self):
		self.color[0] = random.uniform(0, 1)
		self.color[1] = random.uniform(0, 1)
		self.color[2] = random.uniform(0, 1)

	def moveleft(self):
		self.snake.velocity[0] = -5
		self.snake.velocity[1] = 0

	def moveright(self):
		self.snake.velocity[0] = 5
		self.snake.velocity[1] = 0

	def moveup(self):
		self.snake.velocity[1] = 5
		self.snake.velocity[0] = 0

	def movedown(self):
		self.snake.velocity[1] = -5
		self.snake.velocity[0] = 0
 
	def pause(self):
		self.snake.velocity[1] = 0
		self.snake.velocity[0] = 0











































# class Snake():

# 	def __init__(self, **kwargs):




		# self.object_number = kwargs['count']

		# self.draw_pos = [0, 0]
		# self.draw_pos[0], self.draw_pos[1]  = kwargs['position']
	
		# self.color = [0,0,0,0]
		# self.color[0] = random.uniform(0, 1)
		# self.color[1] = random.uniform(0, 1)
		# self.color[2] = random.uniform(0, 1)
		# self.color[3] = random.uniform(0, 1)


		# self.radius = 30 
		# self.half_radius = self.radius/2
		# self.growing = True
		# self.collision = False

		# self.moving_angle = 0
		# self.distance_between = 0

		# self.velocity = [-5, 5]
		# self.acceleration = [random.uniform(-1, 1) * 5 , random.uniform(-1, 1) * 5 ]

		# #self.friction 





# class Sandbox_Widget(BoxLayout):

# 	def __init__(self,  window, **kwargs):
# 		super(Sandbox_Widget, self).__init__(**kwargs)
		
# 		self.window=window

# 		Clock.schedule_interval(self.update, 1/60)


# 		#print(self.window)



# 		#Window.bind(mouse_pos=self.mouse_pos)
# 		self.window_x_edge = window.size[0]
# 		self.window_y_edge = window.size[1]
# 		self.center = [window.size[0]/2, window.size[1]/2]

# 		self.window.bind(mouse_pos=self.on_motion)
# 		self.draw_pos = [0,0]



# 		#self.circle_radius = 30


# 		self.number_of_objects = 0
# 		self.drawing_container = []



# 	def check_collision(self, obj1, obj2):


# 		dx = obj1.draw_pos[0] - obj2.draw_pos[0]
# 		dy = obj1.draw_pos[1] - obj2.draw_pos[1]

# 		distance_between = math.sqrt((dx)**2 + (dy)**2)

# 		if distance_between < (obj1.radius + obj2.radius):
# 			obj2.collision = True
# 			obj1.collision = True

# 			angle = math.atan2(dy, dx)
# 			angle_in_degree = (angle * 180/math.pi)
# 			obj1.moving_angle = angle_in_degree - 180
# 			obj2.moving_angle = angle_in_degree - 180


# 			obj1.distance_between = distance_between

# 			obj1.velocity[0] *= -0.8
# 			obj1.velocity[1] *= -0.8
# 			print(obj1.velocity)
# 			if obj1.velocity[0] <0.1:

# 				obj1.velocity[0] = 5
# 				obj1.velocity[1] = -5

			




# 		else:
# 			obj2.collision = False
# 			obj1.collision = False


# 	def update(self, time_since_call):

# 		#self.rect_pos[1] += 1
# 		#self.rect_pos[0] += 1


# 		self.canvas.clear()
# 		with self.canvas:

# 			for first_object in self.drawing_container:

# 				#update position
# 				first_object.draw_pos[0] += first_object.velocity[0]
# 				first_object.draw_pos[1] += first_object.velocity[1]

# 				# first_object.velocity[0] += first_object.acceleration[0]
# 				# first_object.velocity[1] += first_object.acceleration[1]



# 				#check the bounds of the window so objects stay in window
# 				if first_object.draw_pos[0] > self.window_x_edge-(first_object.radius):
# 					first_object.velocity[0] *= -1

# 				if first_object.draw_pos[1] > self.window_y_edge-(first_object.radius):
# 					first_object.velocity[1] *= -1

# 				if first_object.draw_pos[0] < 0 + (first_object.radius):
# 					first_object.velocity[0] *= -1

# 				if first_object.draw_pos[1] < 0 + (first_object.radius):
# 					first_object.velocity[1] *= -1



# 			# 	if first_object.collision == True:
# 			# 		first_object.draw_pos[0] -=   2 * math.cos(first_object.moving_angle)
# 			# 		first_object.draw_pos[1] -=   2 *  math.sin(first_object.moving_angle)
# 					#first_object.collision = False

# 					# first_object.draw_pos[0] +=   2 * math.cos(first_object.moving_angle)
# 					# first_object.draw_pos[1] +=   2 *  math.sin(first_object.moving_angle)





					
# 				#first animate
# 				# if first_object.growing == True:
# 				# 	first_object.radius += 1

# 				# else:
# 				# 	first_object.radius -= 1



# 				# if first_object.radius > 50:
# 				# 	first_object.growing = False

# 				# elif first_object.radius < 0:
# 				# 	first_object.growing = True



# 				#then check collision
# 				for second_object in self.drawing_container:

# 					if second_object == first_object:
# 						pass

# 					else:

# 						# if second_object.collision == True and first_object.collision == True:
# 						# 	pass
# 						# 	#continue moving in the right direction 

# 						# else: 
# 							self.check_collision(first_object, second_object)
			





# 				#update position for objects
# 				# if first_object.object_number % 2 == 0:
# 				# 	first_object.draw_pos[0] += 5
# 				# else:
# 				# 	first_object.draw_pos[0] -= 5


# 				# if first_object.draw_pos[0] < 0:
# 				# 	first_object.object_number += 1

# 				# if first_object.draw_pos[0] > self.window.size[0]:
# 				# 	first_object.object_number += 1
		
# 				Color(first_object.color[0], first_object.color[1], first_object.color[2], .8)
# 				Line(circle=(first_object.draw_pos[0], first_object.draw_pos[1], first_object.radius))
# 			#Rectangle(size= (200,200), pos = self.rect_pos )


# 	def on_motion(self, window, pos): 
# 		# response =  super(Sandbox_Widget, self).on_motion(touch)
# 		# if response:
# 		# 	print(touch)
# 		# 	return response
# 		# self.draw_pos[0], self.draw_pos[1] = pos

# 		# self.circle_radius = pos[0]
# 		#self.number_of_objects += 1
# 		#self.drawing_container.append(Circles(position=pos, count = self.number_of_objects))
# 		pass
	



# 	def on_touch_down(self, touch): 
# 		self.number_of_objects += 1
# 		self.drawing_container.append(Circles(position=touch.pos, count = self.number_of_objects))


# 	def clear_canvas(self):
# 		self.canvas.clear()

# 	def new_color(self):
# 		self.color[0] = random.uniform(0, 1)
# 		self.color[1] = random.uniform(0, 1)
# 		self.color[2] = random.uniform(0, 1)
