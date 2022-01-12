import os
import re

def clean(path_to_original, path_to_clean, regex, replacement):
    '''
    Opens `path_to_original` (= path to the original text that needs to be cleaned);
    replaces all the matches of the `regex` with the given `replacement`;
    pastes the cleaned text in `path_to_clean` (= new path to the clean text 
    or same path as the original text which will be then replaced);
    prints the lengths of texts before and after cleaning (optional).
    '''
    with open(path_to_original, 'r+') as wrapper:
        text = wrapper.read()
        print('length_1:', len(text.split()))
    new_text = re.sub(regex, replacement, text)
    print('length_2:', len(new_text.split()))

    with open(path_to_clean, 'w') as new_wrapper:
        new_wrapper.write(new_text)