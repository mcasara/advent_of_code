def read_input(file, type):
    content = []
    with open(file,'r') as f:
        if type == 'float':
            for line in f:
                try:
                    content.append(float(line.strip('\n')))
                except:
                    content.append('null')
        elif type == 'int':
            for line in f:
                try:
                    content.append(int(line.strip('\n')))
                except:
                    content.append('null')
        else:
            for line in f:
                content.append(line.strip('\n'))
    return(content)

def sum_list_with_null(l):
    sum_dict = {0:0}
    i=0
    for amount in l:
        if amount == 'null':
            i+=1
            sum_dict[i] = float(0)
        else:
            sum_dict[i]+=amount
    return sum_dict

def main():
    liste= sum_list_with_null(read_input("1/input_1.txt", 'float'))
    return(print( max(liste.items(), key=lambda k: k[1])))

if __name__ == "__main__" :
    main()
