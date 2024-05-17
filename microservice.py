# Source: https://www.geeksforgeeks.org/matplotlib-pyplot-plot_date-function-in-python/amp/

# importing libraries

import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import json
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    received = socket.recv()
    received = received.decode("utf-8")
    json_received = json.loads(received)
    print(f"This is json_received {json_received}")
    print(f"This is received {received}")

    #  Do some 'work'
    time.sleep(1)
    for key in json_received:
        print(f"This is the key: {key}")
        print(f"This is the value: {json_received[key]}")
        if key == "start":
            start_date = json_received[key]
        if key == "end":
            end_date = json_received[key]
        if key == "assets":
            assets_array = json_received[key]
            #print(type(assets_array))
            #print(f"This is assets_array{assets_array}")

    # Convert assets_array to ints
    int_array = [eval(i) for i in assets_array]
    print(int_array)

    # Finding all dates between two dates
    start_string = start_date
    end_string = end_date
    start_date = datetime.datetime.strptime(start_string, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_string, '%Y-%m-%d').date()

    # Finding all dates between two dates
    delta = end_date - start_date

    date_array = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        print(day)
        date_array.append(day)
    print(date_array)

    # Array of dates for x axis
    dates = date_array

    # for y axis
    #x = [0, 1, 2, 3, 4]
    x = int_array

    plt.plot(dates, x, 'g')
    plt.xticks(rotation=70)
    plt.show()

    #  Send reply back to client
    socket.send(b"Success")
