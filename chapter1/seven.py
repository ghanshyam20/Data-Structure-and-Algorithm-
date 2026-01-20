def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for ch in text:
        ch = ch.lower()
        if ch in reference_string:
            result.append(reference_string.index(ch))
        else:
            result.append(-1)

    return result


text = input("enter string ")   # i have add this to see here in terminal so slighlyt modification of code than in moodle.hope you will excuse me ..
print(custom_encoder(text)) 




