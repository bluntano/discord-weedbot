__all__ = ['DROPBOX_TOKEN', 'DISCORD_TOKEN']
import os

if os.environ.get('OS', '') == 'Windows_NT':
    # Load variables from .env file
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

DROPBOX_TOKEN = os.environ.get('DROPBOX')
DISCORD_TOKEN = os.environ.get('DISCORD')

def new_env_file():
    if not os.path.exists('.env'):
        with open('.env', 'w') as env:
            env.write("DROPBOX=\nDISCORD=")
            env.close()
            return print("New .env file created")

new_env_file()