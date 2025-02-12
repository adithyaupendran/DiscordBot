from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Set up bot intents
intents: Intents = Intents.default()
intents.message_content = True  # Required for reading message content
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("No message received")
        return  

    is_private = user_message.startswith('?')
    if is_private:
        user_message = user_message[1:]  # Remove '?' from message

    try:
        response: str = get_response(user_message)
        if response:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
    except Exception as e:
        print(f"Error sending message: {e}")

@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

@client.event
async def on_message(message: Message) -> None:
    if message.author.bot:  
        return  # Ignore messages from all bots, including itself

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}: {user_message}")
    await send_message(message, user_message)

def main() -> None:
    client.run(TOKEN)  # No need to specify 'token='

if __name__ == '__main__':
    main()
