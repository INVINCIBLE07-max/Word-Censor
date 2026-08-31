censoredWords = []
# numberByuser = int(input("Enter the number of words you want to censor : "))

# for i in range(1,numberByuser+1):
while True:
    a = input("enter the censord words as per you ")

    if a == "":
        break

    else:
        censoredWords.append(a)


with open("censor.txt","r") as f:
    i=0
    d = f.read()
    for i in range (len(censoredWords)):
        if censoredWords[i] in d:
            print(f"file contains censord word : {censoredWords[i]}")
            n = input("Do you want to replace that word ? ")
            if (n.lower()=="yes" or n.lower()=="yep" or n.lower()=="y"):
            # if "yes" or "yep" or "y" in n.lower():  
                with open("censor.txt","w") as f:
                    userinput = input("enter the word you want to replace it with : ")
                    repstore = d.replace(censoredWords[i] , userinput)
                    f.write(repstore)
                    print(f"your have successfully replaced {censoredWords[i]} with {userinput}")
        else:
            print("all good")


