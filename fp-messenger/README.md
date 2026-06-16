# FP Messenger · Castilla y León 🧭

Réplica **MVP** inspirada en [messenger.abeto.co](https://messenger.abeto.co/),
enfocada en la **Formación Profesional de Castilla y León**.

Caminas como mensajero/a sobre un **planeta esférico**. Cada casa representa una
**familia profesional de FP** (un hospital, un taller de coches, una granja, un
centro TIC…). Una **brújula 3D te persigue** flotando a tu lado y su aguja apunta
siempre al edificio más cercano. Al acercarte a un edificio, se abre un panel con
información del ciclo de FP correspondiente en Castilla y León.

## Cómo ejecutarlo

Es estático (sin build). Solo necesita un servidor HTTP por los módulos ES:

```bash
cd fp-messenger
python3 -m http.server 8000
# abre http://localhost:8000
```

> Three.js se carga por CDN (unpkg) mediante un *import map*, así que necesita
> conexión a internet la primera vez.

## Controles

- **Mover:** `W A S D` o flechas (en móvil, botones en pantalla).
- **Avanzar/retroceder** sobre la superficie y **girar** a izquierda/derecha.
- Acércate a un edificio para ver su información de FP.

## Edificios → familias de FP incluidas

| Edificio | Familia profesional |
|---|---|
| 🏥 Hospital | Sanidad |
| 🔧 Taller de coches | Transporte y Mantenimiento de Vehículos |
| 💻 Centro TIC | Informática y Comunicaciones |
| 🍽️ Restaurante | Hostelería y Turismo |
| 🌾 Granja | Agraria |
| ⚡ Subestación | Electricidad y Electrónica |

## Estructura

- `index.html` — estructura y UI (HUD, panel, controles, intro).
- `style.css` — estilos.
- `main.js` — escena 3D (Three.js): planeta, personaje, brújula, movimiento esférico.
- `data.js` — datos orientativos de FP de Castilla y León.

## Notas

- Assets generados por código (low-poly) — sin copiar recursos del original.
- Los datos de FP son **orientativos** (familias profesionales, ciclos de ejemplo,
  duración y salidas). Para la oferta oficial y actualizada, consulta el portal de
  educación de la Junta de Castilla y León (Educacyl).

## Próximos pasos posibles

- Multijugador en tiempo real (otros mensajeros visibles).
- Misiones reales de "reparto" entre edificios.
- Datos en vivo desde una API de oferta de FP.
- Modelos 3D dedicados y sonido.
