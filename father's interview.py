# Father Interview Chatbot

qa = {
    1: "My name is Zahid Islam and I was born in 1978.",
    2: "I was born and raised in Mian Channu.",
    3: "My childhood was very good. I enjoyed spending time with family and friends.",
    4: "I completed BSC Commerce from Government College Mian Channu.",
    5: "My father inspired me the most in my life.",
    6: "I started as a garments shopkeeper in Mian Channu and later started my own garment manufacturing business.",
    7: "I have been running this business for 15 years.",
    8: "We manufacture undergarments and tracksuits.",
    9: "We get raw materials from Faisalabad.",
    10: "Garment shopkeepers are our main customers.",
    11: "Managing the business is the biggest challenge, so I run it in partnership with my friends.",
    12: "I started with one machine and one worker. Now we have more than 100 machines and workers.",
    13: "Good quality is the key to success in this industry.",
    14: "I have been involved in farming for about 30 to 35 years.",
    15: "We usually grow wheat and cotton.",
    16: "We have our own land, so I continue farming along with my business.",
    17: "High fertilizer and water costs are major challenges for farmers.",
    18: "Technology helps improve crop production and yields.",
    19: "Wheat and cotton are the most profitable crops for me.",
    20: "I spend time with my family to overcome stress.",
    21: "Keep trying and one day you will become successful.",
    22: "My family has played an important role in my success.",
    23: "Education is very important in both professional and practical life."
}

print("=== Father Interview Chatbot ===")
print("Type a question number (1-23)")
print("Type 0 to exit")

while True:
    user_input = int(input("\nEnter Question Number: "))

    if user_input == 0:
        print("Goodbye!")
        break

    elif user_input in qa:
        print("Answer:", qa[user_input])

    else:
        print("Question not found!")