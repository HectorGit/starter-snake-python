import json
import os
import random
import bottle


from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """


    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """not sure if have to use dumps here """
    """print(json.dumps(data['game']['id']))"""
    

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"
    #headType = "bendr"
    #tailType = "pixel"

    """start_response = {
        "color" : "ff00ff",
        "headType": "bendr",
        "tailType": "pixel"
    }"""

    return start_response(color)#, headType, tailType)



@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    #print(json.dumps(data))

    #directions = ['up', 'down', 'left', 'right']    

    #dirction = random.choice(directions) # i think that's how it was initially
 
    directions = ['up', 'down', 'left', 'right']    

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

    path = pathsQueue.pop(0)#(-1)
    firstMove = path.pop(1)

    x_diff = firstMove['x']-start['x']
    y_diff = firstMove['y']-start['y']

    # here possibly add a way to fix that 
    # you crash into walls

    if y_diff>0 and firstMove['y'] < height-1 and firstMove ['y'] > 0 : 
        direction = 'up'
    elif y_diff<0 and firstMove['y'] < height-1 and firstMove ['y'] > 0: 
        direction = 'down'
    elif x_diff>0 and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
        direction = 'left'
    elif x_diff<0 and firstMove['x'] < width-1 and firstMove ['x'] > 0: 
        direction = 'right'

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )


"""
# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    pathsQueue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while pathsQueue:
        # pop the first path from the pathsQueue
        path = pathsQueue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the pathsQueue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                pathsQueue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 
bfs_shortest_path(graph, 'G', 'D')  # returns ['G', 'C', 'A', 'B', 'D']
"""