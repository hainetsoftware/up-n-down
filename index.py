import classic
import dif_normal
import dif_hard
import dif_dario_moccia
import domenico
print("Benvenutx in Up'n Down, il nuovo gioco marchiato hai.network")
print("")
print("Ecco le varie modalità a cui potrai scegliere di giocare:")
print("")
print("1. Modalita' classica (Uccellino di default e 30FPS)")
print("2. Modalita' normale (Uccellino di default e 50FPS)")
print("3. Modalita' difficile (Uccellino di default e 75FPS)")
print("4. Modalita' Caverna di Platone (Il faccione del noto AniTuber napoletano e 30FPS)")
print("5. Modalita' Dario Moccia (Il faccione del noto YouTuber livornese e 30FPS)")

mod  = int(input("Inserisci 1/2/3/4/5 a seconda della modalità a cui vuoi giocare... "))

if mod == 1: exec(open('classic/classic.py').read())
if mod == 2: exec(open('dif_normal/normal.py').read())
if mod == 3: exec(open('dif_hard/hard.py').read())
if mod == 4: exec(open('domenico/caverna_di_platone.py').read())
if mod == 5: exec(open('dif_dario_moccia/dario.py').read())
