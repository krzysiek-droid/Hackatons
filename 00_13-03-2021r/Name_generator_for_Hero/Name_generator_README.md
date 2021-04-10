# **Name Generator**

Celem projektu było stworzenie programu generującego losowe imie z licznikiem i przydomkiem dla postaci wojownika gry RPG.

Użyte technologie:
- pętle: for;while
- bool'e: if, elif, else
- biblioteki: random
- listy i krotki
- zdefiniowane przez programistę funkcje (zamiana liczb numerycznych na rzymskie)
- funkcje przypisane do klasy String i klasy List (capitalize, join etc.)

Program generuje losowe samogłoski i spółgłoski przy użyciu funkcji random dla zdefiniowanych list tych liter
Tworzenie imienia jest uwarunkowowane:
- obok siebie nie może być więcej niż 2 spółgłoski
- dwie spółgłoski nie mogą tworzyć "zabronionej" kombinacji, którą ciężko wymówić
- nie może występowac więcej niż jedna samogłoska obok siebie