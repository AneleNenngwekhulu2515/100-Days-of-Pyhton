existing_letters =[]
def calculate_love_score(name1, name2):

    word_list = ["LOVE", 'TRUE']
    count = 0
    for word in word_list:
        for char in word:
            for n in name1.upper().strip():
                for i in name2.upper().strip():
                    if char == n  and char == i:
                        count += 1
                        existing_letters.append(i)
                        existing_letters.append(n)
                        set_lst = list(set(existing_letters))
                        num_elements = len(set_lst)

    print(existing_letters, count)


calculate_love_score("Anele", "nombulelo")


print(r"""
   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                               | |                    
                                               |_|                    
""")

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]



# todo 1: create a function called encrypt that takes original_text and
#  shift_amount as 2 inputs

# todo 2: Inside the encrypt function, shift each letter of the original_text
#  forwards in the alphabet by the shift_amount and print the encrypted text

def encrypt(original_text, shift_amount):
    indexes = []
    result = []
    for n in original_text.lower():
        if n in alphabet:
            shifting = alphabet.index(n) + shift_amount
            indexes.append(shifting)
        else:
            result.append(n)

    print(f"Shifted indexes: {indexes}")
    for i in indexes:
        i = i % len(alphabet)
        result.append(alphabet[i])
    print(f"Shifted list: {result}")
    text = "".join(result)
    print(f"Final encoded word is : {text}\n")

# encrypt("Nombulelo", 7)


def decrypt(original_text, shift_amount):
    indexes = []
    result = []
    for n in original_text.lower():
        if n in alphabet:
            shifting = alphabet.index(n) - shift_amount
            indexes.append(shifting)
        else:
            result.append(n)

    print(f"decrypted indexes: {indexes}")
    for i in indexes:
        i = i % len(alphabet)
        result.append(alphabet[i])
    print(f"Decrypted list: {result}")
    text = "".join(result)
    print(f"Final Decrypted word is : {text}\n")

# decrypt("uvtibslsv", 7)

def ceasar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt(), type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower().strip().replace(' ', '')
    shift = int(input("Type the shift number:\n"))


    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction )
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Thank you for playing! GOODBYE!")
    elif restart == "yes":
        should_continue = True
