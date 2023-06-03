from mcstatus import JavaServer
import matplotlib.pyplot as plt
import datetime
import time

server_ip = "mc.javasurvival.com"  # server address
server_port = 25565  # server port

y_axis_limit = 30  # how many y values there are (max player count)
y_tick_increment = 1  # how much the y value increases by
timeToSleep = 3600  # how many seconds to wait between each update
x_axis_limit = 24  # how many x values there can be (times updated)
SaveToFile = False  # Set this flag to True if you want to save a picture of the graph

timestamps = []
player_counts = []
entries = 0

def get_player_count():
    server = JavaServer.lookup(f"{server_ip}:{server_port}")
    status = server.status()
    player_count = status.players.online
    return player_count

def update_graph():
    global entries
    
    time_strings = [timestamp.strftime("%H:%M:%S") for timestamp in timestamps]

    plt.clf()

    plt.plot(time_strings, player_counts)
    plt.xlabel("Time")
    plt.ylabel("Player Count")
    plt.title("Minecraft Server Player Count")
    plt.xticks(rotation=30)
    entries += 1

    plt.ylim(0, y_axis_limit)

    plt.yticks(range(0, y_axis_limit + 1, y_tick_increment))

    plt.draw()
    plt.pause(0.01)

def save_graph():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    plt.savefig(f"graph_{current_date}.png")

while True:
    current_time = datetime.datetime.now()
    player_count = get_player_count()

    timestamps.append(current_time)
    player_counts.append(player_count)

    if len(timestamps) > x_axis_limit:
        if SaveToFIle:
            if entries > x_axis_limit:
                entries = 0
                print("Saving")
                save_graph()

        timestamps.pop(0)
        player_counts.pop(0)

    update_graph()
    time.sleep(timeToSleep)
