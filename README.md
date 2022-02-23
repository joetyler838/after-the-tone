# After the Tone
Project for After the Tone Wedding Phone


## Final Desired Result
Weddings guests are able to pick up telephone at the welcome table, hear a specific welcome message, then leave an message for couple that is saved to local disk folder.

## Current State
Basic python program created that will play prompt in the form of drums.wav file before allow user to speak into attached designated microphone (needed a way to select microphone since development desktop had multiple)

## TODO:
-  Organize guest audio output into folders (stretch, use AI to detect names from people to organize them into named folders/name the output files)
-  Have program auto select correct microphone
-  Have python script auto run at raspberry pi startup
-  Utilize AWS lambda in order to backup sound files to the cloud (utlize wifi chip onboard)

## Current Hardware
-  Raspberry Pi Zero W on Raspbian OS Lite
-  MicroSD card large enough for operating system + wav files created from guests
-  Amazon Maono USB microphone (implanted into phone)
-  Amazon USB/wireless speaker (implanted into phone)
