Úvod
====

Úvodní kapitola obsahující motivaci proč pracovat s nástroji open source GIS,
přehled zdrojů, odkazy na komunitní skupiny světové i lokální.

Proč GIS
--------

:wikipedia:`Geografický_informační_systém` je na počítačích založený informační
systém pro získávání, ukládání, analýzu a vizualizaci dat, která mají prostorový
vztah k povrchu Země. Geodata, se kterými GIS pracuje, jsou definována svou
geometrií, topologií, atributy a dynamikou.

Geografický informační systém umožňuje vytvářet modely části zemského povrchu
pomocí dostupných softwarových a hardwarových prostředků. Takto vytvořený model
lze pak využít například při evidenci katastru nemovitostí, předpovídání vývoje
počasí, určování záplavových zón řek, výběru vhodné lokace pro čistírnu
odpadních vod, plánování výstavby silnic apod.

GIS se skládá z
* Hardware
* Software
* Data
* Pracovníci

Geodata, geoobjekty
-------------------
GIS pracuje s prostorovými daty -- `geodaty`. Geodata se skládají z jednotlivých
(geo)objektů. Každý objekt představuje model prvku reálného světa. Každý objekt
obsahuje jednak

* prostorovou informaci (informaci o tvaru, umístění na zemském povrchu)
* atributové informace (nejčastěji popisné vlastnosti každého prvku).

Datový model
------------
Jak řečeno -- pomocí nástrojů GIS vytváříme modely objektů reálného světa.
Spojité fenomény (nadmořská výška, srážková mapa, teplotní mapa a pod.) se
nejčastěji modeluje pomocí rastrového formátu.

Diskrétní prvky (katastr, uliční síť, mapa výskytu vorvaňů) se nejčastěji
modeluje pomocí vektorového formátu.

Rastrový formát
    Představuje nejčastěji uspořádanou matici hodnot (pixelů). Pixely mohou být
    i 3D, pak hovoříme o tzv. voxelech - volume pixel

Vektorový formát
    Objekt je popsán nejčastěji svým obrysem pomocí párů (ve 3D tripletů)
    souřadnic lomových bodů. Nejčastěji si v rámci vektorového modelu vystačíme
    s body nebo liniemi či polygony.

Proč Open Source
----------------
:wikipedia:`Otevřený_software` (open source), počítačový software, jehož licence
umožňuje

* Studovat zdrojový kód
* Měnit zdrojový kód
* Zdrojový kód dále distribuovat

Open Source není business model, ale vývojový model. Způsob práce se software
předurčuje, jakým způsobem probíhá komunikace mezi vývojáři a mezi uživateli a
vývojáři. 


Komunita
--------
U dobrých open source projektů existuje silná a zdravá komunita vývojářů a
uživatelů. Rozhodovací procesy jsou otevřené a dokumentovatelé. 

Komunita je často prvním místem podpory, kterou může uživatel nebo začínající
vývojář dostat.

Způsob financování
------------------
Nic není zadarmo - ani práce vývojářů otevřeného software. Protože každý může
získat drojový kód, nelze stavět obchod na prodeji krabicových verzí. Business
model je častěji stavěn okolo podpory, plnění určitých úloh pomocí open source
software, ale cena za software není součástí plnění.

OSGeo.org
---------
`Open Source Geospatial Foundation <http://osgeo.org>`_ je ve Spojených státech
registrované nezisková organizace, která se stará o podporu open source software
pro práci s prostorovými daty. Podpora je právní, infrastrukturní i technická.
Většina nejrozšířenějších projektů je registrována jako tzv. OSGeo Projekt, což
znamená že prošli inkubační fází, která garantuje určitou kvalitu software,
zrojový kód nezatížený patentovými spory a dostatečně velkou a zdravou komunitu
okolo projektu.

OSGeo.cz
--------
`Spolek Otevřená GeoInfrastruktura <http://osgeo.cz>`_ je český registrovaný
spolek, který se stará o podporu otevřeného software pro GIS a otevřených
prostorových dat.
