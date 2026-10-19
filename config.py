# Configuración musical - Necrofilia
# Tonalidad: Cm (relativa menor de Eb)
# Género: Rock/Punk (Green Day + Muse)

# Tempo y compás
TEMPO = 160  # BPM
COMPAS = 4   # Tiempos por compás
NOTAS_POR_COMPAS = 4

# Duración en segundos
SEGUNDOS_POR_COMPAS = 60 / TEMPO * COMPAS  # 1.5 segundos

# Canales MIDI (0-indexed)
CHANNEL_BATERIA = 9    # Canal 10 en MIDI (percusión)
CHANNEL_BAJO = 0
CHANNEL_GUITARRA_RITMICA = 1
CHANNEL_GUITARRA_MELODICA = 2
CHANNEL_TECLADO = 3

# Volúmenes (0-127)
VOL_BATERIA = 100
VOL_BAJO = 110
VOL_GUITARRA_RITMICA = 105
VOL_GUITARRA_MELODICA = 115
VOL_TECLADO = 80

# Notas MIDI (octava 4 = 60-71)
# Cm = C Eb G
# G# = Ab Cb Eb = Ab B Eb (enarmónico)
# Fm = F Ab C
# D# = Eb G Bb
# A# = Bb D F

# Root notes para cada acorde (octava baja para bajo, octava 4 para acordes)
C_MENOR_ROOT = 36      # C2
G_SOSTENIDO_ROOT = 44  # Ab2/G#2
F_MENOR_ROOT = 41      # F2
D_SOSTENIDO_ROOT = 39  # Eb2/D#2
A_SOSTENIDO_ROOT = 46  # Bb2/A#2

# Acordes en notación MIDI (para guitarra/teclado)
ACORDE_C_MENOR = [48, 51, 55]      # C3, Eb3, G3
ACORDE_G_SOSTENIDO = [44, 48, 51]  # Ab2, C3, Eb3
ACORDE_F_MENOR = [41, 44, 48]      # F2, Ab2, C3
ACORDE_D_SOSTENIDO = [39, 43, 46]  # Eb2, G2, Bb2
ACORDE_A_SOSTENIDO = [46, 50, 53]  # Bb2, D3, F3

# Power chords para guitarra rítmica (octava 3-4)
POWER_CHORD_C_MENOR = [48, 55, 60]      # C3, G3, C4
POWER_CHORD_G_SOSTENIDO = [44, 51, 56]  # Ab2, Eb3, Ab3
POWER_CHORD_F_MENOR = [41, 48, 53]      # F2, C3, F3
POWER_CHORD_D_SOSTENIDO = [39, 46, 51]  # Eb2, Bb2, Eb3
POWER_CHORD_A_SOSTENIDO = [46, 53, 58]  # Bb2, F3, Bb3

# Introducción
COMPAS_INTRO = 4  # 2 compases solo batería+bajo, 2 compases + guitarra

# Estructura de la canción
ESTRUCTURA = [
    ("intro", 4),           # 4 compases
    ("estrofa", 8),         # 8 compases (2x patrón de acordes)
    ("coro", 8),            # 8 compases (acordes doble duración)
    ("estrofa", 8),
    ("coro", 8),
    ("puente", 4),
    ("coro", 8),
    ("outro", 4),
]

# Nombres de las notas
NOTAS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def nota_a_nombre(nota_midi):
    """Convierte número MIDI a nombre de nota"""
    nota = nota_midi % 12
    octava = (nota_midi // 12) - 1
    return f"{NOTAS[nota]}{octava}"

def nombre_a_nota(nombre):
    """Convierte nombre de nota a número MIDI"""
    nota = nombre[:-1]
    octava = int(nombre[-1])
    return (octava + 1) * 12 + NOTAS.index(nota)
