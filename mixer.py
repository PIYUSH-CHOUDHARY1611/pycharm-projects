from pygame import mixer

mixer.init()

mixer.music.load("onetime.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

while True:
    print("Press'p'to pause 'r'to resume")
    print("Prpess 'e'to exit")
    querry = input(">>> ")

    if querry == 'p':
        mixer.music.pause()
    elif querry == 'r':
        mixer.music.unpause()
    elif querry == 'e':
        mixer.music.stop()
        break