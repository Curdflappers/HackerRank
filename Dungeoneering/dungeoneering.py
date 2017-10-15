"""Run the Dungeoneering coding challenge
"""
def fastest_path(canyon):
    """ Return the fastest path out of the canyon
    """

    # find earliest spot that can escape, add to our path
    # add earliest spot that can access that spot
    # repeat until initial element is in our list
    path = []
    last_stop = len(canyon)
    i = 0
    while True:
        if canyon[i] + i >= last_stop: # this spot escapes
            path.insert(0, canyon[i]) # this is now the first spot
            last_stop = i # we need to get to i
            if i == 0:
                break # our initial spot is in the list
            i = -1 # restart the search
        elif i >= last_stop: # no previous spot gets us where we need to go
            return False # no path exists
        i += 1

    return path

print(fastest_path([1, 2, 3, 4, 5]))
