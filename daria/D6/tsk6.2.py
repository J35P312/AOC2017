import pandas as pd
import copy


df = pd.read_csv('input.txt', delimiter='\t', header=None)
df_list = df.loc[0,:].values.tolist()
memory = [int(x) for x in df_list]

 
def main():

    loops = 0
    memories = ([copy.copy(memory)])

    while True:
        max_val = max(memory)
        max_val_index = memory.index(max_val)
        memory[max_val_index] = 0
        index = max_val_index + 1


        while max_val > 0:
            
            if index < len(memory):
                memory[index] += 1
                max_val -= 1
                index += 1
                
            elif index >= len(memory):
                index = 0
                memory[index] += 1
                index += 1
                max_val -= 1


        loops+=1


        if memory[:] not in memories:
            memories.append(memory[:])

        else:
            print('LOOPS =', loops)
            memories.append(memory[:])

            index1 = memories.index(memory[:])
            start = index1 + 1
            index2 = memories.index(memory[:], beg)
            result = index2 - index1
            print(result)
            break
main()
