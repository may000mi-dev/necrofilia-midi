# Guitarra melódica - Necrofilia (Rock/Punk estilo Muse)
from midiutil import MIDIFile
from config import *

# Escala de Cm: C D Eb F G Ab Bb
ESCALA_CM = [0, 2, 3, 5, 7, 8, 10]  # Distancias desde C
NOTAS_ESCALA_CM = [60, 62, 63, 65, 67, 68, 70]  # C4 a Bb4

def melodía_estrofa(acordes):
    """Melodía para estrofas (línea simple sobre los acordes)"""
    patrón = []
    
    # Melodía que sigue la progresión
    melodías = [
        # Compás 1 (Cm)
        [
            (60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),
            (60, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)
        ],
        # Compás 2 (G#)
        [
            (68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
            (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5)
        ],
        # Compás 3 (Cm)
        [
            (60, 0.5), (63, 0.5), (67, 0.5), (70, 0.5),
            (67, 0.5), (63, 0.5), (60, 0.5), (63, 0.5)
        ],
        # Compás 4 (Fm)
        [
            (65, 0.5), (68, 0.5), (72, 0.5), (68, 0.5),
            (65, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)
        ],
    ]
    
    for root, notas, duracion in acordes:
        compases = []
        for i in range(duracion):
            compases.append(melodías[i % 4])
        patrón.append(compases)
    
    return patrón

def melodía_coro(acordes):
    """Melodía para coros (más épica, usa Muse-like)"""
    patrón = []
    
    # Melodías más dramáticas para coro
    melodías_coro = [
        # Compás 1-2 (Cm)
        [
            (72, 0.5), (70, 0.5), (68, 0.5), (67, 0.5),
            (68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5),
            (63, 0.5), (67, 0.5), (72, 0.5), (70, 0.5),
            (68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5),
        ],
        # Compás 3-4 (G#)
        [
            (68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
            (68, 0.5), (70, 0.5), (72, 0.5), (70, 0.5),
            (68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
            (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5),
        ],
        # Compás 5-6 (D#)
        [
            (67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5),
            (70, 0.5), (68, 0.5), (67, 0.5), (68, 0.5),
            (70, 0.5), (72, 0.5), (75, 0.5), (72, 0.5),
            (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
        ],
        # Compás 7-8 (A#)
        [
            (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
            (67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5),
            (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
            (60, 0.5), (63, 0.5), (67, 0.5), (72, 0.5),
        ],
    ]
    
    for i, (root, notas, duracion) in enumerate(acordes):
        compases = []
        for _ in range(duracion):
            compases.append(melodías_coro[i % 4])
        patrón.append(compases)
    
    return patrón

def melodía_intro_reverb(num_compases=2):
    """Melodía con reverb para intro (compases 3-4)"""
    patrón = []
    
    # Melodía atmosférica estilo Muse
    melodías = [
        # Compás 1 (Cm)
        [
            (72, 0.5), (None, 0.5), (70, 0.5), (None, 0.5),
            (68, 0.5), (None, 0.5), (67, 0.5), (None, 0.5),
        ],
        # Compás 2 (G#)
        [
            (68, 0.5), (None, 0.5), (67, 0.5), (None, 0.5),
            (63, 0.5), (None, 0.5), (60, 0.5), (None, 0.5),
        ],
    ]
    
    for i in range(num_compases):
        patrón.append([melodías[i % 2]])
    
    return patrón

def melodía_puente(acordes):
    """Melodía para puente (más melódica, emotion)"""
    patrón = []
    
    melodías_puente = [
        # Compás 1 (Cm)
        [
            (60, 0.5), (63, 0.5), (67, 0.5), (72, 0.5),
            (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
        ],
        # Compás 2 (G#)
        [
            (68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5),
            (63, 0.5), (67, 0.5), (70, 0.5), (68, 0.5),
        ],
        # Compás 3 (Cm)
        [
            (72, 0.5), (70, 0.5), (68, 0.5), (67, 0.5),
            (63, 0.5), (60, 0.5), (63, 0.5), (67, 0.5),
        ],
        # Compás 4 (Fm)
        [
            (65, 0.5), (68, 0.5), (72, 0.5), (70, 0.5),
            (68, 0.5), (65, 0.5), (63, 0.5), (60, 0.5),
        ],
    ]
    
    for root, notas, duracion in acordes:
        compases = []
        for i in range(duracion):
            compases.append(melodías_puente[i % 4])
        patrón.append(compases)
    
    return patrón

def agregar_guitarra_melodica(midi, track, patrón, tiempo_inicio, canal=CHANNEL_GUITARRA_MELODICA):
    """Agrega guitarra melódica al MIDI"""
    tiempo_actual = tiempo_inicio
    
    for acorde in patrón:
        for compas in acorde:
            for nota, duracion in compas:
                if nota is not None:
                    midi.addNote(track, canal, nota, tiempo_actual, duracion, VOL_GUITARRA_MELODICA)
                tiempo_actual += duracion
    
    return tiempo_actual
