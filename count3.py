import subprocess
import re

# Define the command
command = ["nc", "challs.n00bzunit3d.xyz", "13541"]

# Execute the command and capture the output
output = subprocess.check_output(command, stderr=subprocess.STDOUT)

# Decode the output from bytes to string
output = output.decode("utf-8")

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
        #print(number1)
        #print(number2)

        # Calculate the answer based on the specific logic for your question
        answer = 0
        for num in range(1, number2):
            answer += str(num).count(str(number1))

        # Print the answer
        print("Answer:", answer)

        # Send the answer back to the server
        subprocess.run(['echo', str(answer)], input=b'', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:
        print("Failed to extract numbers from the question.")
else:
    print("Failed to extract the question from the server response.")
