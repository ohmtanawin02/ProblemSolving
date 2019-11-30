def main():
    Read_line()
    Read_Sentense()
def Read_line():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readline = infile.read()
    infile.close()
    result = 0
    for i in readline:
        if i == "\n":
            result = result + 1
        else:
            pass
    print(result)
def Read_Sentense():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readsentense = infile.read()
    infile.close()
    read_splitdot = readsentense.split(".")
    print(read_splitdot)
main()
            