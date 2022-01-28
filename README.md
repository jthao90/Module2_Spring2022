# Module2_Spring2022
Write the manual tests and program average_scores.py to read in one person's names, first and last, their age and three scores out of 100. Take the three scores and find the average, storing into a variable.

    -Create a project Module 2, add directories format_output.
    -In format folder, make average_scores.py 

It's time to write the main in your average_scores.py.

    -Prompt the user for what is expected for each input
    -Store into local variables last_name, first_name.
    -Use a constant to represent the number of scores you will prompt the user to input
    -Prompt the user for the scores, storing them in local variable or variables. 
        -You can keep separate variables for each score, or you keep a running total in one variable. 
    -Calcuate the average using the variables.
    -Print the output, with last name followed by a comma and the first name followed by an integer age and then the average scores with 2 decimal places.
        -Example output:
        Rodriguez, Linda age: 21 average grade: 92.50
        -Add doctring to the top of your file, add comments at the bottom with observed output after a few manual test runs of your code.
    -Submit your average_scores.py

Note: Be sure to format your output string like the above. If the user is promted and enters John Smith for their first and last name, 25 for their age, and test scores of 70,80, and 90 your code should output:
Smith, John age: 25 average grade: 80.00
And if they entered Jane Doe, 33 and scores of 95, 100, and 105 it should output:
Doe, Jane age: 33 average grade: 100.00
