# Línea de bajo - Necrofilia (Rock/Punk)
from midiutil import MIDIFile
from config import *

def línea_bajo_estrofa(acordes):
    """Genera línea de bajo para estrofas (8avos constantes)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            for tiempo in range(4):
                # 8avos: root en cada tiempo, octave up en los tiempos pares
                tiempos.append((root, 0.5))
                tiempos.append((root + 12, 0.5))  # Octava arriba
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def línea_bajo_coro(acordes):
    """Genera línea de bajo para coros (más movimiento)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            # Patrón con más movimiento para coro
            tiempos.append((root, 0.5))
            tiempos.append((root + 7, 0.5))     # 5ta
            tiempos.append((root + 12, 0.5))    # Octava
            tiempos.append((root + 7, 0.5))     # 5ta
            tiempos.append((root, 0.5))
            tiempos.append((root + 5, 0.5))     # 4ta
            tiempos.append((root + 12, 0.5))    # Octava
            tiempos.append((root + 5, 0.5))     # 4ta
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def línea_bajo_intro(num_compases=2):
    """Línea de bajo para intro (solo bajo y batería)"""
    patrón = []
    
    for _ in range(num_compases):
        tiempos = []
        for tiempo in range(4):
            # 8avos simples en Cm
            tiempos.append((C_MENOR_ROOT, 0.5))
            tiempos.append((C_MENOR_ROOT + 12, 0.5))
        patrón.append([tiempos])
    
    return patrón

def línea_bajo_puente(acordes):
    """Línea de bajo para puente (más melódica)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            tiempos = []
            # Patrón más melódico
            tiempos.append((root, 0.5))
            tiempos.append((root + 3, 0.5))     # 3ra menor
            tiempos.append((root + 7, 0.5))     # 5ta
            tiempos.append((root + 12, 0.5))    # Octava
            tiempos.append((root + 7, 0.5))     # 5ta
            tiempos.append((root + 3, 0.5))     # 3ra menor
            tiempos.append((root, 0.5))
            tiempos.append((root + 5, 0.5))     # 4ta
            compases.append(tiempos)
        patrón.append(compases)
    
    return patrón

def agregar_bajo(midi, track, patrón, tiempo_inicio, canal=CHANNEL_BAJO):
    """Agrega la línea de bajo al MIDI"""
    tiempo_actual = tiempo_inicio
    
    for acorde in patrón:
        for compas in acorde:
            for nota, duracion in compas:
                midi.addNote(track, canal, nota, tiempo_actual, duracion, VOL_BAJO)
                tiempo_actual += duracion
    
    return tiempo_actual
