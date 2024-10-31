import data

# Write your functions for each part in the space below.

# Part 1
# The following function takes two points of class Point as the input and rearranges their coordinates
# to create a rectangle of class Rectangle denoted by a bottom right corner point and a top left
# corner point as the output.
def create_rectangle (Point1, Point2):
    if Point1.x < Point2.x:
        Top_leftx = Point1.x
        Bottom_rightx = Point2.x
    else:
        Top_leftx = Point2.x
        Bottom_rightx = Point1.x
    if Point1.y < Point2.y:
        Top_lefty = Point2.y
        Bottom_righty = Point1.y
    else:
        Top_lefty = Point1.y
        Bottom_righty = Point2.y
    Top_left = data.Point(Top_leftx, Top_lefty)
    Bottom_right = data.Point(Bottom_rightx, Bottom_righty)
    return data.Rectangle(Top_left, Bottom_right)




# Part 2
# The following function takes two durations and tests if the first duration is shorter than the second.
# If the first is shorter than the second, the functon returns True as the output. If not, it returns False.
def shorter_duration_than(Duration1, Duration2):
    if Duration1.minutes < Duration2.minutes:
        return True
    if Duration1.minutes == Duration2.minutes and Duration1.seconds < Duration2.seconds:
        return True
    else:
        return False

# Part 3
# The following function takes a list of songs of class Song and a specific song as the inputs and
# returns a list of songs in the list that are shorter than that specific song as the output.
def song_shorter_than(song_list:list, song):
    return [a for a in song_list if shorter_duration_than(a.duration, song.duration) == True]

# Part 4
# The following function takes a list of songs of class song and a list of integers as the inputs.
# The function then creates a playlist using the number list to call each song index in the song list.
# The function returns the total duration of this playlist in minutes and seconds by adding up
# The durations of all the songs in the playlist.
def running_time(song_list:list, number_list:list):
    minutes = 0
    seconds = 0
    for i in range(len(number_list)):
        if number_list[i] < 0 or number_list[i] > len(song_list)-1:
            continue
        else:
            minutes += song_list[number_list[i]].duration.minutes
            seconds += song_list[number_list[i]].duration.seconds
            running_time = data.Duration(minutes, seconds)
        minutes += running_time.seconds // 60
        seconds = running_time.seconds % 60
        running_time = data.Duration(minutes, seconds)
    return running_time


# Part 5
# The following function takes a list of links between cities and a route between multiple cities as the input.
# The function then verifies if it is possible to complete the route using the set of links between
# cities in the links list and returns True if it is possiible and False if it is not possible.
def validate_route(links_list:list, route:list):
    if route == []:
        return True
    if len(route) == 1 and route[0] in links_list:
        return True
    else:
        for i in range(len(route) - 1):
            listone = [route[i], route[i + 1]]
            listtwo = [route[i + 1], route[i]]
            if listone in links_list or listtwo in links_list:
                continue
            else:
                return False
        return True




# Part 6
# The following function takes a list of integers and returns None if the list is empty. Otherwise,
# the function returns the index value at which the largest series of identical values begins in
# the list.
def longest_repitition(numberlist: int):
    if numberlist == []:
        return None
    else:
        repitition = 0
        max_repitition = 0
        for i in range(len(numberlist) - 1):
            if numberlist[i] == numberlist[i-1]:
                repitition += 1
                if repitition > max_repitition:
                    max_repitition = repitition
                    i_max = i - max_repitition
                else: continue
            else: repitition = 0
        return i_max

