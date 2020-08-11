#                     EXERCISE 4
######PATTERN PRINTING######
""" input = integer
    boolean = true / false

TRUE N = 4
*
* *
* * *
* * * *

FALSE N = 4
* * * *
* * *
* *
*

"""
print("Enter number of rows.")
rows = int(input())
print("Enter Boolean value [1 or 0]")
boolean = int(input())
i = 1
if boolean == 1:
    while i <= rows:
        print(i * "* ")
        """, i * " ", i * "*", i * " ", i * "*", i * " ", i * "*",
        i * " ", i * "*", i * " ", i * "*", i * " ", i * "*", i * " ", i * "*"
        , i * " ", i * "*", i * " ", i * "*", i * " ", i * "*", i * " ", i * "*"
        , i * " ", i * "*", i * " ", i * "*", i * " ", i * "*", i * " ", i * "*" """
        i = i + 1
        continue

if boolean == 0:
    while rows >= 1:
        print(rows * "* ")
        """, rows* " ", rows * "*", rows* " ", rows * "*", rows* " ", rows * "*"
        , rows* " ", rows * "*", rows* " ", rows * "*", rows* " ", rows * "*", rows* " "
        , rows * " ", rows * "*", rows* " ", rows * "*", rows* " ", rows * "*" """
        rows = rows - 1
        continue



