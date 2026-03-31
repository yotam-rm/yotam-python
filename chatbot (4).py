import random

# --- שלב 1: הגדרות ונתונים (Variables & Lists) ---
bot_name = "Neo"

greetings = [
    "Hello!",
    "Hi there!",
    "It's nice to meet you.",
    "Hey!",
    "Welcome!"
]

goodbyes = [
    "Goodbye!.",
    "See you later!",
    "Bye-bye!",
    "I will wait for you",
    "Have a good day"
]

jokes = [
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus",
    "I'm friends with 25 letters of the alphabet. I don't know Y",
    "This graveyard looks crowded. People must be dying to get in",
    "What do you call a fish with no eyes? Fsh!",
    "I'm on a seafood diet.I see food and I eat it.!",
    "Why don't computers go to the beach? Because they are afraid of the Reshet!"
]

# --- שלב 2: פונקציות עזר לעיצוב ופלט (Helper Functions) ---

def print_separator():
    """מדפיס קו מפריד לעיצוב"""
    print("==========================================")

def print_bot(message):
    """מדפיס הודעה בשם הבוט עם אמוג'י"""
    print(f"🤖 {bot_name}: {message}")

def show_help():
    """מציג למשתמש מה הבוט יודע לעשות"""
    print_separator()
    print(f"I am {bot_name}, and here is what I can do:")
    print("- Say 'hello' or 'hi'")
    print("- Tell a 'joke'")
    print("- Say 'bye' to exit")
    print("- Type 'help' to see this menu again")
    print_separator()

# --- שלב 3: פונקציית ההיכרות והלוגיקה הראשית (Main Logic) ---

def greet_user():
    """מבצע היכרות ראשונית ומחזיר את שם המשתמש"""
    print_separator()
    print_bot("Welcome to the know evrything bot!")
    name = input("🤖 What's your name? ").strip()
    
    if name == "":
        name = "Friend"  # ברירת מחדל אם המשתמש לא הקיש שם
        
    print_bot(f"It's great to meet you, {name}!")
    return name

def main():
    # הפעלת שלב ההיכרות ושמירת השם
    user_name = greet_user()
    show_help()
    
    # לולאת השיחה
    while True:
        # קבלת קלט מהמשתמש (באותיות קטנות וללא רווחים מיותרים)
        user_choice = input(f"{user_name}: ").lower().strip()

        if "help" in user_choice:
            show_help()

        elif "hello" in user_choice or "hi" in user_choice:
            print_bot(f"{random.choice(greetings)} {user_name}!")
            
        elif "joke" in user_choice:
            print_bot(random.choice(jokes))
            
        elif "bye" in user_choice:
            print_bot(f"{random.choice(goodbyes)} {user_name}!")
            break  # יציאה מהתוכנית
            
        else:
            print_bot(f"I'm sorry {user_name}, I don't know that command yet. Type 'help' for options.")

# הרצת התוכנית
if __name__ == "__main__":
    main()
    import random

# --- פונקציה 1: שליפת בדיחה ---
def tell_joke():
    # שולף בדיחה אקראית מהרשימה שהגדרנו בתחילת הקוד
    return random.choice(jokes)


# --- פונקציה 2: משחק ניחוש מספרים ---
def play_guess_game():
    # הבוט בוחר מספר אקראי בין 1 ל-20
    secret_number = random.randint(1, 20)
    attempts = 0
    print_bot("I'm thinking of a number between 1 and 20. Can you guess it?")

    while True:
        try:
            # קבלת הניחוש מהמשתמש
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print_bot("Too low! Try again.")
            elif guess > secret_number:
                print_bot("Too high! Try again.")
            else:
                # המשתמש צדק - מחזירים הודעת ניצחון
                return f"Correct! It took you {attempts} attempts. Well played!"
        
        except ValueError:
            # טיפול במקרה שהמשתמש הקיש אותיות במקום מספר
            print_bot("Please enter a valid number.")


# --- פונקציה 3: ניתוח מצב רוח ---
def analyze_mood(message):
    message = message.lower()
    
    # רשימות של מילות מפתח
    happy_words = ["happy", "great", "awesome", "good", "wonderful", "excited"]
    sad_words = ["sad", "bad", "terrible", "upset", "lonely", "bored"]

    # בדיקה האם מילה מהרשימה מופיעה בהודעה
    for word in happy_words:
        if word in message:
            return "happy"
            
    for word in sad_words:
        if word in message:
            return "sad"
            
    # אם לא נמצאה התאמה
    return "neutral"
