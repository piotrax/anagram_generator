#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Anagram generator
# English dictionary from page: http://wiki.puzzlers.org/pub/wordlists/unixdict.txt

def is_anagram(phrase1: str, phrase2: str) -> bool:
    '''
    Function checks phrases for anagrams.
    Function needs two arguments of string type.
    Function returns a logical value true or false.
    '''
    try:
        list1 = sorted(phrase1.replace(' ','').lower()) # 1st phrase format
        list2 = sorted(phrase2.replace(' ','').lower()) # 2nd phrase format
        if list1 == list2:
            return True
        return False
    except Exception as ex:
        return f'Error: {ex}'


def anagram_generator(phrase: str, my_dict: list) -> str:
    '''
    Function displays anagrams for the given expression.
    Function needs two arguments:
        1st arg - phrase of string type
        2nd arg - dictionary of list type
    '''
    for word in my_dict:
        if is_anagram(phrase, word.replace('\n','')):
            print(word.replace('\n',''),end=', ',flush=True)


def main():
    from itertools import combinations
    import sys
    
    my_file = open('unixdict.txt','r')
    my_dict = my_file.readlines()
    my_file.close()
    print(type(my_dict))
    
    phrase = list(sys.argv[1]) # input phrase as argument
    all_combinations = [''.join(combination) for item in range(len(phrase)) for combination in combinations(phrase, item+1)] # list of tuples as list of strings
    all_combinations = all_combinations[::-1]
    
    for item in all_combinations:
        if len(item) > 0:
            anagram_generator(item, my_dict)
 
 
if __name__ == '__main__':
    main()