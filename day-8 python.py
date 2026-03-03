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
                        set_lst = list(set(existing_letters))
                        num_elements = len(set_lst)

    print(set_lst, num_elements)


calculate_love_score("Anele", "Anele")