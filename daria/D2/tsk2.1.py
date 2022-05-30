import pandas as pd
import string

colnames = list(map(chr, range(ord('a'), ord('p')+1)))
my_df = pd.read_csv('input.txt', sep = '\t', names = colnames)
print(my_df)


max_element = my_df.max(axis=1)
min_elememt = my_df.min(axis=1)
diff = max_element - min_elememt
                
print(diff.sum())



