# discord-weedbot

a bot that smokes some dank-ass weed, my nigguhs! also it will tell you how high you are. very nice eh? xd
it even uploads weed pics to dropbox from #weedpic-request text channel, holy moly
#
![](image.png)

I got inspiration from [this JavaScript code I found on Plexi Development's page](https://sourcecode.glitch.me/view?key=1460278146236522)

## Requirements

In order to make your own, you will need:
- `discord.py[voice]==0.16.12` to make it work, duh.  You can find it in [here!](https://libraries.io/pypi/discord.py)
- `dropbox` to take your weed pics from Dropbox cloud storage instead of storing pictures locally
- `pymediainfo` to process through .mp4 and .mov files
- `python-dotenv` to read your Dropbox and Discord app tokens
  - Must have created `.env` file inside the `weedbot/` folder with `DISCORD` and `DROPBOX` tokens
  ```
  DROPBOX=<your secret app token>
  DISCORD=<your secret app token>
  ```

Just do `python/python3 -m pip install --user -r weedbot/req.txt` and you should be good to go. Or, in case of Linux, you could use `start.sh` instead.

The place where I host my bot, they haven't updated Python from 3.5.2 to 3.7.2 or newer yet. Have to be a bit patient!

In here there are also included server-side of things like:
- `server.js` which has express the minimalistic web framework installed, and also comes with `exec-sh` that executes the Shell startup script. Also has auto-updater (set up with GitHub's webhook)
- `start.sh` which installs the required Python packages and runs the Python code in the weedbot folder
- `git.sh` which is repository updater - updates inside the project where it has been cloned to
- `package.json` which has listed necessary packages for the server code.

Keep in mind: you don't need these unless, you decide to run the bot on Node.js engine. I, for example, made the back-end in JavaScript because the host I'm using has Node.js engine and it doesn't support Python language.

### Have Fun!
