def read_input(file):
    with open(file,'r') as f:
        content = f.readlines()
    return(content)

def main():
    print (read_input("input_1.txt"))

main()
