import socket
import re

rEquation = r"Equation: (\d+)\*X\^2 ([\-\+] \d+)\*X ([\-\+] \d+) = 0"

def solve(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    if delta == 0:
        return int(-b/(2*a))
    else:
        return int((-b + delta**0.5)/(2*a)), int((-b - delta**0.5)/(2*a))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('115.79.193.109', 28063))

count = 0
while True:
    buffer = ''
    buffer += sock.recv(1024).decode('utf-8')

    match = re.search(rEquation, buffer)
    if match:
        a = int(match.group(1))
        b = int(match.group(2).replace(' ', ''))
        c = int(match.group(3).replace(' ', ''))

        solution = solve(a, b, c)
        if len(solution) == 1:
            s = str(solution[0]) + '\n'
        else:
            s = str(solution[1]) + ', ' + str(solution[0]) + '\n'

        sock.send(s.encode('utf-8'))
        count += 1
        print(buffer)
        print(s)
    else:
        print(buffer)
        print(count)
        break