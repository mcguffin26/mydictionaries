codes = {'A':'%', 'a':'9', 'B':'!', 'b':'(', 'C':'X', 'c':'?', 'D':':', 'd':'&', 'E':'+', 'e':'#', 'F':'^', 'f':'K', 'G':'w', 'g':'Z', 'H':'*', 'h':'<', 'I':'>', 'i':',', 'J':'=', 
        'j':'F', 'K':'a', 'k':';', 'L':'-', 'l':'G', 'M':'7', 'm':'2', 'O':'1', 'o':'3', 'P':'q', 'p':'Q', 'Q':'t', 'q':'y', 'R':'v', 'r':'#', 'S':'%', 's':'@', 'T':'_', 't':'^', 
        'U':'t', 'u':'.', 'V':'&', 'v':'*', 'W':'{', 'w':'}', 'X':'p', 'x':'B', 'Y':'/', 'y':'?', 'Z':'|', 'z':'K'}

infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')


for word in infile:
    word = word.strip()

infile.close()

for character in word:
    if character in codes:
        outfile.write(codes[character])
    else:
        outfile.write(character)

outfile.close()