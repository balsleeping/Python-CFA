#!/usr/bin/env python

import random

def main():
    """start a guessing genre music between "electro", "jazz", "classic", "funk", "opera", "grunge"."""
    print("gueses the genre music")
    
    x = random.choice("genre")
    guess = None
    
    while x !=guess:
        
        guess = str(input("pick a music genre :DD"))
        
        if x ==guess:
            print("noice")
        else:
            print("try againn")
main()