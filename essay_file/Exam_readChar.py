def main():
    Read_character()
    line()
def Read_character():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Example.txt",'r')
    readcharacter = infile.read()
    infile.close()
    read_charlen = len(readcharacter)
    print(read_charlen)
def line():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/example.txt",'r')
    line1 = infile.read()
    infile.close()
    result = len(line1.splitlines())
    print(result)
main()