def main():
    Read_line()
    Read_Sentense()
    Read_Word()
    Read_character()
    Char_upper()
    Char_lower()
def Read_line():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readline = infile.read()
    infile.close()
    result = len(readline.splitlines())
    print(result)
def Read_Sentense():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readsentense = infile.read()
    infile.close()
    read_splitdot = readsentense.split(".")
    print(len(read_splitdot))
def Read_Word():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readword = infile.read()
    infile.close()
    read_wordsplit = readword.split()
    print(len(read_wordsplit))
def Read_character():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    readcharacter = infile.read()
    infile.close()
def Char_upper():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    read_upper = infile.read()
    infile.close()
    result = 0
    for i in read_upper:
        if i.isupper() == True:
            result = result + 1
        else :
            pass
    print(result)
def Char_lower():
    infile = open("/Users/again/Desktop/GIT/ProblemSolving/essay_file/Loop.txt",'r')
    read_lower = infile.read()
    infile.close()
    result = 0
    for i in read_lower:
        if i.islower() == True:
            result = result +1
        else :
            pass
    print(result)
main()
            