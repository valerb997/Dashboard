import docx2txt
my_text = docx2txt.process("DESCRIPTION OF THE PROJECT 3.docx")

s="\n"
for i in range(5):
    s=s+"\n"
    my_text=my_text.replace(s, '\n')
new = list(filter(None, my_text))
str=""
for c in new:
    str=str+c
str=str.split("\n")
#25
print(str[75])