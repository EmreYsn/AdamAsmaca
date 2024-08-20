import random

def select_words():
    words = ["telefon","bilgisayar"]
    return random.choice(words)

def adam_asmaca():
    word = select_words()
    word_letters = set(word)
    true_letters = set()
    predicted_letters = set()
    life_number = 6

    while len(word_letters) > 0 and life_number > 0:
        print(f"Kalan can hakkınız : {life_number}")
        print("Tahmin ettiğiniz harfler : " , "".join(predicted_letters))

        word_appearance = [letter if letter in true_letters else "_" for letter in word]
        print("Kelime : " , "".join(word_appearance))

        guess = input("Bir harf tahmin ediniz : ").lower()

        if guess in predicted_letters:
            print("Bu harfi zaten tahmin ettiniz.")
        elif guess in word_letters:
            true_letters.add(guess)
            word_letters.remove(guess)
            print("Doğru Tahmin!!")
        else:
            life_number -= 1
            print("Yanlış Tahmin!!")

        predicted_letters.add(guess)

    if life_number == 0:
        print(f"Kaybettiniz!! Doğru kelime : {word}")
    else:
        print(f"Kazandınız!! Tahmin etmiş olduğunuz gibi doğru kelime : {word}")

if __name__ == "__main__":
    adam_asmaca()

