def duplicate_count(text):
    list_char = list(text.lower())
    total_repeat=0

    for index_char in set(list_char):
        if list_char.count(index_char) > 1:
            total_repeat+=1
            
    return print(total_repeat)
        
duplicate_count('9XVEWmVpJVnSaTrTGuYfSMfTzP0yiDH7stzRP44weVcQbPJ4X54ytjGf77yyHQ245hR5i')