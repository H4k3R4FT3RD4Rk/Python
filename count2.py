import subprocess
import re

def execute_command():
    command = ['nc', 'challs.n00bzunit3d.xyz', '13541']
    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = process.stdout.read().decode()

        #question = re.search(r'Question: (.+)', output).group(1)
        #print(f"Received question: {question}")

        number1, number2 = extract_numbers(question)
        print(f"Extracted numbers: {number1}, {number2}")

        answer = calculate_answer(number1, number2)
        print(f"Calculated answer: {answer}")

        process.stdin.write(f"{answer}\n".encode())
        process.stdin.flush()

        output = process.stdout.read().decode()
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error: {e}")

def extract_numbers(question):
    match = re.search(r'How many (\d+)\'s appear till (\d+)', question)
    number1 = int(match.group(1))
    number2 = int(match.group(2))
    return number1, number2

def calculate_answer(number1, number2):
    digit = str(number1)
    count = str(count_digit_appearances(number2, digit))
    return count

def count_digit_appearances(number, digit):
    return sum(str(num).count(digit) for num in range(1, number + 1))

execute_command()
