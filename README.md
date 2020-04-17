# discord-weedbot

a bot that smokes some dank-ass weed, my nigguhs! also it will tell you how high you are. very nice eh? xd
it even uploads weed pics to dropbox from #weedpics text channel, holy moly
#
![](image.PNG)

I got inspiration from [this JavaScript code I found on Plexi Development's page](https://sourcecode.glitch.me/view?key=1460278146236522)

## Requirements

In order to make your own, you will need:
- `discord.py` to make it work, duh.  You can find it in [here!](https://libraries.io/pypi/discord.py)
- `dropbox` to take your weed pics from Dropbox cloud storage instead of storing pictures locally
- `pymediainfo` to process through .mp4 and .mov files
- `python-dotenv` to read your Dropbox and Discord app tokens (**on Glitch, you don't need that**)
- `Flask` to launch up web server with textline submission system on the webpage
  - Must have created `.env` file inside the `weedbot/` folder with `DISCORD` and `DROPBOX` tokens
  ```
  DROPBOX=<your secret app token>
  DISCORD=<your secret app token>
  ```

`start.sh` is included with the repo, for [Glitch.com](https://glitch.com)

### Have Fun!
