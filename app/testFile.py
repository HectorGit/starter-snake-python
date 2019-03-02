
#kinsol research... 

def main():

	#data = {}
	data = {"game": {"id": "game-id-string"},"turn": 1,"board": {"height": 11,"width": 11, "food": [{"x": 7,"y": 0}],"snakes": [{"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 5,"y": 5}]}]},"you": {"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 1,"y": 3}]}}

	move(data)

	#print("Hello World!")


def move(data):

	#print(data)

	directions = ['up', 'down', 'left', 'right']    

	height = data['board']['height']

	print("boardHeight %d", height)

	width = data['board']['width']

	print("boardWidth %d",width)

	snakesPositions = []
	for snake in data['board']['snakes']:
		snakesPositions.append(snake['body'])

	print("\n snake positions")
	print(snakesPositions)


	start = data['you']['body'][0] # should be {"x":n1, "y":n2}

	print('printing start: %s ', start)

	explored = []

	pathsQueue = [[start]]
 
	foodFound = False

	iterations = 0

	while pathsQueue and not foodFound and iterations < 10:

		iterations = iterations+1

		path = pathsQueue.pop(0)
		node = path[-1]

		if node not in explored:

			value_x = node['x']
			value_y = node['y']

			#changed these because of board orientation
			up_neighbour = {"x":value_x,"y":value_y-1}
			down_neighbour = {"x":value_x,"y":value_y+1}
			left_neighbour = {"x":value_x-1,"y":value_y}
			right_neighbour = {"x":value_x+1,"y":value_y}

			#print("printing node and neighbours")
			#print(node)
			#print(up_neighbour)
			#print(down_neighbour)
			#print(left_neighbour)
			#print(right_neighbour)

			neighbours = []
			if up_neighbour not in explored:
				neighbours.append(up_neighbour)
			if down_neighbour not in explored:	
				neighbours.append(down_neighbour)
			if left_neighbour not in explored:
				neighbours.append(left_neighbour)
			if right_neighbour not in explored:
				neighbours.append(right_neighbour)   

			print("printing neighbours")
			print(neighbours)
		   
			for neighbour in neighbours:
				#exceeds x coordinates?
				if neighbour['x'] >= width-1 or neighbour['x'] < 0:
					neighbours.remove(neighbour) 

				#exceeds y coordinates?
				if neighbour['y'] >= height-1 or neighbour['y'] <0:
					neighbours.remove(neighbour) 
 
			for neighbour in neighbours:
				if neighbour in snakesPositions: 
					neighbours.remove(neighbour)

			print("printing neighbours post filtering")
			print(neighbours)

			for neighbour in neighbours:
			    new_path = list(path)
			    new_path.append(neighbour)
			    pathsQueue.append(new_path)
			 
			    if neighbour in data['board']['food']:
			        foodFound = True 
			        print("\n foodFound at:")
			        print(neighbour)

				explored.append(node)


	path = pathsQueue.pop(0)

	print("\n start")
	print(start)

	print("\n path:")
	print(path)

	firstMove = path.pop(1)
	print("firstMove")
	print(firstMove)

	x_diff = firstMove['x']-start['x']
	y_diff = firstMove['y']-start['y']

	print("x_diff %d", x_diff)
	print("y_diff %d", y_diff)

	direction = "none_selected"

	"""if y_diff>0 : 
		direction = 'up'
	elif y_diff<0 : 
		direction = 'down'
	elif x_diff>0 : 
		direction = 'left'
	elif x_diff<0 : 
		direction = 'right'
	"""

	#reversed the y conditions
	#given board orientation

	if y_diff < 0:#and firstMove['y'] < height-1 and firstMove ['y'] > 0: 
		direction = 'up'
	elif y_diff > 0:# and firstMove['y'] < height-1 and firstMove ['y'] > 0: 
		direction = 'down'
	elif x_diff > 0:# and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
		direction = 'left'
	elif x_diff < 0:# and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
		direction = 'right'

	print("\n direction picked:")
	print(direction)

 

if __name__== "__main__":

  main()


"""

height = data['board']['height']

   # print("boardHeight %d", height)

    width = data['board']['width']

    #print("boardWidth %d",width)

    snakesPositions = []
    for snake in data['board']['snakes']:
        snakesPositions.append(snake['body'
    #print(snakesPositions)
])

    #print("\n snake positions")

    start = data['you']['body'][0] # should be {"x":n1, "y":n2}

    #print('printing start: %s ', start)

    explored = []

    pathsQueue = [[start]]
 
    foodFound = False

    while pathsQueue and not foodFound:

        path = pathsQueue.pop(0)
        node = path[-1]

        if node not in explored:

            value_x = node['x']
            value_y = node['y']

            up_neighbour = {"x":value_x,"y":value_y+1}
            down_neighbour = {"x":value_x,"y":value_y-1}
            left_neighbour = {"x":value_x-1,"y":value_y}
            right_neighbour = {"x":value_x+1,"y":value_y}

            #print("printing node and neighbours")
            #print(node)
            #print(up_neighbour)
            #print(down_neighbour)
            #print(left_neighbour)
            #print(right_neighbour)

            neighbours = []
            neighbours.append(up_neighbour)
            neighbours.append(down_neighbour)
            neighbours.append(left_neighbour)
            neighbours.append(right_neighbour)   

            #print("printing neighbours")
            #print(neighbours)
           
            for neighbour in neighbours:
                if neighbour['x'] >= width or neighbour['y'] >= height:
                    neighbours.remove(neighbour) 
                    
            for neighbour in neighbours:
                if neighbour in snakesPositions: 
                    neighbours.remove(neighbour)

            #print("printing neighbours post filtering")
            #print(neighbours)

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                pathsQueue.append(new_path)
             
                if neighbour in data['board']['food']:
                    foodFound = True 

                explored.append(node)

    path = pathsQueue.pop(-1)
    firstMove = path.pop(0)

    x_diff = firstMove['x']-start['x']
    y_diff = firstMove['y']-start['y']

    direction = ""


    # here possibly add a way to fix that 
    # you crash into walls

    if y_diff>0 and firstMove['y'] < height-1 and firstMove ['y'] > 0 : 
        direction = 'up'
    if y_diff<0 and firstMove['y'] < height-1 and firstMove ['y'] > 0: 
        direction = 'down'
    if x_diff>0 and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
        direction = 'left'
    if x_diff<0 and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
        direction = 'right'

    return move_response(direction)
"""



































