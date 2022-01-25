# Networking
###### Release v1.0
 
## Overview
In order to gain a greater understanding of how computers communicate with each other, I created a program that allows two computers to send messages back and forth. 

[Software Demo](https://youtu.be/7mRdbnCuT08)

## Network Communication
This program communicates back and forth using a peer-to-peer networking module. It uses TCP for increased reliability, IPv4 addresses, and by default port 50007. Messages are inherently strings, which are encoded as bytes, sent, and then decoded as a string when the message is received. This program includes a GUI to make it easier to send and receive messages.

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
* Validate IP address and port before submitting
* Make messages send on enter keypress
