# ServerCare
If you lazy like me, I made that script that via Telegram you could turn off, reboot, see if it's alive or see the temperature 
of your raspberry pi

## Small guide
In the folder create a .env file with `TOKEN=<telegramBotApiKey>` and `CHAT_ID=<yourChatId>` so the program will replay only to you.
The .service file has a tamplate for the service in ubuntu, so the program cloud turn on every time you turn on the pi.
Remember to install the requiremets with the root user otherwise it won't work (for the service).

## What I used
Raspberry pi 4 with Ubuntu server
