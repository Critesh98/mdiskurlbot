import json
import requests
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client('zee5 bot',
             api_id=19886681,
             api_hash='600e799cf14a251134cd0c6ea8e08f27',
             bot_token="5154193675:AAE2sU4FJe_RLIHopHxFD2799pgR9XTi80U",
             workers=50,
             sleep_threshold=10)

# ... (previous code)

@bot.on_message(filters.command('dashboard') & filters.private)
async def show_dashboard(bot, message):
    chat = message.chat
    url = f"https://mdiskurl.yss.workers.dev/{chat.id}"
    res = requests.get(url).json()

    if res['status']:
        api_token = res['data']['token']
        user_dashboard_url = 'https://mdiskurl.com/api/user/dashboard'
        headers = {'Authorization': f'Bearer {api_token}'}

        # Make a GET request to retrieve user details
        response = requests.get(user_dashboard_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            dashboard_text = f"User Dashboard Data:\n{json.dumps(user_data, indent=2)}"
            await message.reply(dashboard_text)
        else:
            error_text = f"Error: {response.status_code}, {response.text}"
            await message.reply(error_text)
    else:
        await message.reply("You need to log in first using /login")

# ... (remaining code)

if __name__ == "__main__":
    bot.run()
