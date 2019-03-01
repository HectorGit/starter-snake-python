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
    headType = "bendr"
    tailType = "pixel"

    """start_response = {
        "color" : "ff00ff",
        "headType": "bendr",
        "tailType": "pixel"
    }"""

    return start_response(color, headType, tailType)












@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']    

    #get these properties, not sure if we will need them
    #graph = the board, width , height
    height = ['board']['height']
    width = ['board']['width']

    # not sure if this works
    # snakes positions
    snakesPositions = []
    for snake in data['board']['snakes']:
        snakesPositions.append(snake['body'])



    start = data['you']['body'] #this would be a {"x":1, "y:3"}
    #goal = any food that is closest - so w're not putting it here.

    # keep track of explored nodes (they will look like {"x":n1, "y":n2}
    explored = []


    # pathspathsQueue or allPaths
    # keep track of all the paths to be checked
    # should looks like [[{"x":n1, "y":n2}],[{},{},{}],[],[]] 
    pathsQueue = [[start]]
 
    #this would never happen
    # return path if start is goal
    #if start == goal:
    #    return "That was easy! Start = goal"
    bool foodFound = false

    # MOD : check until a food has been found, and then return that path. 
    # NOT THIS : keeps looping until all possible paths have been checked
    while pathsQueue and not foodFound :

        # pop the first path from the pathsQueue
        path = pathsQueue.pop(0)
        # get the last node from the path
        node = path[-1] # this would be the last coordinate in one of the paths {"x":n1,"y":n2}

        if node not in explored:

            # PROBLEM : what if the neighbour calculated here is 
            # not within the dimentions of the board, e.g. - larger
            # than "height" and "width" 
            # WHAT IS THE DEAL WITH DOUBLE AND SINGLE QUOTES?

            #generating the neighbours
            #POSSIBLE PROBLEM HERE :
            #node['x'] might be treated as a string, which means you can't
            #perform numeric operations on it.
            neighbours = 
            {"x":node['x'],"y":node['y']+1} , #UP
            {"x":node['x'],"y":node['y']-1},  #DOWN
            {"x":node['x']-1,"y":node['y']},  #LEFT
            {"x":node['x']+1,"y":node['y']}   #RIGHT
            # we dont have a graph, just the board and dimensions 
            # dont use graph[node]

            #filtering to avoid crashing into walls
            #pop to delete element by index
            #remove to delete element by value.

            #TRIED TO SOLVE PROBLEM AND REMOVE 
            #COORDINATES THAT ARE OFF THE BOARD
            for neighbour in neighbours:
                if neighbour['x'] >= width or neighbour['y'] >= height:
                    neighbours.remove(neighbour) 
                    
            # AVOIDING SNAKES : CHECK if any of the neighbours
            # has the coordinates that a SNAKE currently has
            # if so, remove it.
            for neighbour in neighbours:
                #if neighbour in data['board']['snakes'] #cant use this - not same type
                #for coords in data['board']['snakes']['body']
                if neighbour in snakesPositions: #created snakesPositions which is correct type for comparison
                    neighbours.remove(neighbour)



            # go through all neighbour nodes, construct a new path and
            # push it into the pathsQueue
            for neighbour in neighbours:

                # check if this neighbour contains food
                # need to access the data['board']['food']
                # possibly can use the 'in' operatior
                # if so - set the boolean to true to stop the loop    
                # might not need this... lets see
                #if neighbour in data['board']['food']:
                #    foodFound = true


                new_path = list(path)
                new_path.append(neighbour)
                pathsQueue.append(new_path)
                # return path if neighbour is goal
                #if neighbour in goal:
                #    return new_path
 
                if neighbour in data['board']['food']:
                    foodFound = true # to exit the loop
                    #we need to operate on the path found.

            # mark node as explored
            explored.append(node)

    # at this point we have exited the loop
    # and we have a path towards food 
    # is this possible?
    # we want the very last path appended
    path = pathsQueue.pop(-1)
    firstMove = path.pop(0)
    #{"x":n1,"y":n2}
    #subtract start from these coordinates,
    #and determine which direction to move
    #and return that direction
    x_diff = firstMove['x']-start['x']
    y_diff = firstMove['y']-start['y']

    if(y_diff>0){direction = 'right'}
    if(y_diff<0){direction = 'left'}
    if(x_diff>0){direction = 'up'}
    if(x_diff<0){direction='down'}

 
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