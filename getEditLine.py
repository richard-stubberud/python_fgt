import re
def main():
    #read file
    file = open('putty.log')
    lines = file.readlines()
    f = open("result.txt", "w")

    #look for patterns

    for line in lines:
        line = line.strip()
        if re.match("(.*)edit(.*)",line):
            print (line, file=f)




main()
