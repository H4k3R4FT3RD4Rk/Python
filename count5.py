import socket
import re

# Define the server details
server_host = 'challs.n00bzunit3d.xyz'
server_port = 13541

# Create a socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_host, server_port))

# Receive the initial server response
output = sock.recv(4096).decode("utf-8")
print("Server Response:")
print(output)

while True:
    # Extract the question from the server response
    question_match = re.search(r'How many .*?\?', output)
    if question_match:
        question = question_match.group()
        print("Question:")
        print(question)

        # Extract the two random numbers from the question using regular expressions
        number_matches = re.findall(r'\d+', question)
        if len(number_matches) == 2:
            number1 = int(number_matches[0])
            number2 = int(number_matches[1])

            # Calculate the answer based on the specific logic
            answer = 0
            for num in range(1, number2):
                answer += str(num).count(str(number1))

            # Print the answer
            print("Answer:", answer)

            # Send the answer back to the server
            answer_str = str(answer) + "\n"
            sock.sendall(answer_str.encode("utf-8"))

            # Receive the server response
            output = sock.recv(4096).decode("utf-8")
            print("Server Response:")
            print(output)
        else:
            print("Failed to extract numbers from the question.")
    else:
        print("Failed to extract the question from the server response.")

# Close the socket connection
sock.close()
