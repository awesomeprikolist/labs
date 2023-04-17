from pydub import AudioSegment
from pydub.effects import speedup

filename = "muz.wav"

sound = AudioSegment.from_wav(filename)

x = input('Ускорить / Замедлить? ')
if x == 'Ускорить':
    playback_speed = 1.5
elif x == "Замедлить":
    playback_speed = 0.9

new_sound = speedup(sound, playback_speed, chunk_size=150, crossfade=30)

new_filename = "changed_" + filename
new_sound.export(new_filename, format="wav")