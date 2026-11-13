def count_vowels_and_consonants(text: str) -> dict:
    
  

    sumu = 0
    sumn = 0

    for i in text:
        if i in "aeiou":
            sumu += 1
        elif i.isalpha():
            sumn += 1

    return {
        "unlilar": sumu,
        "undoshlar": sumn
    }

print(count_vowels_and_consonants("Salom Dunyo!"))