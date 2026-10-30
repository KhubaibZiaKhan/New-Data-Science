import nltk
from nltk.chat.until import chat, reflection

reflection = {
    "You "     : "me",
    "You are " : "I am",
    "I'd "     : "You would",
    "I'll"     : "You",
    "I "       : "You Are",
    "I was "   : "You Are",
}

pairs = [
    [
        r"My Name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
            r"hi|hey|hello",
            ["Hello", "Hey there",]
    ]
    [
            r"How are You ?",
            ["I am doing good how about you ?",]
    ]
    [
            r"sorry(.*)",
            ["Its alright","Its ok,never mind",]
    ]
    [
            r"quit",
            ["Bye Take Care,See You soon :)",]
    ]
    [
            r"Favourite car (.*)",
            ["Bmw M4", "Mayback", "Toyota Supra"]
    ]

]

def chat():
    print("Hi I am A chatbot created by Khubaib Zia Khan For your Service")
    chat = Chat(pairs,reflection)
    chat.converse()
if __name__ == "__main__":
    chat()