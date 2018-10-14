# Author Dancan Angwenyi
# Date 06 september 2018
# Basic server program for communicating with the an android application
# over the internet.
# The server receives messages from the client and acks by sending back
# 'ACK, Message received, OK'. Incase the message contains an exit command,
# the server acks and sends an additional message 'Terminated' and breaks the connection
#
# The code is be improved by including in ways for checking that the data received is indeed
# not corrupted. 

import socket
import config

HOST = config.HOSTNAME # Server IP or Hostname
PORT = config.SERVER_PORT # The port we are going to connect to

receiving_error = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('*****Socket created*****')

try:
        s.bind((HOST, PORT))
        print("...Socket bind successful..")

        #Listen to only one client
        s.listen(1)

        #Runs until the user sends an exit command
        while True:
                (conn, addr) = s.accept()

                print('********Connected**********')

                data = (conn.recv(1024))
                reply = ''

                # process your message
                if not data:
                        break

                print("Data: "+data)
                reply = 'ACK, Message received, OK'
                print("Reply to client: "+reply)

                # TODO
                if receiving_error:
                        # Send Error Message
                        continue

                #Incase we want to exit the connection
                if data == 'exit':
                        print("Terminating...")
                        conn.send('Connection terminated, bye')
                        break

                conn.send(reply)
                conn.close()

except OSError as e:
        print ('Socket Bind failed, terminating')



def secondary_error():
        """
        This function means that a receiving error occurred
        """
        receiving_error=True

