###################################################################
# Invert CONLL | by Maroussia Bednarkiewicz
###################################################################

import os
import pandas as pd

###################################################################
# Invert the positions of token and tag in a CONLL file
###################################################################

def inv_conll(path_to_folder:str):
    """Takes a folder with files in the format .conll
    i.e. token-whitespace-tag-newline
    and invert the order token/tag to tag/token
    or the other way around depending on original order.
    A new file is generated for each file processed,
    the filename is the same except that it starts with `NEW-`.
    Remove `NEW-` in the last line to automatically 
    replace the original file in the folder. 
    """

    for root, dirs, files in os.walk(path_to_folder, topdown=False):
        for f_name in files:
            with open(os.path.join(root, f_name), 'r') as wrapper:
                text = wrapper.read()

                # Invert the order of each tuple (token, tag) --> (tag, token)
                new = [tuple(t.split())[::-1] for t in text.split('\n')]
                
                df = pd.DataFrame.from_records(new)
                
                # Export the new content to a file with the same format
                df.to_csv(os.path.join(path_to_folder,
                                        f"NEW-{f_name}"),
                                        sep=' ', 
                                        index=False,
                                        header=False)

