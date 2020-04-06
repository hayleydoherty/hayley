# hayley

## Problem Sheet

The GitHub repository hayleydoherty/hayley contains my code for the weekly problems set out in the programming and scripting module.  
Below I will outline each problem and the approach I took to solving it.

## Week2v2.py
The python file entitled week2v2 is the file I wish to submit for the weekly task 2.
We were asked to write a program that takes in a persons height and weight and outputs their BMI.
The equation for calculating BMI was provided.
I used the input function which asks the user to input their height and weight.
I saved the values input as variables called height and weight.
I then used these variables in the equation to calculate the users BMI (and saved it as a variable called BMI).
Finally I used the print function to return the users BMI to them.

## Week3.py
We had to write a program that takes in a string from the user and returns only every second letter in reverse order.
I used the input function to get the string from the user and saved it as the variable x.
I used the preint function to return the string.
Using [:] with print allow you to slice a string and output only the section specified. And including -1 at the end returns the string in reverse order, [::-1].
By using print(x[::-2]) in my code I returned the string in reverse order and only returned every second character.

## Week4.py
For this task we had to write a programme that used a loop and if statement.
Depending on whether the number inout was even or odd, we had to perform certain math to the input.
Again I used the input function to get the inout from the user and converted it to an integer.
I created a while loop that would run so long as the number is greater than 1.
An if statement was used to determine if the number input is even or odd.
If even it is divided by 2 and so long as the result of this is greater then 1, it goes through the while loop again.
Again it is determined if this number is even or not.
If it is odd, it is multiplied by 3 and added to 1.
This new number is then run through the loop again and the process continues until the number reaches 1.
The print statement at the end prints each nu,ber that is put though the while loop.

## Week5.py
In week 5 we had to write a program that outputs whether it is currently the weekend or not.
I imported the module datetime and set a variable (d) equal to the current date and time.
I then use an if statement to decide what day it is, i.e. if the day (d.weekday())is equal to either 0-4 it is a week day as Monday is represented by 0, Tuesday by 1 etc.
If the day (d.weekday()) is 5 or 6 it is the weekend.
A statement is printed to the screen informing the user whether or not today is a weekday.

## week6v2.py
Create a function that uses Newton's square root equation to calculate the approxiamte square root of a positive floating point number.
I created a variable called root which multiplied the number given in the function by 0.3 in order to give an approximation of the square root.
In a while loop, I used this approximation in Newton's equation: divide the number givin in function by root, then add it to root and finally divide this by 2.
I called this new value root2.
I used an if statemnt to determine if the precision is less than 0.00001.
If it isn't then it goes through the calculation until it is and root2 it returned as the solution.

## week7v2.py
Write a program that counts the number of occurences of a particular letter in a text file.
I used the input function in order to get the file name and letter to be counted from the user.
'with open' opens the file and closes it again once the program is finished without explicitly having to close the program.
I then split the lines in the file into words and the words into letters so that python would read over each individual letter and keep a count of the letter specified by the user.
This count is then returned to the user.

## week8
Write a program that displays a plot of 3 functions.
numpy and matplotlib were imported.
NumPy is a package that can be used with python when working with arrays and matplotlib is a python plotting library.
first I defined an array with NumPy and stored it in the variable x.
I then used matplotlib to plot x, x squared and x cubed.
I inserted axis labels, a graph title and a legend









