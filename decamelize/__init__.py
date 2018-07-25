import re

def convert(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
