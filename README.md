# Project:- Checkout System
## _Description_
    This project is a checkout system with having the option of changing the price of items in minimal time. It also includes opening day sale logic. 


## Features

- Pricing of all the items are stored in DB(here csv) which can be changed on the fly without touching the code
- This package contains a test case file which is having multiple test cases.
- As the format of input was not mentioned specifically, I have taken the input in form of a string and each SKU are separated by a comma(,).
- This package contains 6 files.
    1. Total_cost:- This code is having all the business logic
    2. price_reader.py:- This code reads the price of each item from CSV
    3. Price.CSV:- This file contains the list of item with price details
    4. user_input.py:- This code is to take input from the user 
    5. test_case.py:- Different test cases are written in this file for testing purpose
    6. readme:- This file gives details about the code and setup process


## Tech

Code is written in Python 3.

## Setup and Run
Please follow the steps to run the code:-
1. Install Python 3 in the system.
2. you can use any IDE for this. (I have used PyCharm to develop this code)
3. Pull the file from Git
4. Make sure all  files are in the same path (folder) while running the code
5. To pass your input set, run user_input.py. Then it will ask for an input bar code. Please give all your SKU separated by a comma. There should be no space between 2 SKUs. only separate it by a comma.
6. To run test cases please run test_case.py


## Changing the price of any item
Open price.csv and update  column C of the item for which price needs to be changed.

## Different test cases in test_case.py file
There are 5 different test cases written in this file:-
1. SKUs Scanned:atv,atv,atv,vga Total expected: $249.00
2. SKUs Scanned:atv,ipd,ipd,atv,ipd,ipd,ipd Total expected: $2718.95
3. SKUs Scanned:mbp,vga,ipd Total expected: $1949.98
4. Passing valid and invalid SKU: it will give an invalid input warning and give the cost of the remaining item
5. passing all invalid SKUs, will give a warning for invalid SKU and total cost at zero


## Exception Handling:-
1. If the wrong SKU is passed in input, code will show the error "XXX  is not a valid SKU, please check the spelling or extra whitespace"
2. It will still do the calculation for all the valid SKUs.

**Addition of new item in the list (CSV)**
I was not aware of this can be a condition to add a new item to the list,
So this condition is handled in a different package named as checkout System secondary code.
This package I will share separately
