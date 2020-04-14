from flask import Flask, redirect
import WeedBot

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

@app.route('/bot')
def bot_invite():
    return redirect(f"https://discordapp.com/api/oauth2/authorize?client_id={WeedBot.bot_id()}&permissions=2064&scope=bot")

if __name__ == "__main__":
    WeedBot.bot_alive()
    app.run()