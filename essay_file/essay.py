def main():
    Read_line()
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
main()
            