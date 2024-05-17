import json
import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

example_json = '{"start":"2000-10-01", "end":"2000-10-05", "assets": ["1.0", "2.0", "4.0", "3.5", "5.5"]}'
#example_json = '{}'

while True:
    socket.send(bytes(example_json, 'utf-8'))

    #  Get the reply.
    message = socket.recv()
    print("Received reply [ %s ]" % (message))