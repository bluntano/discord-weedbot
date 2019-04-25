# discord-weedbot

a bot that smokes some dank-ass weed, my nigguhs! also it will tell you how high you are. very nice eh? xd
#
![](/res/image.png)

I got inspiration from [this JavaScript code I found on Plexi Development's page](https://sourcecode.glitch.me/view?key=1460278146236522)

## Requirements

In order to make your own, you will need:
- `discord.py[voice]==0.16.12` to make it work, duh.  You can find it in [here!](https://libraries.io/pypi/discord.py)
- `dotenv` to take your Discord bot's token from `.env` file
- `dropbox` to take your weed pics from Dropbox cloud storage instead of storing pictures locally (v1 prototype of the bot is also available if you don't want to set up Dropbox)

I'll get into upgrading from discord.py 0.16.12 to the newest version as well ASAP.

In here there are also included server-side of things like:
- `server.js` which has express the minimalistic web framework installed, and also comes with `exec-sh` that executes the Shell startup script
- `start.sh` which installs the required Python packages and runs the Python code in the weedbot folder
- `package.json` which has listed necessary packages for the server code.

Keep in mind: you don't need these unless, you decide to run the bot on Node.js engine. I, for example, made the back-end in JavaScript because the host I'm using has Node.js engine and it doesn't support Python language.

### Have Fun!