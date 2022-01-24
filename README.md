# Networking
###### Beta v0.1
 
## Overview
In order to gain a greater understanding of how computers communicate with each other, I created a program that allows two computers to send messages back and forth. This using IPv4 addresses ports. 

## Network Communication
While I plan to implement this in a peer-to-peer format, this app still using a server-client relationship. It uses TCP for increased reliability on port 50007. Messages are inherently strings, which are encoded as bytes, sent, and then decoded as a string when the message is received.

## Development Environment
* __Visual Studio Code (IDE):__ An IDE with great support for Python.
* __Python 3.9.7:__ Python is a programming language, which this whole program was developed in.
* __Socket:__ Socket is a low-level networking interface. It provides you with the necessary objects and functions to make network calls to the OS
* __JSON:__ JSON is a library that provides function to read and store .json files. This was used to store the previous address and port so they could quickly be reused.
* __TKinter:__ This library is used for creating GUIs. Currently it is not being used, but will soon provide a way to easily see and send messages.

## Useful Websites
* [TestOut](https://labsimapp.testout.com/)
* [Python Documentation: Socket Library](https://docs.python.org/3.9/library/socket.html#)

## Future Work
* Implement a TKinter GUI
* Loop the program so messages can be sent back and forth without delay
* Update readme with more info (Documents/network_readme.md)
