

#f = open(path_to_file, mode)
import pandas as pd
import os
data = {'first_column':  ['first_value', 'second_value', ...],
        'second_column': ['first_value', 'second_value', ...],
        }

df = pd.DataFrame(data)
with open('readme.txt', 'w') as f:
    f.write(df)