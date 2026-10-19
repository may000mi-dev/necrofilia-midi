# Necrofilia - Rock/Punk

## Descripción
Canción original de **Auge BO** en género Rock/Punk (estilo Green Day + Muse).

## Características
- **Tonalidad:** Cm (Do menor)
- **Tempo:** 160 BPM
- **Compás:** 4/4
- **Género:** Rock/Punk

## Estructura
1. **Intro** (4 compases): Batería + bajo (2 compases) → guitarra con reverb entra (2 compases)
2. **Estrofa 1** (8 compases): Patrón punk con power chords
3. **Coro 1** (8 compases): Acordes con doble duración, más intenso
4. **Estrofa 2** (8 compases)
5. **Coro 2** (8 compases)
6. **Puente** (4 compases): Momento melódico/emocional
7. **Coro Final** (8 compases): Clímax
8. **Outro** (4 compases): Cierre

## Acordes
- **Cm** (Do menor)
- **G#** (Sol sostenido / Ab)
- **Fm** (Fa menor)
- **D#** (Re sostenido / Eb)
- **A#** (La sostenido / Bb)

## Instrumentos (MIDI)
1. Batería (canal 10)
2. Bajo
3. Guitarra rítmica (power chords)
4. Guitarra melódica (líneas principales)
5. Teclado/Sintetizador (pads, arpegios, lead)

## Instalación
```bash
pip install midiutil numpy
```

## Uso
```bash
python generar_midi.py
```

El archivo MIDI se generará en `output/necrofilia.mid`.

## Ver letra
```bash
python letra.py
```

## Archivos
- `config.py` - Configuración musical
- `acordes.py` - Progresiones de acordes
- `bateria.py` - Patrones de batería
- `bajo.py` - Líneas de bajo
- `guitarra_ritmica.py` - Power chords
- `guitarra_melodica.py` - Melodías principales
- `teclado.py` - Arreglos de sintetizador
- `letra.py` - Letra de referencia
- `generar_midi.py` - Script principal

## Notas
- La letra es solo de referencia, puede ser modificada
- El MIDI es un prototipo; la producción final se hará en un DAW
- Compatible con Termux (Android)
