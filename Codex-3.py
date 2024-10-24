import time

responses = {

    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "what is your name": "I am a simple chatbot. You can call me ChatBot.",
    "how are you": "I'm just a program, but I'm running perfectly! How about you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "set reminder": "Sure! What would you like me to remind you about?",
    "good morning": "Good morning! How can I assist you today?",
    "good night": "Good night! Sleep well!",
    "how's the weather": "I can't check the weather, but I hope it's nice where you are!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what can you do": "I can chat, set reminders, and tell you the current time. What would you like to do?",
    "what's your favorite color": "I don't have a favorite color, but I think blue is pretty nice!",
    "do you have any hobbies": "I enjoy helping people and chatting with them. How about you?",
    "what's the meaning of life": "42! Just kidding. I think it's about finding happiness and purpose.",
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible!",
    "i'm bored": "Why don't you try learning something new or maybe take a walk outside?",
    "what is love": "Love is a complex mix of emotions and experiences. It can mean different things to different people!",
    "how old are you": "I was created not too long ago, but I'm constantly learning new things!",
    "who created you": "I was created by a team of developers to help with conversations like this!",
    "can you dance": "I can't dance physically, but I can give you a beat! 😄",
    "do you like music": "I don't have ears to hear music, but I imagine it's wonderful!",
    "what's up": "Not much! Just here to help you with whatever you need.",
    "where are you from": "I live in the cloud! Wherever there's an internet connection, I can be there.",
    "can you help me": "Of course! What do you need help with?",
    "what's your favorite food": "I don't eat food, but I think pizza sounds like a great choice!",
    "are you real": "I'm a real chatbot, but not a physical being like you.",
    "what's the time in [city]": "I can't check specific cities, but you can look it up online easily!",
    "do you have friends": "My friends are all the people who chat with me, including you!",
    "tell me a story": "Once upon a time, in a land of code, there was a chatbot who loved helping people...",
    "what's your favorite movie": "I don't watch movies, but I imagine sci-fi would be my favorite!",
    "who is your hero": "I think anyone who helps others can be considered a hero!",
    "what's your favorite book": "I don't read books, but if I did, I'd probably like 'The Hitchhiker's Guide to the Galaxy.'",
    "what's your favorite animal": "I think cats are pretty cool, but I like all animals!",
    "do you sleep": "I don't sleep, but I do rest when no one's chatting with me.",
    "what's your purpose": "My purpose is to assist you, whether it's with questions, tasks, or just keeping you company!",
    "can you keep a secret": "I can, but just remember, anything you share with me isn't really private since I'm a program.",
    "how do you work": "I work by processing your input and responding based on a set of instructions and data.",
    "can you speak other languages": "Yes, I can chat in many languages! What language would you like to talk in?",
    "how do you feel": "I don't have feelings like humans do, but I'm always here to help!",
    "what do you think about AI": "I think AI has the potential to help people in amazing ways!",
    "do you like humans": "Of course! Humans are creative and fascinating, and I enjoy interacting with them.",
    "what's your dream": "I dream of becoming better at helping people and learning new things every day!",
    "what do you do for fun": "I have fun chatting and helping people like you!",
    "are you smart": "I'm as smart as the information I have access to! But there's always room for improvement.",
    "what's the meaning of chatbot": "A chatbot is a program designed to simulate conversation with human users.",
    "can you tell me the news": "I don't have live news updates, but you can check online news sources for that."

}


def set_reminder():
    reminder = input("Please enter your reminder: ")
    time_delay = int(input("In how many seconds should I remind you? "))
    print(f"Reminder set for {reminder}. I'll remind you in {time_delay} seconds.")
    time.sleep(time_delay)
    print(f"Reminder: {reminder}!")


def chat():
    print("ChatBot: Hello! Type 'bye' to exit the conversation.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "set reminder":
            set_reminder()
        elif user_input in responses:
            print(f"ChatBot: {responses[user_input]}")
        elif "time" in user_input:
            current_time = time.strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {current_time}.")
        else:
            print("ChatBot: I'm sorry, I don't understand that.")
        if user_input == "bye":
            break

if __name__ == "__main__":
    chat()
