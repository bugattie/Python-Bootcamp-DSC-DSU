import time


def main():
    lyrics = "And I'll rise up.I'll rise like the day.I'll rise up.I'll rise unafraid.I'll rise up.And I'll do it a thousand times again.And I'll rise up.High like the waves.I'll rise up.In spite of the ache.I'll rise up.And I'll do it a thousand times again"

    # lyrics = lyrics.split('.')
    printWithDelay(lyrics)


def printWithDelay(lyrics):
    lyrics = lyrics.split('.')

    for i in lyrics:
        time.sleep(1)
        print(i)


if __name__ == "__main__":
    main()
