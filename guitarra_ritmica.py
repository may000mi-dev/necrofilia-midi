# Guitarra rítmica (Power Chords) - Necrofilia (Rock/Punk)
from midiutil import MIDIFile
from config import *

def power_chords_estrofa(acordes):
    """Power chords con palm mute para estrofas (8avos)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            for _ in range(4):  # 4 tiempos por compás
                # 8avos con palm mute (simulado con duración corta)
                for nota in notas:
                    tiempos.append((nota, 0.4))  # Duración corta para palm mute
                    tiempos.append((None, 0.1))  # Pequeño silencio
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def power_chords_coro(acordes):
    """Power chords abiertos para coros (más sustain)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            for _ in range(4):  # 4 tiempos por compás
                # 8avos abiertos (más sustain)
                for nota in notas:
                    tiempos.append((nota, 0.45))
                    tiempos.append((None, 0.05))
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def power_chords_intro(num_compases=2):
    """Power chords para intro (compases 3-4)"""
    patrón = []
    
    # Intro usa Cm y G#
    acordes_intro = [
        (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 1),
        (G_SOSTENIDO_ROOT, POWER_CHORD_G_SOSTENIDO, 1),
    ]
    
    for root, notas, duracion in acordes_intro:
        compases = []
        for _ in range(duracion):
            tiempos = []
            # Patrón más lento para intro
            for _ in range(4):
                for nota in notas:
                    tiempos.append((nota, 0.8))
                    tiempos.append((None, 0.2))
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def power_chords_puente(acordes):
    """Power chords para puente (más dinámico)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            # Patrón con variaciones
            for tiempo in range(4):
                if tiempo % 2 == 0:  # Tiempos 1 y 3: 8avos
                    for nota in notas:
                        tiempos.append((nota, 0.4))
                        tiempos.append((None, 0.1))
                else:  # Tiempos 2 y 4: sostenido
                    for nota in notas:
                        tiempos.append((nota, 0.9))
                        tiempos.append((None, 0.1))
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def agregar_guitarra_ritmica(midi, track, patrón, tiempo_inicio, canal=CHANNEL_GUITARRA_RITMICA):
    """Agrega guitarra rítmica al MIDI"""
    tiempo_actual = tiempo_inicio
    
    for acorde in patrón:
        for compas in acorde:
            for nota, duracion in compas:
                if nota is not None:
                    midi.addNote(track, canal, nota, tiempo_actual, duracion, VOL_GUITARRA_RITMICA)
                tiempo_actual += duracion
    
    return tiempo_actual
