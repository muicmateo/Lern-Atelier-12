## Pygame-Projekt 


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


#### Epic 4: Treffer-Logik 
* Als System möchte ich erkennen, wenn ein Spieler-Schuss einen Alien trifft, damit der Alien verschwindet und ich Punkte bekomme.


#### Epic 5: HUD 
* Als Spieler möchte ich meine aktuellen Punkte und meine verbleibenden Leben sehen, damit ich meinen Spielstand kenne.


#### Epic 6: Alien-Gegenangriff
* Als System sollen die Aliens ebenfalls Schüsse abgeben und diese treffen mich, damit ich eine Herausforderung habe und Leben verlieren kann.


#### Epic 7: Spielende und Neustart
* Als Spieler möchte ich nach dem Verlieren aller Leben einen "Game Over"-Bildschirm sehen, damit ich das Spiel beenden oder neu starten kann.
