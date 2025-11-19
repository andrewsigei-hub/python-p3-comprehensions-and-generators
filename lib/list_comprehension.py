#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    return [strings + "!" for strings in sentence_list]

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
    
