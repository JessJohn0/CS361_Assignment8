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
    try:
        json_received = json.loads(received)
    except json.JSONDecodeError:
        socket.send(b"Error - Invalid JSON.")

    #  Do some 'work'
    time.sleep(1)
    for key in json_received:
        #print(f"This is the key: {key}")
        #print(f"This is the value: {json_received[key]}")
        if key == "start":
            start_date = json_received[key]
        if key == "end":
            end_date = json_received[key]
        if key == "assets":
            assets_array = json_received[key]

    # Convert assets_array to floats
    try:
        float_array = [float(i) for i in assets_array]
    except NameError:
        socket.send(b"Error - JSON is missing parameters.")

    # Finding all dates between two dates
    start_string = start_date
    end_string = end_date
    start_date = datetime.datetime.strptime(start_string, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_string, '%Y-%m-%d').date()

    # Finding all dates between two dates and putting them into an array
    delta = end_date - start_date

    date_array = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        date_array.append(day)

    # Array of dates for x axis
    x = date_array

    # Array of ints for y axis
    y = float_array

    try:
        plt.plot(x, y, 'b') # Blue line
        plt.title("Net Assets Over Time", fontsize=20, weight="bold")
        plt.xlabel("Dates", fontsize=16, weight="bold")
        plt.ylabel("Net Assets", fontsize=16, weight="bold")
        plt.xticks(x, rotation=30)
        #plt.yticks(y) # This will use the values of the float_array as the y-axis
        plt.show()
    except ValueError:
        socket.send(b"Error - Graph did not display.")

    #  Send reply back to client
    socket.send(b"Success")
