Úvod
====

Úvodní kapitola nastiňuje motivaci, proč pracovat s nástroji open source GIS. Dále poskytuje
přehled zdrojů, odkazy na komunitní skupiny světové i lokální.

Proč GIS
--------

:wikipedia:`Geografický informační systém` (GIS) je na počítačích
založený informační systém pro získávání, ukládání, analýzu a
vizualizaci dat, která mají prostorový vztah k povrchu Země (hovoříme
o geografických datech, zkráceně *geodatech*). Geodata, se kterými GIS
pracuje, jsou definována svou *geometrií*, *topologií*, *atributy* a
*dynamikou*.

GIS umožňuje vytvářet digitální modely části zemského povrchu
pomocí dostupných softwarových a hardwarových prostředků. Takto vytvořený model
lze pak využít například při evidenci katastru nemovitostí, předpovídání vývoje
počasí, určování záplavových zón řek, výběru vhodné lokace pro čistírnu
odpadních vod, plánování výstavby silnic, krizové řízení apod.

GIS se skládá z

 * Hardwaru
 * Softwaru
 * Dat
 * Pracovnícků (operátorů a uživatelů)
  

Geodata, geoprvky
-----------------

GIS pracuje s prostorovými daty, tzv. *geodaty*. Geodata se skládají z
jednotlivých (geo)prvků. Každý *geoprvek* představuje model fenoménu
reálného světa. Geoprvek je tvořen dvěma základními složkami:

* *geometrickou* (informaci o tvaru, umístění na zemském povrchu)
* *popisnou, atributovou* (nejčastěji popisné vlastnosti každého prvku)

Další složky popisují *topologii*, *dynamiku* prvku.
  
Datový model
------------

Jak již bylo řečeno -- pomocí nástrojů GIS vytváříme modely objektů
(fenoménů) reálného světa. Rozlišuje dvě základní reprezentace dat:

**Rastrový formát**

    Představuje nejčastěji uspořádanou matici hodnot (buňek), které
    označujeme jako pixely. Buňky mohou být 3D, pak hovoříme o
    tzv. voxelech (volume pixel)

**Vektorový formát**
    Prvek je popsán nejčastěji svým obrysem pomocí párů (ve 3D tripletů)
    souřadnic lomových bodů. Nejčastěji si v rámci vektorového modelu vystačíme
    s body nebo liniemi a polygony.

*Spojité* fenomény (nadmořská výška, srážková mapa, teplotní mapa a
pod.) se nejčastěji modelují pomocí rastrové reprezentace dat.

*Diskrétní* fenomény  (katastr, uliční síť, mapa výskytu vorvaňů) se
nejčastěji modeluje pomocí vektorového reprezentace dat.


Proč Open Source
----------------
:wikipedia:`Otevřený software` (open source) je počítačový software, jehož licence
umožňuje

* Studovat zdrojový kód
* Měnit zdrojový kód
* Zdrojový kód dále distribuovat

Open Source není business model, ale *vývojový model*. Způsob práce se software
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
získat zdrojový kód, nelze stavět podnikání na prodeji krabicových verzí. Business
model je častěji stavěn na poskytování podpory, plnění určitých úloh pomocí open source
software. Cena za software není součástí plnění.

OSGeo.org
---------

`Open Source Geospatial Foundation <http://osgeo.org>`_ je ve Spojených státech amerických
registrovaná nezisková organizace, která se stará o podporu open source software projektů
zaměřených na práci s prostorovými daty. Podpora je právní, infrastrukturní i technická.
Většina nejrozšířenějších projektů je registrována jako tzv. *OSGeo Projekt*, což
znamená že prošly inkubační fází, která garantuje určitou kvalitu software,
zrojový kód nezatížený patentovými spory a dostatečně velkou a zdravou komunitu
okolo projektu.

OSGeo.cz
--------

`Spolek Otevřená GeoInfrastruktura <http://osgeo.cz>`_ je český registrovaný
spolek, který se stará o podporu otevřeného software pro GIS a otevřených
prostorových dat v České republice.
