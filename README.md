## Pygame Projekt:  Space Invaders Clone

### 🎮 Game Übersicht

Ein klassischer **Space Invaders Klon** entwickelt mit Pygame

**Spielsteuerung:**
- **← / A** und **→ / D**:  Raumschiff bewegen
- **Leertaste**: Schiessen
- **R**: Neustart nach Game Over
- **Q**: Spiel beenden

**Features:**
- 🚀 Spieler Raumschiff mit Bewegung und Schussmechanik
- 👾 Alien Gruppe mit intelligenter Formation und Bewegung
- 💥 Kollisionserkennung zwischen Schüssen und Aliens/Spieler
- 💯 Punktesystem und HUD (Score & Leben)
- 🔫 Alien Gegenangriff mit zufälligen Schüssen
- 🛡️ Unverwundbarkeits Timer nach Treffer
- 🏆 Game Over und Victory Screens

### 🔍 Interessante Code Stellen

| Feature | Code Location | Beschreibung |
|---------|--------------|--------------|
| **Spieler Klasse** | [`Player` (Zeilen 26-71)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L26-L71) | Bewegung, Schiessen, Schadensmechanik mit Invincibility Frames |
| **Alien Klasse** | [`Alien` (Zeilen 96-120)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L96-L120) | Alien Bewegung, Edge Detection und Formation Logik |
| **Kollisionserkennung** | [Game Loop (Zeilen 246-276)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L246-L276) | Bullet Alien und Alien Player Kollisionen |
| **Bullet System** | [`Bullet` (Zeilen 74-93)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L74-L93) | Schuss Logik und Bewegung |
| **HUD System** | [`HUD` (Zeilen 155-170)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L155-L170) | Score und Leben Anzeige |
| **Main Game Loop** | [Game Loop (Zeilen 210-317)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L210-L317) | Event Handling, Update Logik und Rendering |
| **Game Over/Victory** | [Draw Functions (Zeilen 190-197)](https://github.com/muicmateo/Lern-Atelier-12/blob/21ee44a81f6368f071ebf8f5409d6e0a28a718c2/shooter_game.py#L190-L197) | End Screen Darstellung |


### Technologien

Ich will die Pygame-Bibliothek richtig kennenlernen. Also:
1.  Event Handling: Wie reagiere ich auf Tastendrücke (Schüsse, Bewegung)?
2.  Sprites und Kollisionen: Wie bewege ich Bilder (Schiff, Aliens) und erkenne, wenn sie sich treffen?
3.  OOP (Objektorientierte Programmierung) in Python 

### Grobe Beschreibung des Projekts

Ich werde einen simplen "Space Invaders"-Klon mit Pygame entwickeln. Das ist ein Shooter, bei dem ich mein Schiff unten bewege und von oben kommende Aliens abschiessen muss. 


### 7 User Stories (Epics)


#### Epic 1: Spieler-Bewegung
* Als Spieler möchte ich mein Raumschiff mit Pfeiltasten/A, D nach links und rechts bewegen können, damit ich den Alien-Schüssen ausweichen kann.
    * *Arbeitspakete:*
        - [x]  Einrichtung des Spieler-Sprites.
        - [x]  Implementierung der horizontalen Bewegung.
        - [x]  Begrenzung der Bewegung im Fenster.
        - [x]  Erstellung der Spieler-Klasse.

#### Epic 2: Schuss-Funktion
* Als Spieler möchte ich mit der Leertaste Schüsse abfeuern können, damit ich die feindlichen Aliens treffen und zerstören kann.
    * *Arbeitspakete:*
        - [x]  Erstellung der Bullet-Klasse für Schuss-Objekte.
        - [x]  Implementierung der Schuss-Bewegung nach oben.
        - [x]  Registrierung der Leertaste für das Abfeuern von Schüssen.
        - [x]  Entfernung von Schüssen, die den Bildschirm verlassen.


#### Epic 3: Alien-Gruppe
* Als System sollen mehrere Aliens in einer Gruppe oben auf dem Bildschirm erscheinen und sich hin und her bewegen, damit eine Bedrohung entsteht.
    * *Arbeitspakete:*
        - [x]  Erstellung der Alien-Klasse.
        - [x]  Generierung einer Alien-Gruppe in Reihen und Spalten.
        - [x]  Implementierung der horizontalen Alien-Bewegung.
        - [x]  Richtungswechsel und Abwärtsbewegung bei Bildschirmrand.


#### Epic 4: Treffer-Logik 
* Als System möchte ich erkennen, wenn ein Spieler-Schuss einen Alien trifft, damit der Alien verschwindet und ich Punkte bekomme.
    * *Arbeitspakete:*
        - [x]  Implementierung der Kollisionserkennung zwischen Bullets und Aliens.
        - [x]  Entfernung getroffener Aliens aus der Alien-Liste.
        - [x]  Entfernung des Schusses nach Treffer.
        - [x]  Einführung eines Punktesystems und Erhöhung bei Alien-Treffer.


#### Epic 5: HUD 
* Als Spieler möchte ich meine aktuellen Punkte und meine verbleibenden Leben sehen, damit ich meinen Spielstand kenne.
    * *Arbeitspakete:*
        - [x]  Anzeige der aktuellen Punktzahl auf dem Bildschirm.
        - [x]  Anzeige der verbleibenden Leben des Spielers.
        - [x]  Erstellung einer Textdarstellung mit pygame.font.
        - [x]  Positionierung des HUD am oberen Bildschirmrand.


#### Epic 6: Alien-Gegenangriff
* Als System sollen die Aliens ebenfalls Schüsse abgeben und diese treffen mich, damit ich eine Herausforderung habe und Leben verlieren kann.
    * *Arbeitspakete:*
        - [x]  Implementierung zufälliger Alien-Schüsse.
        - [x]  Bewegung der Alien-Schüsse nach unten.
        - [x]  Kollisionserkennung zwischen Alien-Schüssen und Spieler.
        - [x]  Reduzierung der Spieler-Leben bei Treffer.


#### Epic 7: Spielende und Neustart
* Als Spieler möchte ich nach dem Verlieren aller Leben einen "Game Over"-Bildschirm sehen, damit ich das Spiel beenden oder neu starten kann.
