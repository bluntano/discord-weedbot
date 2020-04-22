from flask import Flask, redirect, render_template, url_for, request
import subprocess
import WeedBot
import json

server_debug = False # This only activates Flask web server

def page_handler(input: str):
    return render_template('header.html') + render_template(input) + render_template('footer.html')

def status_handler(input: str):
    return render_template('header.html') + f"<h1>{input}</h1>" + """
    <script>
        window.onload = setTimeout(function() {
            window.location.replace('/');
        }, 3000);
    </script>
    """ + render_template('footer.html')

def process_textline(textline, chosen_set):
    print(f"{textline}\n{chosen_set}")
    if not textline or not chosen_set:
        return status_handler("Why are we still here to suffer?")
    if len(textline) > 56:
        return status_handler("Yooo brooo, chill!")
    with open('sentences.json', 'r') as infile:
        data = json.load(infile)
        if textline in data[chosen_set]:
            return status_handler("It's already there, someone made the joke before you.")
        data[chosen_set].append(textline)
        with open('sentences.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    return status_handler("Yooooo! Poggers, fam!")

app = Flask(__name__, static_folder='web/public', template_folder='web/views')
@app.route('/')
def index():
    return page_handler('index.html')

@app.route('/bot')
def bot_invite():
    bot_id = 0
    if not server_debug:
        bot_id = WeedBot.bot_id()
    return redirect(f"https://discordapp.com/api/oauth2/authorize?client_id={bot_id}&permissions=43024&scope=bot")

@app.route('/submit')
def submit_page():
    return page_handler('submit.html')

@app.route('/git', methods=['POST'])
def git_update():
    proc = 'sh git.sh'
    subprocess.call(proc.split())
    return 200

@app.route('/handle_data', methods=['POST'])
def handle_data():
    textline = request.form['textline']
    chosen_set = request.form['sets']
    return process_textline(textline, chosen_set)

@app.route('/electronjs/api/textline', methods=['POST'])
def handle_data_json():
    data = request.get_json(force=True)
    textline = data['textline']
    chosen_set = data['sets']
    return process_textline(textline, chosen_set)

if __name__ == "__main__":
    if not server_debug:
        WeedBot.bot_alive()
    app.run('0.0.0.0')