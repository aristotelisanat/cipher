import string

def caesar_encode(message, offset):
    alphabet = string.ascii_lowercase
    encoded = ""
    for char in message.lower():
        if char in alphabet:
            index = (alphabet.index(char) + offset) % 26
            encoded += alphabet[index]
        else:
            encoded += char
    return encoded

def caesar_decode(message, offset):
    return caesar_encode(message, -offset)

def vigenere_encode(message, keyword):
    alphabet = string.ascii_lowercase
    keyword = keyword.lower()
    keyword_index = 0
    encoded = ""
    for char in message.lower():
        if char in alphabet:
            shift = alphabet.index(keyword[keyword_index])
            index = (alphabet.index(char) + shift) % 26
            encoded += alphabet[index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encoded += char
    return encoded

def vigenere_decode(message, keyword):
    alphabet = string.ascii_lowercase
    keyword = keyword.lower()
    keyword_index = 0
    decoded = ""
    for char in message.lower():
        if char in alphabet:
            shift = alphabet.index(keyword[keyword_index])
            index = (alphabet.index(char) - shift) % 26
            decoded += alphabet[index]
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            decoded += char
    return decoded

# Task 1: Decode Vishal's first message
vishal_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_message = caesar_decode(vishal_message, 10)
print("Decoded message:")
print(decoded_message)

# Task 2: Encode a reply to Vishal
reply = "Hello Vishal! I successfully decoded your message. This Caesar Cipher is really cool!"
encoded_reply = caesar_encode(reply, 10)
print("\nEncoded reply:")
print(encoded_reply)

# Task 3: Decode Vishal's two new messages
message1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

decoded_message1 = caesar_decode(message1, 10)
print("\nDecoded first message:")
print(decoded_message1)

decoded_message2 = caesar_decode(message2, 14)
print("\nDecoded second message:")
print(decoded_message2)

# Task 4: Brute force to decode Vishal's message
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for offset in range(26):
    decoded = caesar_decode(brute_force_message, offset)
    if "computers" in decoded:
        print(f"\nBrute force decoded message (offset {offset}):")
        print(decoded)
        break

# Task 5: Decode Vishal's Vigenère Cipher message
vigenere_message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
vigenere_keyword = "friends"

decoded_vigenere = vigenere_decode(vigenere_message, vigenere_keyword)
print("\nDecoded Vigenère Cipher message:")
print(decoded_vigenere)

# Task 6: Encode a message using Vigenère Cipher
final_message = "Vishal, I've mastered both the Caesar and Vigenère Ciphers. Let's find an even more secure method!"
final_keyword = "python"

encoded_final = vigenere_encode(final_message, final_keyword)
print("\nFinal encoded message:")
print(encoded_final)

# Bonus: Decode the final message to verify
decoded_final = vigenere_decode(encoded_final, final_keyword)
print("\nDecoded final message (verification):")
print(decoded_final)
