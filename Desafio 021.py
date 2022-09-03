from pygame import mixer, event
mixer.init() 
mixer.music.load("2WEI.mp3")
mixer.music.set_volume(0.7) 
mixer.music.play()
input()
while True:

    print("Pressione 'p' para pausar, 'r' para retornar")
    print("Pressione 'e' para sair do programa")
    query = input("  ")

    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

