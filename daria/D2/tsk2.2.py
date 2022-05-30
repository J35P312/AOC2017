import pandas as pd


def main(filename):
    col_names = list(map(chr, range(ord('a'), ord('p')+1)))
    df = pd.read_csv(filename, sep = '\t', names = col_names)

    even_devison_result = 0

    for row in df.itertuples():
        for i in row[1::]:
            for j in row[1::]:
                if i != j and i % j == 0:
                    even_devison_result += i // j
                
    print(even_devison_result)

main('input.txt')
