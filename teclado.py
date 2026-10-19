# Teclado/Sintetizador - Necrofilia (Rock/Punk estilo Muse)
from config import *

def pad_estrofa(acordes):
    """Pad sutil para estrofas (notas sostenidas)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            # Pad con notas del acorde sostenidas
            compases.append({
                "tipo": "pad",
                "notas": [notas[0] + 12, notas[2] + 12],  # Octava arriba
                "duracion": 3.5
            })
        patrón.append(compases)
    
    return patrón

def pad_coro(acordes):
    """Pad más intenso para coros"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            compases.append({
                "tipo": "pad_coro",
                "notas": [n + 12 for n in notas] + [n + 24 for n in notas],
                "duracion": 0.5
            })
        patrón.append(compases)
    
    return patrón

def arpegio_puente(acordes):
    """Arpegio para puente (estilo Muse)"""
    patrón = []
    
    for root, notas, duracion in acordes:
        compases = []
        for _ in range(duracion):
            # Arpegio ascendente y descendente
            notas_arpegio = []
            for nota in notas:
                notas_arpegio.append((nota + 12, 0.25))
                notas_arpegio.append((nota + 24, 0.25))
            for nota in reversed(notas):
                notas_arpegio.append((nota + 24, 0.25))
                notas_arpegio.append((nota + 12, 0.25))
            compases.append({
                "tipo": "arpegio",
                "notas": notas_arpegio
            })
        patrón.append(compases)
    
    return patrón

def lead_coro(acordes):
    """Lead synth para coros (melodía épica)"""
    patrón = []
    
    # Melodías lead para coro
    melodías = [
        # Cm
        [(72, 0.5), (70, 0.5), (68, 0.5), (67, 0.5),
         (68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5)],
        # G#
        [(68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
         (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5)],
        # D#
        [(67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5),
         (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5)],
        # A#
        [(70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
         (67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5)],
    ]
    
    for i, (root, notas, duracion) in enumerate(acordes):
        compases = []
        for _ in range(duracion):
            compases.append({
                "tipo": "lead",
                "notas": melodías[i % 4]
            })
        patrón.append(compases)
    
    return patrón

def agregar_teclado(midi, track, patrón, tiempo_inicio, canal=4):
    """Agrega teclado/sintetizador al MIDI"""
    tiempo_actual = tiempo_inicio
    
    for acorde in patrón:
        for compas in acorde:
            if compas["tipo"] == "pad":
                # Pad sostenido
                for nota in compas["notas"]:
                    midi.addNote(track, canal, nota, tiempo_actual, compas["duracion"], 80)
                tiempo_actual += 4  # Un compás completo
            elif compas["tipo"] == "pad_coro":
                # Pad coro con notas más cortas
                for nota in compas["notas"]:
                    midi.addNote(track, canal, nota, tiempo_actual, compas["duracion"], 80)
                tiempo_actual += 0.5
            elif compas["tipo"] == "arpegio":
                # Arpegio
                for nota, duracion in compas["notas"]:
                    midi.addNote(track, canal, nota, tiempo_actual, duracion, 80)
                    tiempo_actual += duracion
            elif compas["tipo"] == "lead":
                # Lead synth
                for nota, duracion in compas["notas"]:
                    midi.addNote(track, canal, nota, tiempo_actual, duracion, 80)
                    tiempo_actual += duracion
    
    return tiempo_actual
