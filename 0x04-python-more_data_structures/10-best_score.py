#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        lista_tup = [(value, key) for key, value in a_dictionary.items()]
        return max(lista_tup)[1]
