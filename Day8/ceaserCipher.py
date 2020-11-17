import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo+"\n\n")

def ceaser(text,shift,direction):
    newText=""
    for i in range(len(text)):
        if(text[i] in alphabet):
            if(direction=="encode"):
                pos = alphabet.index(text[i])-shift
            else:
                pos = (alphabet.index(text[i])+shift) % 26
            newText += alphabet[pos]
        else:
            newText += text[i]

    print(f"The {direction}d Text is : {newText}")

run_code = "yes"
while(run_code=="yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction =="encode" or direction=="decode":
        ceaser(text,shift,direction)
    else:
        print("Please Enter A Valid Input")
    
    run_code = input("\nTo run the code again type 'yes' otherwise type 'no'.")
    print("\n\n")

print("GOODBYE!!")