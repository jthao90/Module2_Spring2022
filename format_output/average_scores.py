"""
Below I took notes, made comments, wrote pseudocode
"""

#store a constant of the number of scores we will input: 3


#Prompt user for inputs

    #store input as last_name
    #store input as first_name

    #Prompt user for inputs (do it constant times, use a new variable each time)


#calculate an average (sum each value and divide by the number of values)

#print output: should look like
#Rodriguez, Linda age: 21 average grade: 92.50



"""
Examples of what we are doing
"""

#store a constant of the number of scores we will input: 3
NUM_OF_SCORES = 3


#Prompt user for inputs
print('Enter your name, last then first and age: ')

#store input as last_name
last_name = input()
print(last_name.capitalize())

#store input as first_name
first_name = input()
print(first_name.capitalize())

#store input as age
age = input()
print(age)

#Prompt user for inputs (do it constant times, use a new variable each time)
print('Enter score 1: ')
score_one = input()
print(score_one)
score_one = float(score_one)

print('Enter score 2: ')
score_two = input()
print(score_two)
score_two = float(score_two)

print('Enter score 3: ')
score_three = input()
print(score_three)
score_three = float(score_three)


#calculate an average (sum each value and divide by the number of values)
total_score = score_one + score_two + score_three
print(total_score)

avg = total_score / NUM_OF_SCORES
format_avg = "{:.2f}".format(avg)
print(format_avg)


#print output: should look like
print('{}, {} age: {} average grade: {:5.2f}'.format(first_name.capitalize(), last_name.capitalize(), age, avg))

#Rodriguez, Linda age: 21 average grade: 92.50
