#Name: Dante Rivera
#Date: August 27th, 2018
#This program returns the length of an ACTG string, and the percentage of the string that is g or c


dna_str = input('Enter a DNA string:       ')




# Returns the number of occurances of "G" and "C" in given string
def gc_counter(string):
    gc = 0
    for i in string:
        if i == "G" or i == "C":
            gc += 1
    return gc

def gc_perc(string, gc_count):
    lenny = len(string)
    perc = gc_count / lenny

    print('Length is :', lenny, '\n')
    print('GC-content is', round(perc, 2))




gc_perc(dna_str, gc_counter(dna_str))
