"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-09-18"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


Principal = float(input("Principal:"))
Interest = float(input("Interest (%):"))
Years = int(input("Number of years:"))
compounded = int(input("Number of times interest compounded per year:"))

AIntrest = Interest*100
balance = Principal*(1+(AIntrest/compounded)**(compounded*Years))
print(f"Balance: $ {balance}")
