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


calculate_love_score("Anele", "kyle")


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

direction = input("Type 'encode' to encrypt(), type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# todo 1: create a function called encrypt that takes original_text and
#  shift_amount as 2 inputs

# todo 2: Inside the encrypt function, shift each letter of the original_text
#  forwards in the alphabet by the shift_amount and print the encrypted text

def encrypt(original_text, shift_amount):
    indexes = []
    result = []
    for n in original_text.lower():
        shifting = alphabet.index(n)+shift_amount
        indexes.append(shifting)

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
        decrypted = alphabet.index(n)-shift_amount
        indexes.append(decrypted)

    print(f"decrypted indexes: {indexes}")
    for i in indexes:
        i = i % len(alphabet)
        result.append(alphabet[i])
    print(f"Decrypted list: {result}")
    text = "".join(result)
    print(f"Final Decrypted word is : {text}")

# decrypt("uvtibslsv", 7)

def ceasar(original_text, shift_amount, direction):
    if direction == "encode":
        encrypt(original_text, shift_amount)
    elif direction == "decode":
        decrypt(original_text, shift_amount)

ceasar("hulsl", 7, "decode")
