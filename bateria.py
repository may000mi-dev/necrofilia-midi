# Patrones de batería - Necrofilia (Rock/Punk estilo Green Day)
from midiutil import MIDIFile
from config import *

# Notas de batería General MIDI
KICK = 36      # C1 - Bombo
SNARE = 38     # D1 - Caja
HI_HAT_CLOSE = 42  # F#1 - Hi-hat cerrado
HI_HAT_OPEN = 46   # A#1 - Hi-hat abierto
CRASH = 49     # C#2 - Plato crash
RIDE = 51      # D#2 - Plato ride

# Patrones de batería (cada fila = 1 tiempo, subdivisión en 8avos)
# K=Bombo, S=Caja, H=Hi-hat, X=Silencio

def patrón_estrofa():
    """Patrón punk básico para estrofas"""
    # 8 compases, 4 tiempos cada uno, 8 subdivisiones por tiempo
    patrón = []
    
    for compas in range(8):
        tiempos = []
        for tiempo in range(4):
            subdivisiones = []
            if tiempo == 0:  # Tiempo 1
                subdivisiones = [KICK, HI_HAT_CLOSE, None, HI_HAT_CLOSE, 
                               None, HI_HAT_CLOSE, None, HI_HAT_CLOSE]
            elif tiempo == 1:  # Tiempo 2
                subdivisiones = [None, HI_HAT_CLOSE, SNARE, HI_HAT_CLOSE,
                               None, HI_HAT_CLOSE, None, HI_HAT_CLOSE]
            elif tiempo == 2:  # Tiempo 3
                subdivisiones = [KICK, HI_HAT_CLOSE, None, HI_HAT_CLOSE,
                               KICK, HI_HAT_CLOSE, None, HI_HAT_CLOSE]
            elif tiempo == 3:  # Tiempo 4
                subdivisiones = [None, HI_HAT_CLOSE, SNARE, HI_HAT_CLOSE,
                               None, HI_HAT_CLOSE, None, HI_HAT_CLOSE]
            tiempos.append(subdivisiones)
        patrón.append(tiempos)
    
    return patrón

def patrón_coro():
    """Patrón más intenso para coros"""
    patrón = []
    
    for compas in range(8):
        tiempos = []
        for tiempo in range(4):
            subdivisiones = []
            if tiempo == 0:  # Tiempo 1
                subdivisiones = [KICK, None, None, HI_HAT_OPEN,
                               None, None, CRASH, None]
            elif tiempo == 1:  # Tiempo 2
                subdivisiones = [None, None, SNARE, None,
                               None, None, None, HI_HAT_OPEN]
            elif tiempo == 2:  # Tiempo 3
                subdivisiones = [KICK, None, KICK, None,
                               None, None, None, HI_HAT_OPEN]
            elif tiempo == 3:  # Tiempo 4
                subdivisiones = [None, None, SNARE, None,
                               None, None, CRASH, None]
            tiempos.append(subdivisiones)
        patrón.append(tiempos)
    
    return patrón

def patrón_intro_bateria():
    """Patrón simplificado para intro (solo batería y bajo)"""
    patrón = []
    
    for compas in range(2):  # Solo 2 compases
        tiempos = []
        for tiempo in range(4):
            subdivisiones = []
            if tiempo == 0:
                subdivisiones = [KICK, None, None, None,
                               None, None, None, None]
            elif tiempo == 1:
                subdivisiones = [None, None, SNARE, None,
                               None, None, None, None]
            elif tiempo == 2:
                subdivisiones = [KICK, None, None, None,
                               KICK, None, None, None]
            elif tiempo == 3:
                subdivisiones = [None, None, SNARE, None,
                               None, None, None, None]
            tiempos.append(subdivisiones)
        patrón.append(tiempos)
    
    return patrón

def patrón_outro():
    """Patrón de cierre"""
    patrón = []
    
    for compas in range(4):
        tiempos = []
        for tiempo in range(4):
            subdivisiones = []
            if compas < 2:  # Primeros 2 compases normales
                if tiempo == 0:
                    subdivisiones = [KICK, None, None, None,
                                   None, None, None, None]
                elif tiempo == 1:
                    subdivisiones = [None, None, SNARE, None,
                                   None, None, None, None]
                elif tiempo == 2:
                    subdivisiones = [KICK, None, None, None,
                                   KICK, None, None, None]
                elif tiempo == 3:
                    subdivisiones = [None, None, SNARE, None,
                                   None, None, None, None]
            else:  # Últimos 2 compases con fill
                if tiempo == 0:
                    subdivisiones = [KICK, None, None, None,
                                   None, None, None, None]
                elif tiempo == 1:
                    subdivisiones = [None, None, SNARE, None,
                                   None, None, None, None]
                elif tiempo == 2:
                    subdivisiones = [KICK, None, SNARE, None,
                                   KICK, None, SNARE, None]
                elif tiempo == 3:
                    subdivisiones = [None, None, SNARE, None,
                                   CRASH, None, None, None]
            tiempos.append(subdivisiones)
        patrón.append(tiempos)
    
    return patrón

def agregar_bateria(midi, track, patrón, tiempo_inicio, canal=CHANNEL_BATERIA):
    """Agrega el patrón de batería al MIDI"""
    tiempo_actual = tiempo_inicio
    
    for compas in patrón:
        for tiempo_idx, tiempo in enumerate(compas):
            for subdiv_idx, nota in enumerate(tiempo):
                if nota is not None:
                    # Calcular tiempo en beats
                    # Cada tiempo = 1 beat, cada beat = 2 subdivisiones (8avos)
                    beat = tiempo_actual + tiempo_idx + (subdiv_idx * 0.5)
                    midi.addNote(track, canal, nota, beat, 0.5, VOL_BATERIA)
        tiempo_actual += 4  # Siguiente compás
    
    return tiempo_actual
