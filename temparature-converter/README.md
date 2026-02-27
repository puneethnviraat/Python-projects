Project: Temperature Converter
Practice the Python project—that converts between Celsius, Fahrenheit, and Kelvin.

Create a Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin. The goal is to help learners understand basic input handling, conditionals, arithmetic operations, and functions—all in a practical, real-world context.

Goals
By the end of this project, you’ll be able to:

Convert temperatures between Celsius, Fahrenheit, and Kelvin.

Use input() to get user input.

Apply conditionals (if, elif, else) to control program flow.

Use functions to organize code for reusability and clarity.

Handle invalid input gracefully.

Project breakdown
Print a welcome message, explain the conversion options, and prompt the user to choose one.

Get the user’s choice and the temperature to convert; handle invalid input.

Write a separate function for each type of temperature conversion.

Use if/elif/else to call the correct function and display the result.

Step 1: Program setup
Print a welcome message.

Explain the available conversion types.

Prompt the user to choose a conversion type (e.g., Celsius to Fahrenheit).
Step 2: Take the user input
Get the user’s choice (conversion type).

Ask for the temperature to convert.

Convert the input to a float.
Step 3: Define conversion functions
Create separate functions for each conversion type:
Step 4: Perform the conversion
Use conditionals to check the user’s choice and call the appropriate function:
Mini challenge
Let the user convert multiple temperatures in one run and log the results in a list. At the end, print all conversions done during the session.

bulb
Use a while loop to let users keep converting temperatures, and store each result in a list. Exit the loop with a special input like 'q', then print the list at the end.
