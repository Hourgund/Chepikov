eng_words = ["computer", "scanner", "printer",
             "speaker", "keyboard", "mouse",
             "motherboard"]

rus_words = ["компьютер", "сканер", "принтер",
             "колонки", "клавиатура", "мышь",
             "материнская плата"]

index = eng_words.index("mouse")
print(rus_words[index])

# { key : value } --> item
dictionary = {"computer": "компьютер",
              "scanner": "сканер",
              "printer": "принтер",
              "speaker": "колонки",
              "keyboard": "клавиатура",
              "mouse": "мышь",
              "motherboard": "материнская плата"}

# print(type(dictionary))
# print(dictionary)
print(dictionary["mouse"])