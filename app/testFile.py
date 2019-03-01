
#kinsol research... 

def main():

	#data = {}
	data = {"game": {"id": "game-id-string"},"turn": 1,"board": {"height": 11,"width": 11, "food": [{"x": 1,"y": 3}],"snakes": [{"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 5,"y": 5}]}]},"you": {"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 1,"y": 3}]}}

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

			print("printing neighbours")
			print(neighbours)
		   
			for neighbour in neighbours:
				if neighbour['x'] >= width or neighbour['y'] >= height:
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

				explored.append(node)

	path = pathsQueue.pop(-1)
	firstMove = path.pop(0)

	x_diff = firstMove['x']-start['x']
	y_diff = firstMove['y']-start['y']

	direction = ""

	if y_diff>0 : 
		direction = 'right'
	if y_diff<0 : 
		direction = 'left'
	if x_diff>0 : 
		direction = 'up'
	if x_diff<0 : 
		direction = 'down'

 
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



































