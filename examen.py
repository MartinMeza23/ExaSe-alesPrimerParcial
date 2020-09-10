import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate



frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

wave_852 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido_9 = wave_852 + wave_1477


frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

wave_852 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido_7 = wave_852 + wave_1209


frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

wave_941 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido_0 = wave_941 + wave_1336


frecuencia941 = SinSignal(freq=941, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

wave_941 = frecuencia852.make_wave(duration=0.5, start=0, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido_0 = wave_941 + wave_1336

wave_Sonido = wave_sonido_9 + wave_sonido_7 + wave_sonido_0 + wave_sonido_0

wave_Sonido.write("NoSalio.wav")
