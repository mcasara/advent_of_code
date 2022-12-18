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
            sum_dict[i] = int(0)
        else:
            sum_dict[i]+=amount
    return sum_dict

def main():
    dict1= sum_list_with_null(read_input("1/input_1.txt", 'int'))
    sorted_dict = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
    return(print(f"Part1: {sum([k[1] for k in list(sorted_dict.items())[:1]])} \nPart2 : {sum([k[1] for k in list(sorted_dict.items())[:3]])}"))

if __name__ == "__main__" :
    main()
