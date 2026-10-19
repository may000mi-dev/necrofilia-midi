# Generador MIDI principal - Necrofilia (versión simplificada)
# Script que genera el archivo MIDI completo
from midiutil import MIDIFile
from config import *
from acordes import obtener_acordes_seccion

def crear_midi():
    """Crea el archivo MIDI completo de Necrofilia"""
    
    # Crear objeto MIDI con 5 tracks
    midi = MIDIFile(5)
    
    # Configurar tracks
    tracks = {
        "batería": 0,
        "bajo": 1,
        "guitarra_ritmica": 2,
        "guitarra_melodica": 3,
        "teclado": 4,
    }
    
    # Configurar nombres de tracks
    track_names = [
        "Batería",
        "Bajo",
        "Guitarra Rítmica",
        "Guitarra Melódica",
        "Teclado/Sintetizador"
    ]
    
    for i, name in enumerate(track_names):
        midi.addTrackName(i, 0, name)
    
    # Configurar tempo
    midi.addTempo(0, 0, TEMPO)
    
    # Tiempo actual para cada track
    tiempos = {track: 0 for track in tracks.values()}
    
    print("Generando Necrofilia...")
    print(f"Tempo: {TEMPO} BPM | Compás: {COMPAS}/4")
    print(f"Duración por compás: {SEGUNDOS_POR_COMPAS:.2f} segundos")
    print()
    
    # Notas de batería General MIDI
    KICK = 36
    SNARE = 38
    HI_HAT_CLOSE = 42
    HI_HAT_OPEN = 46
    CRASH = 49
    
    # Función para agregar un compás de batería
    def agregar_compas_bateria(track, tiempo_inicio, patrón="normal"):
        tiempo = tiempo_inicio
        for beat in range(4):
            if patrón == "normal":
                if beat == 0:
                    midi.addNote(track, 9, KICK, tiempo, 0.5, 100)
                    midi.addNote(track, 9, HI_HAT_CLOSE, tiempo, 0.5, 80)
                elif beat == 1:
                    midi.addNote(track, 9, SNARE, tiempo, 0.5, 100)
                    midi.addNote(track, 9, HI_HAT_CLOSE, tiempo, 0.5, 80)
                elif beat == 2:
                    midi.addNote(track, 9, KICK, tiempo, 0.5, 100)
                    midi.addNote(track, 9, KICK, tiempo + 0.5, 0.5, 100)
                    midi.addNote(track, 9, HI_HAT_CLOSE, tiempo, 0.5, 80)
                    midi.addNote(track, 9, HI_HAT_CLOSE, tiempo + 0.5, 0.5, 80)
                elif beat == 3:
                    midi.addNote(track, 9, SNARE, tiempo, 0.5, 100)
                    midi.addNote(track, 9, HI_HAT_CLOSE, tiempo, 0.5, 80)
            elif patrón == "coro":
                if beat == 0:
                    midi.addNote(track, 9, KICK, tiempo, 0.5, 110)
                    midi.addNote(track, 9, CRASH, tiempo, 1, 90)
                elif beat == 1:
                    midi.addNote(track, 9, SNARE, tiempo, 0.5, 110)
                    midi.addNote(track, 9, HI_HAT_OPEN, tiempo, 1, 80)
                elif beat == 2:
                    midi.addNote(track, 9, KICK, tiempo, 0.5, 110)
                    midi.addNote(track, 9, KICK, tiempo + 0.5, 0.5, 110)
                elif beat == 3:
                    midi.addNote(track, 9, SNARE, tiempo, 0.5, 110)
                    midi.addNote(track, 9, CRASH, tiempo, 0.5, 90)
            tiempo += 1
        return tiempo_inicio + 4
    
    # Función para agregar bajo
    def agregar_compas_bajo(track, tiempo_inicio, root):
        tiempo = tiempo_inicio
        for beat in range(4):
            midi.addNote(track, 0, root, tiempo, 0.5, 110)
            midi.addNote(track, 0, root + 12, tiempo + 0.5, 0.5, 110)
            midi.addNote(track, 0, root + 7, tiempo + 1, 0.5, 110)
            midi.addNote(track, 0, root + 12, tiempo + 1.5, 0.5, 110)
            tiempo += 2
        return tiempo_inicio + 4
    
    # Función para agregar power chords
    def agregar_compas_power_chord(track, tiempo_inicio, notas):
        tiempo = tiempo_inicio
        for beat in range(4):
            for nota in notas:
                midi.addNote(track, 1, nota, tiempo, 0.4, 105)
            tiempo += 1
        return tiempo_inicio + 4
    
    # Función para agregar melodía
    def agregar_compas_melodia(track, tiempo_inicio, notas):
        tiempo = tiempo_inicio
        for nota, duracion in notas:
            if nota is not None:
                midi.addNote(track, 2, nota, tiempo, duracion, 115)
            tiempo += duracion
        return tiempo_inicio + 4
    
    # 1. INTRO (4 compases)
    print("1. Generando Intro...")
    
    # Compases 1-2: Solo batería y bajo
    tiempos[tracks["batería"]] = agregar_compas_bateria(
        tracks["batería"], tiempos[tracks["batería"]], "normal"
    )
    tiempos[tracks["batería"]] = agregar_compas_bateria(
        tracks["batería"], tiempos[tracks["batería"]], "normal"
    )
    
    tiempos[tracks["bajo"]] = agregar_compas_bajo(
        tracks["bajo"], tiempos[tracks["bajo"]], C_MENOR_ROOT
    )
    tiempos[tracks["bajo"]] = agregar_compas_bajo(
        tracks["bajo"], tiempos[tracks["bajo"]], G_SOSTENIDO_ROOT
    )
    
    # Compases 3-4: Entra guitarra
    tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
        tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
        POWER_CHORD_C_MENOR
    )
    tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
        tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
        POWER_CHORD_G_SOSTENIDO
    )
    
    # Melodía de intro
    melodía_intro = [
        (72, 0.5), (None, 0.5), (70, 0.5), (None, 0.5),
        (68, 0.5), (None, 0.5), (67, 0.5), (None, 0.5),
    ]
    melodía_intro_2 = [
        (68, 0.5), (None, 0.5), (67, 0.5), (None, 0.5),
        (63, 0.5), (None, 0.5), (60, 0.5), (None, 0.5),
    ]
    
    tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
        tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
        melodía_intro
    )
    tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
        tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
        melodía_intro_2
    )
    
    print(f"   Intro: {4 * SEGUNDOS_POR_COMPAS:.1f} segundos")
    
    # Ajustar tiempos para que todo empiece junto después de 4 compases
    tiempo_inicio_secciones = 4 * 4  # 4 compases × 4 beats
    for track in tracks.values():
        tiempos[track] = tiempo_inicio_secciones
    
    # 2. ESTRUCTURA PRINCIPAL
    num_estrofa = 0
    num_coro = 0
    
    for seccion, compases in ESTRUCTURA:
        if seccion == "intro":
            continue
        
        print(f"2. Generando {seccion.upper()} ({compases} compases)...")
        
        if seccion == "estrofa":
            num_estrofa += 1
            acordes = obtener_acordes_seccion(seccion, compases)
            
            for i in range(compases):
                # Batería
                tiempos[tracks["batería"]] = agregar_compas_bateria(
                    tracks["batería"], tiempos[tracks["batería"]], "normal"
                )
                
                # Bajo
                root = acordes[i % len(acordes)][0]
                tiempos[tracks["bajo"]] = agregar_compas_bajo(
                    tracks["bajo"], tiempos[tracks["bajo"]], root
                )
                
                # Guitarra rítmica
                notas = acordes[i % len(acordes)][1]
                tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
                    tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
                    notas
                )
                
                # Guitarra melódica (melodía simple)
                melodías = [
                    [(60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),
                     (60, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)],
                    [(68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
                     (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5)],
                    [(60, 0.5), (63, 0.5), (67, 0.5), (70, 0.5),
                     (67, 0.5), (63, 0.5), (60, 0.5), (63, 0.5)],
                    [(65, 0.5), (68, 0.5), (72, 0.5), (68, 0.5),
                     (65, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)],
                ]
                tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
                    tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
                    melodías[i % 4]
                )
            
            print(f"   Estrofa {num_estrofa}: {compases * SEGUNDOS_POR_COMPAS:.1f} segundos")
        
        elif seccion == "coro":
            num_coro += 1
            acordes = obtener_acordes_seccion(seccion, compases)
            
            for i in range(compases):
                # Batería
                tiempos[tracks["batería"]] = agregar_compas_bateria(
                    tracks["batería"], tiempos[tracks["batería"]], "coro"
                )
                
                # Bajo
                root = acordes[i % len(acordes)][0]
                tiempos[tracks["bajo"]] = agregar_compas_bajo(
                    tracks["bajo"], tiempos[tracks["bajo"]], root
                )
                
                # Guitarra rítmica
                notas = acordes[i % len(acordes)][1]
                tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
                    tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
                    notas
                )
                
                # Guitarra melódica (melodía épica)
                melodías_coro = [
                    [(72, 0.5), (70, 0.5), (68, 0.5), (67, 0.5),
                     (68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5)],
                    [(68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
                     (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5)],
                    [(67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5),
                     (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5)],
                    [(70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5),
                     (67, 0.5), (68, 0.5), (70, 0.5), (72, 0.5)],
                ]
                tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
                    tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
                    melodías_coro[i % 4]
                )
            
            print(f"   Coro {num_coro}: {compases * SEGUNDOS_POR_COMPAS:.1f} segundos")
        
        elif seccion == "puente":
            acordes = obtener_acordes_seccion(seccion, compases)
            
            for i in range(compases):
                # Batería (patrón normal)
                tiempos[tracks["batería"]] = agregar_compas_bateria(
                    tracks["batería"], tiempos[tracks["batería"]], "normal"
                )
                
                # Bajo (más melódico)
                root = acordes[i % len(acordes)][0]
                tiempos[tracks["bajo"]] = agregar_compas_bajo(
                    tracks["bajo"], tiempos[tracks["bajo"]], root
                )
                
                # Guitarra rítmica
                notas = acordes[i % len(acordes)][1]
                tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
                    tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
                    notas
                )
                
                # Guitarra melódica (más melódica)
                melodías_puente = [
                    [(60, 0.5), (63, 0.5), (67, 0.5), (72, 0.5),
                     (70, 0.5), (68, 0.5), (67, 0.5), (63, 0.5)],
                    [(68, 0.5), (67, 0.5), (63, 0.5), (60, 0.5),
                     (63, 0.5), (67, 0.5), (70, 0.5), (68, 0.5)],
                    [(72, 0.5), (70, 0.5), (68, 0.5), (67, 0.5),
                     (63, 0.5), (60, 0.5), (63, 0.5), (67, 0.5)],
                    [(65, 0.5), (68, 0.5), (72, 0.5), (70, 0.5),
                     (68, 0.5), (65, 0.5), (63, 0.5), (60, 0.5)],
                ]
                tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
                    tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
                    melodías_puente[i % 4]
                )
            
            print(f"   Puente: {compases * SEGUNDOS_POR_COMPAS:.1f} segundos")
        
        elif seccion == "outro":
            acordes = obtener_acordes_seccion("estrofa", compases)
            
            for i in range(compases):
                # Batería (patrón normal)
                tiempos[tracks["batería"]] = agregar_compas_bateria(
                    tracks["batería"], tiempos[tracks["batería"]], "normal"
                )
                
                # Bajo
                root = acordes[i % len(acordes)][0]
                tiempos[tracks["bajo"]] = agregar_compas_bajo(
                    tracks["bajo"], tiempos[tracks["bajo"]], root
                )
                
                # Guitarra rítmica
                notas = acordes[i % len(acordes)][1]
                tiempos[tracks["guitarra_ritmica"]] = agregar_compas_power_chord(
                    tracks["guitarra_ritmica"], tiempos[tracks["guitarra_ritmica"]], 
                    notas
                )
                
                # Guitarra melódica
                melodías = [
                    [(60, 0.5), (63, 0.5), (67, 0.5), (63, 0.5),
                     (60, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)],
                    [(68, 0.5), (67, 0.5), (63, 0.5), (67, 0.5),
                     (68, 0.5), (70, 0.5), (67, 0.5), (63, 0.5)],
                    [(60, 0.5), (63, 0.5), (67, 0.5), (70, 0.5),
                     (67, 0.5), (63, 0.5), (60, 0.5), (63, 0.5)],
                    [(65, 0.5), (68, 0.5), (72, 0.5), (68, 0.5),
                     (65, 0.5), (63, 0.5), (65, 0.5), (63, 0.5)],
                ]
                tiempos[tracks["guitarra_melodica"]] = agregar_compas_melodia(
                    tracks["guitarra_melodica"], tiempos[tracks["guitarra_melodica"]], 
                    melodías[i % 4]
                )
            
            print(f"   Outro: {compases * SEGUNDOS_POR_COMPAS:.1f} segundos")
    
    # Calcular duración total
    tiempo_total_beats = tiempos[tracks["batería"]]
    tiempo_total_segundos = tiempo_total_beats * (60 / TEMPO)
    
    print()
    print("=" * 50)
    print(f"DURACIÓN TOTAL: {tiempo_total_beats} beats")
    print(f"                {tiempo_total_segundos:.1f} segundos")
    print(f"                {int(tiempo_total_segundos // 60)}:{int(tiempo_total_segundos % 60):02d}")
    print("=" * 50)
    
    return midi

def guardar_midi(midi, nombre_archivo="output/necrofilia.mid"):
    """Guarda el archivo MIDI"""
    import os
    
    # Crear directorio output si no existe
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
    
    with open(nombre_archivo, "wb") as archivo:
        midi.writeFile(archivo)
    
    print(f"\nArchivo MIDI guardado: {nombre_archivo}")
    print(f"Tamaño: {os.path.getsize(nombre_archivo)} bytes")
    
    return nombre_archivo

if __name__ == "__main__":
    # Generar MIDI
    midi = crear_midi()
    
    # Guardar archivo
    archivo = guardar_midi(midi)
    
    print("\n¡Listo! Puedes abrir el archivo MIDI en cualquier reproductor o DAW.")
    print("Para escuchar en Termux, puedes usar: ffplay output/necrofilia.mid")