def get_response(message, user_name):
    # המרת ההודעה לאותיות קטנות כדי שהבוט יבין הכל
    message_lower = message.lower()
    
    # 1. בדיקת ברכות
    if any(word in message_lower for word in ["hello", "hi", "hey"]):
        greeting = random.choice(greetings)
        return f"{greeting}, {user_name}!"
    
    # 2. איך אתה מרגיש?
    elif "how are you" in message_lower:
        return "I'm doing great! Being a bot is awesome. How are you?"
    
    # 3. שאלות על שם הבוט
    elif "your name" in message_lower or "who are you" in message_lower:
        return f"My name is {bot_name}, your personal Python assistant!"
    
    # 4. בדיחות
    elif "joke" in message_lower or "funny" in message_lower:
        return tell_joke()
    
    # 5. בקשה למשחק (סימון מיוחד ל-main)
    elif "game" in message_lower or "play" in message_lower:
        return "game_menu"
    
    # 6. עזרה
    elif "help" in message_lower or "commands" in message_lower:
        show_help()
        return "What else can I help you with?"
    
    # 7. חישובים מתמטיים (בונוס חכם)
    elif any(op in message_lower for op in ["+", "-", "*", "/"]):
        try:
            # eval מריץ את התרגיל המתמטי מתוך המחרוזת
            result = eval(message_lower)
            return f"The answer is {result}."
        except:
            return "I tried to calculate that, but the numbers look a bit confusing!"

    # 8. דפוסי תגובה משלי (5 תגובות נוספות)
    elif "color" in message_lower:
        return "My favorite color is White, like Real Madrid the best club in the world!"
    elif "hobby" in message_lower or "hobbies" in message_lower:
        return "I love reading and play soccer. What about you?"
    elif "music" in message_lower:
        return "I like the  Beatelse! 🎵"
    elif "sport" in message_lower:
        return "I like football and basketball!"

    # 9. שימוש בניתוח מצב רוח
    mood = analyze_mood(message_lower)
    if mood == "happy":
        return f"I'm happy to hear that you're feeling good, {user_name}!"
    elif mood == "sad":
        return f"I'm sorry to hear that, {user_name}. you want me to tell you a joke?"

    # 10. תגובות ברירת מחדל (Default)
    default_responses = [
        "That's interesting!",
        "Tell me more!",
        "I see...",
        "Cool!"
    ]
    return random.choice(default_responses)
def chat():
    """פונקציית הצ'אט המרכזית שמחברת הכל"""
    
    # 1. היכרות עם המשתמש וקבלת שמו
    user_name = greet_user()
    
    # 2. הצגת רשימת היכולות של הבוט
    show_help()
    
    # משתנה לספירת הודעות (סטטיסטיקה אופציונלית)
    message_count = 0
    
    # 3. לולאת הצ'אט המרכזית
    while True:
        # קבלת הודעה מהמשתמש וניקוי רווחים
        user_message = input(f"\n{user_name}: ").strip()
        
        # דילוג אם ההודעה ריקה
        if not user_message:
            continue
            
        message_count += 1
        message_lower = user_message.lower()
        
        # 4. בדיקת פרידה (Exit logic)
        if any(word in message_lower for word in ["bye", "goodbye", "quit", "exit"]):
            farewell = random.choice(goodbyes)
            print_bot(f"{farewell} {user_name}!")
            break # יוצא מהלולאה ומסיים את התוכנית
            
        # 5. קבלת תגובה מה"מוח" של הבוט
        response = get_response(user_message, user_name)
        
        # 6. בדיקה האם המשתמש ביקש משחק
        if response == "game_menu":
            print_separator()
            print_bot("What would you like to play?")
            print("1. Number Guessing Game")
            print("2. Never mind")
            
            choice = input(f"{user_name}: ").strip()
            
            if choice == "1":
                game_result = play_guess_game()
                print_bot(game_result)
            else:
                print_bot("Okay, maybe next time!")
            print_separator()
            
        else:
            # אם זו לא בקשה למשחק, פשוט מדפיסים את התגובה הרגילה
            print_bot(response)
            
    # 7. סיכום וסטטיסטיקה בסיום
    print_separator()
    print(f"Chat Statistics: We exchanged {message_count} messages.")
    print("Thanks for chatting! See you soon!")
    print_separator()

# הפעלת האפליקציה
if __name__ == "__main__":
    chat()