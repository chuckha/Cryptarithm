#Cryptarithm Solver

Question: Given the word addition problem with no access to the internet:

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


## Todo

* Implement an algorithm that does not take 10000000000 (10^10) comparisons
