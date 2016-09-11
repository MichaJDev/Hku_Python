**Uitleg Lab2**

> We beginnen de opdracht met het aanmaken van alle benodigde variablen, ik heb deze totaal geen namen gegeven die ergens op slaan ze zijn gewoon van alfabetische volgorde

```python
a = 0
b = 0
c = False
d = 0
e = 20
f = False
```

> Als we dit gedaan hebben gaan we onze eerste voorgebouwde functie defineren, dit is de functie "setup()" de beginnen we als volgt.

```python
def setup():
``` 

> als we dit getypt dan drukken we op enter zodat hij automatisch voor ons inspringt (als je processing gebruikt), 
nu typen we in hoe groot het venster word waar we in gaan werken en de achtergrond en als we een lijn om onze rectangle en ellipse willen of niet
onze achtegrond word zwart en we willen geen omlijning

> als je een lijn om alle getekende objecten wilt dan hoef je het gedeelte "noStroke()" niet toe te voegen, wil je dat niks een omlijning heeft doe dan als volgt

```python
size(400,400)
background(0)
noStroke()
```

> zodra we dit gedaan hebben weet python wat ons werk vlak word, nu als je op play drukt in het processing zie je dat python een scherm van
400 bij 400 maakt met de achtergrond zwart, je ziet nog niks met de omlijning gebeuren aangezien we nog niks hebben getekent dat doen we nu 

> we gaan nu werken met de voorgebouwde functie draw deze defineer je als volgt

```python
def draw():
```

> Dit zorgt er voor dat alles word gehandteerd hoe je iets wilt tekenen.
hier in gaan we alle variablen opvragen, dit doen we met 'global' voor onze variablen naam te zetten . dus als volgt.

```python
global a
global b
global c
global d
global e
global f
```

> als we dit gedaan hebben gaan we onze rectangle tekenen net zoals we in lab 1 gedaan hebben.
we geven hem de kleur blauw en maken hem de grote die we willen

```python
fill(0,0,255)
rect(a,b,80,80)
```

> zoals je kunt zien heb ik hier a en b in gebruikt als de coordinaten van het rectangle, a en b zijn allebei 0 zodat ze linksboven in het scherm beginnen
nu gaan we er voor zorgen dat onze rectangle van links boven naar rechts onder te laten bewegen en deze weer terug te laten komen
dit doen we doormiddle van de c variable die een boolean is (True of False)

```python
if(c == False):
  a = (a + 1) % width
  b = (b + 1) % height
  if(a >= 360 and b >= 360):
      c = True
else:
  a = (a - 1) % width
  b = (b - 1) % height
  if(a <= 0 and b <= 0):
      c = False
```

> Laten we dit even opbreken in meerdere delen zodat ik het kan uitleggen

```python
if(c == False):
```

> Dit betekent "*als* **C** **_niet waar_** is doe dan: **dit** " C heb je hierboven gedefineerd dat hij niet waar was (False)
daarna gaan we de a en de b variablen aanpassen die we gebruiken als x en y coordinaten van het rectangle (rect(**a**,**b**,80,80))

```python
a = (a + 1) % width
b = (b + 1) % height
```

> voeg 1 aan de a en b toe, gezien de breedte en hoogte van het scherm. zodat de rectangle van links boven (coordinaten 0,0) naar schuinonder (coordinaten 360,360) loopt

```python
  if(a >= 360 and b >= 360):
      c = True
```
> Hier zeg is als a en b grote of gelijk aan 360 zijn zet C dan op True
Dit is nodig om te zien als C veranderd is anders zal hij niet de andere kant op gaan als hij tegen de rand aan zit van het scherm.

```python
else:
```

> Else betekent letterlijk 'anders dit' oftewel het tegenover gestelde of alle andere dingen

```python
a = (a-1) % width
b = (b-1) % height
```
> haal 1 van a en b af in gelijkstelling tot de hoogte en breedte van het scherm. zodat de rectangle weer terug gaan naar schuinboven

```python
if(a <= 0 and b <= 0):
    c = False
```

> als a en b kleiner of gelijk aan 0 zijn verander c dan in false zodat hij de normale richting weer aan neemt zoals hiervoor.

>hier na ga ik verder met het maken van de ellipse die eigenlijk alleen naar rechts moest gaan maar ik hem ook gewoon heb laten bouncen omdat ik dit grappig vond
Dit is precies de zelfde werk richting alleen heb je hier dan verschillende variablen voor maar het is precies het zelfde geprogrammeerd behalve dan dat hij alleen
de breedte veranderd en de hoogte gewoon het zelfde laat.
