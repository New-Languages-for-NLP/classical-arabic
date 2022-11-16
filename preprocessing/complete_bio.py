###################################################################
# Complete BIO | by Maroussia Bednarkiewicz
###################################################################

import os

###################################################################
# Add the annotation O (for Other) to manually annotated files
###################################################################
# Coments: I found it easier to annotate some relatively `short`
# files manually without the help of a software. In shuch cases
# I only annotated the B (Beginning) and the I (Inside) for each
# relevant token, and left empty the tokens which should get the
# O (Outside) tag. This code adds the tag O to all empty spots.
###################################################################

def add_O(path_to_input:str, path_to_output:str):
    """Takes the file given in `path_to_input`, which is in the CONLL format,
    i.e. token-whitespace-(tag)-newline, and has been annotated by hand with
    only B (Beginning) and I (Inside) but does not have the O (Outside) tag
    following the BIO tag format.
    Add the tag O (Outside) after all tokens that have not been tagged.
    Write the results, a file with full BIO annotations, on the file given
    by `path_to_output` (which can be the same as the input or not).
    """
    with open(path_to_input, 'r') as in_:
        text = in_.readlines()
    
    res = []
    
    for string in text:
        if len(string.split()) == 1:
            token = string.split('\n')[0] # select the word token
            tag_token = f"{token} O" # preserves the word token and adds the tag
        else:
            tag_token = string.split('\n')[0]
        
        res.append(tag_token)
    
    with open(path_to_output, 'w') as out:
        out.write('\n'.join(res))