#Cryptarithm Solver

Question: Given the word addition problem with no access to wikipedia:

      SEND
    + MORE
    ------
     MONEY

How do you solve it?
Answer: With this python library

##Examples

    from cryptarithm import solver
    
    vals = solver("send", "more", "money")
    print vals #=> (9567, 1085, 10652)

## Running the tests

Because every good project needs tests:

    $ python test_equation.py
