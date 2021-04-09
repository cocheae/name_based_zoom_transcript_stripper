import webvtt
import sys


def error():
    print("File not found, please make sure that you've renamed the file to 'transcript.vtt'")
    print("if the fiel is correctly named, make sure that the .vtt file is in the same folder as the 'script.py' is")
    print("if the error still persists, please reachout to cocheae@umich.edu")


def main(name):


    name_in_file = False
    name = name.lower()
    cc = webvtt.read('transcript.vtt')
    cleaned = open("cleaned_transcript.txt", 'w')

    for caption in cc:
        split = caption.text.split(':')
        if len(split) > 1 and name in str(split[0]).lower():
            name_in_file = True
            line = str(split[1])
            cleaned.write(line + '\n\n')
    #
    if not name_in_file:
        print("Make sure that you typed your name EXACTLY as it appears in the transcript")




if __name__ == "__main__":
    try:
        main(input("Please enter name in all-lowered case, EXACTLY as in the transcript, WITHOUT the ':' -> "))
    except FileNotFoundError:
        error()
