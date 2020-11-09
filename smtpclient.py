from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    mailFromCommand = 'MAIL FROM:<tsr9804@nyu.edu>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send RCPT TO command and print server response.
    rcptToCommand = 'RCPT TO:<tsriggs11@gmail.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send message data.
    msg = "\r\n My message"
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send QUIT command and get server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
