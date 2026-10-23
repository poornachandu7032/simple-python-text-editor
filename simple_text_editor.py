lines=[]
try:
    file_name=input(" Enter the filename to open or create : ");
    with open(file_name,"r") as file:
        content=file.read()
        print(content)
        
except FileNotFoundError:
    print(f"{file_name} not found.Creating a new file");

print(" Enter your text (Type SAVE on a new line to save and exit) : ")
#collect the lines
while True:
    line=input()
    if line == "SAVE":
        break
    lines.append(line)
#write into the file
with open(file_name,"a") as file:
    for line in lines:
        file.write(line+"\n")
            





