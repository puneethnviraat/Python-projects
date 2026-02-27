import random

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Stay hungry. Stay foolish. – Steve Jobs",
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "Do or do not. There is no try. – Yoda",
    "It always seems impossible until it's done. – Nelson Mandela",
    "Knowladge,money,time. - jackie"
    # ...add more quotes here!
]

print("💬 Welcome to the Quote Machine!")
quote = random.choice(quotes)
print("✨ Here's your quote:")
print("👉 {}".format(quote))  # or use: print(f"👉 {quote}")