import os
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext


# carico variabili
load_dotenv()
api_token = os.getenv('TOKEN')
chat_id = int(os.getenv('CHAT_ID'))


async def stop(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id == chat_id:
        await update.message.reply_text("Spegnimento server in corso ...")
        subprocess.run("sudo shutdown now", shell=True, check=True)
    else:
        pass

async def reboot(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id == chat_id:
        await update.message.reply_text("Reboot server in corso ...")
        subprocess.run("sudo reboot", shell=True, check=True)
    else:
        pass

async def temp(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id == chat_id:
        result = subprocess.run("vcgencmd measure_temp", capture_output=True, text=True, shell=True, check=True)
        await update.message.reply_text(result.stdout)
    else:
        pass

async def start(update: Update, context: CallbackContext) -> None:
    if update.effective_chat.id == chat_id:
        await update.message.reply_text("Hi!")
    else:
        pass

def main() -> None:
    # creo applicazione
    application = Application.builder().token(api_token).build()

    # Assegno gestione comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("reboot", reboot))
    application.add_handler(CommandHandler("temp", temp))

    # run application
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
