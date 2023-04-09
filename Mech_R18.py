import telegram
from telegram.ext import CommandHandler, Updater,Filters,MessageHandler

# Define the Google Drive links for each semester
sem_links = {
    "/info": 0,
    "/syllabus": "https://drive.google.com/file/d/1XDhzJY3k9W75mObKufsNt213uDNNT_je/view?usp=drivesdk",
    "/sem1": "https://drive.google.com/drive/folders/1ZZC-1DNW1reBbg-fjqosu4sOeWRaAsIj",
    "/sem2": "https://drive.google.com/drive/folders/1zjqvCEB1nizE2H0oZ4PpYTYIkc9x56BO",
    "/sem3": "https://drive.google.com/drive/folders/1VN4tMoON4YeqOCkcTfZyVmDYLS9RVs8H",
    "/sem4": "https://drive.google.com/drive/folders/18VLkxcUt_ksu66L5GLDfFV0xxBxfq9cC",
    "/sem5": "https://drive.google.com/drive/folders/1FnAunBCJRKcakd_hlsAicIScpd1rsg4l",
    "/sem6": "https://drive.google.com/drive/folders/1jlSHDixLfW_WosF_LgwOIJm8JGzdBfjV",
    "/sem7": "https://drive.google.com/drive/folders/12HPJ_4vsdbEB7y1rNClyJHrzI-Gld9VG",
    "/sem8": "https://drive.google.com/drive/folders/1A4iludfiuMfD-JnL_bjFa9DCzetN2vJb",
    "/help":0,
    "/chat":0
}

# Define the function to handle the /start command
def start(update, context):
    # Ask the user if they have access
    s="Welcome ! I am Mech_R18"
    update.message.reply_text(s)
    update.message.reply_text("Here are the available commands:\n" + "\n".join(sem_links.keys()))

def help(update, context):
    update.message.reply_text("Here are the available commands:\n" + "\n".join(sem_links.keys()))

def syllabus(update, context):
    update.message.reply_text(f"Here is the Link to view Syllabus : \nhttps://drive.google.com/file/d/1XDhzJY3k9W75mObKufsNt213uDNNT_je/view?usp=drivesdk")

def info(update, context):
    update.message.reply_text('I am a Bot, Created by "Manik Raj" \nI am able to provide you with study materials for all 8 semesters of JNTUH college\'s mechanical engineering program.')
    update.message.reply_text("Here are the available commands:\n" + "\n".join(sem_links.keys()))

def chat(update, context):
    update.message.reply_text("Here are some questions I can answer")
    update.message.reply_text("what is your name?\nwho created you? \nwhat can you do? \nwhat programming language are you written in?")


    
# Define the function to handle the user's response to the /start command
def Read(update, context):
    # Get the user's response
    response = update.message.text.lower()
    response.strip()

    if response=='what is your name?':
        update.message.reply_text("Iam MechR18")
    
    elif response=='who created you?':
        update.message.reply_text('I was Created by "Manik Raj"')

    elif response=='what can you do?':
        update.message.reply_text("I am able to provide you with study materials for all 8 semesters of JNTUH college's mechanical engineering program.")    

    elif response=='what programming language are you written in?':
        update.message.reply_text('I was written in Python')

    elif response=='hello':
        update.message.reply_text('Hey there!')

    elif response=='hi':
        update.message.reply_text('Hey there!')

    else:
        update.message.reply_text("I'm sorry, I didn't understand.")
        update.message.reply_text("Here are the available commands:\n" + "\n".join(sem_links.keys()))

# Define the function to handle the semester commands
def sem(update, context):
    # Get the semester command
    sem_command = update.message.text.lower()

    # If the semester command is recognized, send the corresponding Google Drive link
    if sem_command in sem_links:
        update.message.reply_text(sem_links[sem_command])
    # If the semester command is not recognized, send an error message

    else:
        update.message.reply_text("I'm sorry, that command is not recognized.")

# Set up the bot
updater = Updater("5974301894:AAExUmLTOfz34v5YGuWh3rW_aAqyDzdIbOY", use_context=True)
dispatcher = updater.dispatcher

# Add the command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("info", info))
dispatcher.add_handler(CommandHandler("syllabus", syllabus))
dispatcher.add_handler(CommandHandler("sem1", sem))
dispatcher.add_handler(CommandHandler("sem2", sem))
dispatcher.add_handler(CommandHandler("sem3", sem))
dispatcher.add_handler(CommandHandler("sem4", sem))
dispatcher.add_handler(CommandHandler("sem5", sem))
dispatcher.add_handler(CommandHandler("sem6", sem))
dispatcher.add_handler(CommandHandler("sem7", sem))
dispatcher.add_handler(CommandHandler("sem8", sem))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("chat", chat))
# Add the message handler for the user's input
dispatcher.add_handler(MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command,Read))

# Start the bot
print("Bot is Running.....")
updater.start_polling()
updater.idle()
