#Day3-Challenge-3
# Day 3 – Daily Python Challenge 🐍
# 🚀 Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime number hai ya nahi! 🔢💡
# 🔥 Example:
# 📌 Input: 7
# 📌 Output: Yes, it's a prime number!
# 📌 Input: 10
# 📌 Output: No, it's not a prime number!
# Hint:
# 1️⃣ Prime Number wo hota hai jo sirf 1 aur apne aap se divisible ho.
# 2️⃣ Tum loops (for/while) aur modulus operator (%) ka use kar sakte ho.
# 3️⃣ Edge Cases: 1 aur negative numbers prime nahi hote!


num =int (input("Enter a number!"))

if num < 2 :

    print("No It's not a pime number")


for i in range(2, num):
   if num % i == 0:
       print("No, Its not a prime number")
       break
else:
      print("Its a prime number!")
