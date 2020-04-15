from flask import Flask, redirect
import subprocess
import WeedBot

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

@app.route('/bot')
def bot_invite():
    return redirect(f"https://discordapp.com/api/oauth2/authorize?client_id={WeedBot.bot_id()}&permissions=43024&scope=bot")

@app.route('/git', methods=['POST'])
def git_update():
    proc = 'sh git.sh'
    subprocess.call(proc.split())
    return "git"

if __name__ == "__main__":
    WeedBot.bot_alive()
    app.run()