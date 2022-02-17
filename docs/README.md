> Current Status : Incomplete
# Status Embed

Status Embed is an awesome open source api and a bot that lets you embed your status into github's README.md file or almost anywhere with image support.

### Features
- Realtime Update
- Easily Self-Hosted
- Customisable
- Never tracks data

### How to get it

1. https://discord.gg/qEYbuWu5NE (Join this server or it will not work)
2. Go to ``statusembed.theindiandev.xyz/api/<your-user-id>`` for json API and for the image ``statusembed.theindiandev.xyz/api/<your-user-id.png>``.

### How to self host
1. Install Python Version >= 3.7 on your server.
2. Create a new bot and turn on all the intents.
3. Add the bot to your server (Check tutorials on YouTube if you can't do it yourself).
4. Run this command:
```bash
git clone https://github.com/the-indian-dev/status-embed
cd status-embed
python3 -m pip install -r requirements.txt
EXPORT DISCORD_TOKEN=<your token here>
EXPORT GUILD_ID=<server id here>
python main.py
```

### Lisence
Lisenced under MIT. Have fun! Please star the project if you liked it.
