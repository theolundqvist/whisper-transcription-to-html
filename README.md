# whisper-transcription-to-html
A python script that reformats whisper transcriptions (text with timestamp) to a readable format in html with convenient play buttons on each row to listen to the recording at that time.

From:
```
[00:00:09.000 --> 00:00:11.000]  Väldigt simpelt namn.
[00:00:11.000 --> 00:00:13.000]  Ja, just det. Vanligt.
[00:00:35.000 --> 00:00:40.000]  Okej, och vad är dina planer när du är klar?
```

To:

![image](https://user-images.githubusercontent.com/31588188/236912191-017c3c88-67ff-4dfd-b8ab-c31db553b81e.png)



## Requirements
 - Python3
 - (please notify me if anything else is needed so that I can add it to this README)

## How to use
1. Place your `X.txt` files in the folder called `in/`
2. Place your audio files with corresponding names: `X.m4a` in the folder `out/audio/`
3. Run `python format.py`
4. `out/X.html` is created, `out/` is then zipped to `out.zip`.
