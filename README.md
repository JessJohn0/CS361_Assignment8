# CS361-Sprint2-Assignment8

Net Assets vs Time Graph Microservice

This microservice recieves a JSON object from the main program (my example main program is called ui.py). 
It will then do some conversions and display a graph showing the dates on the x-axis and the net assets on the y-axis. 
The graph is made using [matplotlib](https://matplotlib.org/) and [ZeroMQ](https://zeromq.org/) is used for pipeline communication.

# Set-up for ZeroMQ
Include this in both the main program and the microservice.

![image](https://github.com/JessJohn0/CS361_Assignment8/assets/129867751/5544c719-acf4-425e-8f26-8f041744b9d2)

# How to request data from the microservice
To request data from the microservice, send a JSON object with a start date, end date, and net assets as floats. 

![image](https://github.com/JessJohn0/CS361_Assignment8/assets/129867751/fe395545-24c1-4d27-888a-4bfe1614fbfa)

# How to recieve data from the microservice
A message will be send back from the microservice. Either an error message if something went wrong, or "Success" if the graph was able to be displayed.

![image](https://github.com/JessJohn0/CS361_Assignment8/assets/129867751/fde7cc51-fe07-4868-a1ba-8d6d309da02c)

# UML Diagram

![image](https://github.com/JessJohn0/CS361_Assignment8/assets/129867751/7cd1de44-cfd0-4d1c-99a2-5529e3d968e6)




