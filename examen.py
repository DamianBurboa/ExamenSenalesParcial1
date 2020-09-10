import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

##6

frecuencia440 = SinSignal(freq=770, amp=1, offset=0)
frecuencia622 = SinSignal(freq=1477, amp=1, offset=0)

wave_440 = frecuencia440.make_wave(duration=0.5, start=0, framerate=44100)
wave_622 = frecuencia622.make_wave(duration=0.5, start=0, framerate=44100)

wave_sonido6 = wave_440 + wave_622

##7

frecuencia441 = SinSignal(freq=852, amp=1, offset=0)
frecuencia623 = SinSignal(freq=1209, amp=1, offset=0)

wave_441 = frecuencia441.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_623 = frecuencia623.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_sonido7 = wave_441 + wave_623

##2

frecuencia442 = SinSignal(freq=697, amp=1, offset=0)
frecuencia624 = SinSignal(freq=1336, amp=1, offset=0)

wave_442 = frecuencia442.make_wave(duration=0.5, start=1.0, framerate=44100)
wave_624 = frecuencia624.make_wave(duration=0.5, start=1.0, framerate=44100)

wave_sonido2 = wave_442 + wave_624

##5

frecuencia443 = SinSignal(freq=770, amp=1, offset=0)
frecuencia625 = SinSignal(freq=1336, amp=1, offset=0)

wave_443 = frecuencia443.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_625 = frecuencia625.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido5 = wave_443 + wave_625

sonidofinal = wave_sonido6 + wave_sonido7 + wave_sonido2 + wave_sonido5

sonidofinal.write("Sonidofinal.wav")
