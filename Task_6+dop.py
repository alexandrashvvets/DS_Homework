# def high_word(text):
#     word = text[0].upper()+text[1:].lower()
#     return word
#
# text = input('Vvedite slovo:')
# print(high_word(text))

def high_word(text):
    word = text[0].upper()+text[1:].lower()
    return word

string = str(input('Vvedite slovo:'))
for word in string.split(' '):
    print(f'{high_word(word)}', end=' ')