#1-masala
for i in range(1, 21):
     print(i)

#8-masala
word = "Python"
print(f"To'liq so'z: {word}")

for letter in word:
    print(letter)

#16-masala
name = ["Ali", "Vali", "Sardor", "Madina", "Aziza", "Anvar"]
print(name)

a_ismlar = [ism for ism in name if ism[0] == "A"]
print(f"A harfidan boshlanadigan ismlar: {a_ismlar}")

#23-masala
student = {
     "ism": "Ali",
     "yosh": 15,
    "sinf": 9
}
print(student)

#32-masala
def salom_ber(ism):
      print(f"Salom, {ism}")

salom_ber("Ali")
