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


caesar_art = r"""
   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                               | |                    
                                               |_|                    
"""