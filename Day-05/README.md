Command Line Argument :

Command line arguments are another way to read user-provided input into a Python program, distinct from using the input() function. Instead of providing input during the program's execution, you pass arguments from the command prompt at the time of executing the Python script.

To pass command-line arguments, you type the py command followed by the script name (e.g., test.py) and then any arguments separated by spaces. For example: py test.py 10 20 30. In this case, 10, 20, and 30 are considered command-line arguments.

Within a Python script, you can read these command-line arguments using the sys module and its argv variable. The sys module is a predefined module in Python. The argv variable, present inside the sys module, allows you to access the command-line arguments. To use it, you first need to import it from the sys module: from sys import argv.

The argv variable is a list. This is because the order of command-line arguments is important, and duplicate values are allowed. You can verify this by printing the type of argv: print(type(argv)) will output <class 'list'>.

When you access elements of the argv list using indexing (e.g., argv), it's crucial to understand that the first element (argv) is always the name of the Python file being executed. It is not the first argument you pass after the script name. So, for the command py test.py 10 20 30, argv will be 'test.py', argv will be '10', argv will be '20', and argv will be '30'.

You can iterate through all the command-line arguments, including the script name, using a for loop:


from sys import argv
for arg in argv:
    print(arg)
    
This will print each element of the argv list on a new line. You can also get the total number of command-line arguments using the len() function on the argv list:

from sys import argv

number_of_arguments = len(argv)
print("The number of command line arguments:", number_of_arguments)
print("The list of command line arguments:", argv)
for x in argv:
print(x)


When you pass command-line arguments, they are always considered as string type. Even if you pass numbers, they are treated as strings. Therefore, if you intend to perform numerical operations on these arguments, you must explicitly convert them to the desired numeric type (e.g., integer using int()).

A practical example demonstrating this is calculating the sum of numbers provided as command-line arguments. To sum the numbers, you need to iterate through the argv list starting from the second element (index 1) to ignore the script name, convert each argument to an integer, and then add it to a running sum:

from sys import argv
args = argv[1:]
sum = 0

for x in args:
sum=sum+args
print("the sum:", sum)

(OR)

from sys import argv

sum_of_numbers = 0
# Consider arguments from index 1 onwards
for arg in argv[1:]:
    try:
        number = int(arg)
        sum_of_numbers += number
    except ValueError:
        print(f"Warning: '{arg}' is not a valid number and will be ignored.")

print("The sum is:", sum_of_numbers)

Another significant advantage of command-line arguments is the ability to customize the behavior of an application without modifying the code directly. A real-time scenario illustrating this is a file merger application. Instead of hardcoding the input and output file names in the script, you can pass them as command-line arguments:

from sys from argv
f1= open(argv[1])
f2= open(argv[2])
f3= open(argv[3], 'w')

for x in f1:
f3 .write(x)
for x in f2:
f2.write(x)

(OR)

from sys import argv

if len(argv) != 4:
    print("Usage: python merger.py <input_file1> <input_file2> <output_file>")
else:
    input_file1_name = argv[1]
    input_file2_name = argv[5]
    output_file_name = argv[4]

    try:
        with open(input_file1_name, 'r') as f1, open(input_file2_name, 'r') as f2, open(output_file_name, 'w') as f3:
            for line in f1:
                f3.write(line)
            for line in f2:
                f3.write(line)
        print(f"Successfully merged '{input_file1_name}' and '{input_file2_name}' into '{output_file_name}'.")
    except FileNotFoundError:
        print("Error: One or more input files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
To execute this script, you would provide the file names as arguments: py merger.py file1.txt file2.txt output.txt. This makes the application more flexible, as you can specify different file names each time you run it without altering the Python code.
