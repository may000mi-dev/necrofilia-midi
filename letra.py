# Letra de referencia - Necrofilia
# Tema: Amor que trasciende la muerte, pasión extrema
# Estilo: Rock/Punk (Green Day + Muse)

LETRA = {
    "intro": "",  # Sin letra
    
    "estrofa_1": """
En la oscuridad de tu ausencia
busco tu calor entre las sombras
tu piel fría como el mármol
me encadena a esta pasión

No me importa lo que digan
ni las leyes de los vivos
tu silencio es mi alimento
tu olvido es mi camino
""",
    
    "coro_1": """
Necrofilia de mi alma
amor que cruza la frontera
donde la muerte no existe
solo tu cuerpo y mi hambre

Necrofilia de mi vida
pasión que nunca se apagará
hasta que el mundo se acabe
yo te amaré más allá
""",
    
    "estrofa_2": """
Tus ojos vacíos me miran
como si todavía vivieras
tu boca fría besa mi alma
y me devuelves a la vida

Cada noche te visito
en este sueño sin final
tu amor es mi única ley
tu muerte es mi eternidad
""",
    
    "coro_2": """
Necrofilia de mi alma
amor que cruza la frontera
donde la muerte no existe
solo tu cuerpo y mi hambre

Necrofilia de mi vida
pasión que nunca se apagará
hasta que el mundo se acabe
yo te amaré más allá
""",
    
    "puente": """
¿Quién dijo que el amor muere?
¿Quién dijo que la muerte es el final?
Yo te amo más que a mi vida
y mi vida es solo para ti

No hay pecado en esta pasión
no hay culpa en este deseo
tu cuerpo es mi templo sagrado
y yo soy tu devoto fiel
""",
    
    "coro_final": """
Necrofilia de mi alma
amor que cruza la frontera
donde la muerte no existe
solo tu cuerpo y mi hambre

Necrofilia de mi vida
pasión que nunca se apagará
hasta que el mundo se acabe
yo te amaré más allá

Necrofilia de mi ser
amor más allá de la muerte
tu eternidad es mi prisión
y yo soy tu eterno amante
""",
    
    "outro": "",  # Instrumental
}

# Estructura para guiar la composición
ESTRUCTURA_LETRA = [
    ("intro", 4, ""),
    ("estrofa", 8, "estrofa_1"),
    ("coro", 8, "coro_1"),
    ("estrofa", 8, "estrofa_2"),
    ("coro", 8, "coro_2"),
    ("puente", 4, "puente"),
    ("coro", 8, "coro_final"),
    ("outro", 4, ""),
]

def obtener_letra_seccion(seccion, num_seccion):
    """Retorna la letra para una sección específica"""
    clave = f"{seccion}_{num_seccion}" if num_seccion > 1 else seccion
    return LETRA.get(clave, "")

def mostrar_letra_completa():
    """Muestra la letra completa formateada"""
    print("=" * 60)
    print("NECROFILIA - Letra de Referencia")
    print("Género: Rock/Punk (Green Day + Muse)")
    print("Tonalidad: Cm | Tempo: 160 BPM")
    print("=" * 60)
    
    for seccion, compases, clave in ESTRUCTURA_LETRA:
        if clave:
            print(f"\n{'=' * 40}")
            print(f"{seccion.upper()} ({compases} compases)")
            print("=" * 40)
            print(LETRA[clave].strip())
    
    print("\n" + "=" * 60)
    print("NOTA: Esta letra es solo de referencia.")
    print("Puedes modificarla según tu visión artística.")
    print("=" * 60)

if __name__ == "__main__":
    mostrar_letra_completa()
