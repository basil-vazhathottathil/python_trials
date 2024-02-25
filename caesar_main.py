alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#to not get a error when last alphabets are used in text,
#it seems just duplicating the elements once more in alphabet works, idk :-o
#numbers ,symbols and  spaces are preserved
#for gods sake dont use uppercase because i am to lazy to consider that scenario

def caesar(shift,text):
    end_text=""
    if( choice=="decode"):
        shift *=-1 
    for char in text:
        if char in alphabet:
            position =alphabet.index(char)
            new_position= (position +shift)%26
            end_text +=  alphabet[new_position]
        else:
             end_text += char
        
    if choice=="encode":
            print(f"Encoded message is {end_text}") 
    else :
            print(f"The decrypted code is {end_text}")


run_again= True
while run_again:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice != "encode" and choice != "decode" :
         print("invlaid choice")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
       
        caesar(shift,text)
        
    query= input("do you want to continue(Y /N)").lower()
    if query=="n":
         run_again=False
