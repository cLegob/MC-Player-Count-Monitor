# MC-Player-Count-Monitor  
I created this program to monitor the amount of players on a minecraft server, it's very customizable:  
y_axis_limit changes how many ticks there are on the y axis, I recommend setting this to your server's max playercount  
y_tick_increment changes what the y axis ticks count up by, 1's, 2's, 5's, 10's, etc  
timeToSleep changes how often the graph updates (in seconds)
x_axis_limit changes how many x values there are (how many updates) there are before it either starts to delete the earliest ones, or until it saves to file  
resetSaveToFile is a boolean, if it is true, it will save a picture of the graph every time x_axis_limit is hit, and it will also reset the graph
