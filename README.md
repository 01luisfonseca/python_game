# Invasión Espacial 🚀

Un juego de arcade estilo Space Invaders desarrollado en Python usando Pygame.

## Descripción 📝

Invasión Espacial es un juego clásico de arcade donde controlas una nave espacial y debes defenderte de una invasión alienígena. Los enemigos se vuelven más fuertes y rápidos a medida que avanzas de nivel.

## Características 🎮

- Control de nave espacial con movimiento en 4 direcciones
- Sistema de disparos
- Enemigos con IA que se mueven de forma aleatoria
- Enemigos que disparan hacia el jugador
- Sistema de puntuación
- Múltiples niveles de dificultad
- Efectos de sonido y música de fondo
- Rotación de proyectiles para apuntar al jugador

## Requisitos 📋

- Python 3.x
- Pygame

## Instalación 🔧

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/invasion-espacial.git
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo Jugar 🎯

1. Ejecuta el juego:

```bash
python main.py
```

2. Controles:

- Flechas direccionales: Mover la nave
- Espacio: Disparar
- ESC: Salir del juego o reiniciar el juego en caso de que el jugador muera

## Mecánicas del Juego 🎲

- Cada enemigo eliminado otorga 10 puntos multiplicados por el nivel actual
- Los enemigos se vuelven más rápidos y agresivos en niveles superiores
- Los enemigos de nivel 10 o superior pueden disparar
- El juego termina cuando tu nave es destruida

## Estructura del Proyecto 📁

```markdown
invasion-espacial/
├── main.py           # Punto de entrada del juego
├── classes.py        # Clases del juego (Player, Enemy, Bullet)
├── requirements.txt  # Dependencias del proyecto
├── README.md        # Este archivo
├── alien.png        # Sprite de los enemigos
├── spaceship.png    # Sprite de la nave del jugador
├── bullet.png       # Sprite de los proyectiles del jugador
├── bullet_enemy.png # Sprite de los proyectiles enemigos
├── background2.jpg  # Imagen de fondo del juego
├── disparo.mp3      # Efecto de sonido de disparo
├── Golpe.mp3        # Efecto de sonido de impacto
├── dead.mp3         # Efecto de sonido de destrucción
├── MusicaFondo.mp3  # Música de fondo
└── Fastest.ttf      # Fuente para el texto del juego
```

## Contribuir 🤝

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios que te gustaría hacer.

## Licencia 📄

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. El proyecto fue desarrollado como parte de un trabajo de fin de curso en Python en Udemy.

## Créditos 👏

Desarrollado por Luis Fonseca.

Los sprites fueron obtenidos de [Flaticon](https://www.flaticon.es/).
