def count_words(book_text):
    words = book_text.split()
    return len(words)    

def get_chars_dict(text):
    chars ={}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    return chars