#  Word Censor

A simple Python project made with one basic idea:

*What if we could automatically stop unwanted words and spam from appearing during a livestream?**

The user can decide which words they don't want. The program checks the input/text for those words and gives the option to replace them.

The long-term aim of this project is to make something that can be connected to **livestreams, chats, or other platforms* so that unwanted or abusive words can be detected before they become a problem.

## What it does right now

At the moment, the program:

- Takes a list of words from the user that they want to censor.
- Reads the text from `censor.txt`.
- Checks whether any of the selected words are present.
- If a word is found, the user can replace it with another word.
- The modified text is then written back to the file.

## Why I made this

Livestream chats can get messy very quickly.

Sometimes people spam the same message again and again, use abusive words, or post things that the streamer simply doesn't want on their stream.

I wanted to start with a basic version where **the user decides what should be censored** instead of having a fixed list of words.

This is just the starting version. The bigger idea is to make it usable directly with livestreams and chats.

## Current limitations

This is still an early version.

Right now it works with a text file instead of directly connecting to a livestream platform.

It also does not automatically detect every type of spam or understand the context of a message. It mainly checks whether the selected words exist in the text.

## Future plans

Some things I want to add later:

- Real-time livestream chat monitoring
- Automatic word replacement
- Spam detection
- Repeated message detection
- User-defined rules
- Integration with platforms like YouTube/Twitch
- A simple interface so that users don't have to edit the code
- Better filtering for different forms of the same word

