# Definición de acordes y progresiones - Necrofilia
from config import *

# Progresión de acordes para cada sección
# Cada tupla: (acorde_root, notas_acorde, duracion_compases)
PROGRESION_ESTROFA = [
    (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 1),
    (G_SOSTENIDO_ROOT, POWER_CHORD_G_SOSTENIDO, 1),
    (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 1),
    (F_MENOR_ROOT, POWER_CHORD_F_MENOR, 1),
]

PROGRESION_CORO = [
    (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 2),
    (G_SOSTENIDO_ROOT, POWER_CHORD_G_SOSTENIDO, 2),
    (D_SOSTENIDO_ROOT, POWER_CHORD_D_SOSTENIDO, 2),
    (A_SOSTENIDO_ROOT, POWER_CHORD_A_SOSTENIDO, 2),
]

PROGRESION_PUENTE = [
    (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 1),
    (G_SOSTENIDO_ROOT, POWER_CHORD_G_SOSTENIDO, 1),
    (C_MENOR_ROOT, POWER_CHORD_C_MENOR, 1),
    (F_MENOR_ROOT, POWER_CHORD_F_MENOR, 1),
]

# Acordes completos para teclado (arreglos)
ACORDES_COMPLETOS = {
    "Cm": ACORDE_C_MENOR,
    "G#": ACORDE_G_SOSTENIDO,
    "Fm": ACORDE_F_MENOR,
    "D#": ACORDE_D_SOSTENIDO,
    "A#": ACORDE_A_SOSTENIDO,
}

def obtener_progresion(seccion):
    """Retorna la progresión de acordes para una sección"""
    if seccion == "estrofa" or seccion == "puente":
        return PROGRESION_ESTROFA
    elif seccion == "coro":
        return PROGRESION_CORO
    return PROGRESION_ESTROFA

def obtener_acordes_seccion(seccion, num_compases):
    """Genera la secuencia completa de acordes para una sección"""
    progresion = obtener_progresion(seccion)
    acordes = []
    compases_restantes = num_compases
    
    while compases_restantes > 0:
        for root, notas, duracion in progresion:
            if compases_restantes <= 0:
                break
            duracion_real = min(duracion, compases_restantes)
            acordes.append((root, notas, duracion_real))
            compases_restantes -= duracion_real
    
    return acordes
