Úvod
====

Úvodní kapitola nastiňuje motivaci, proč pracovat s nástroji open source GIS, 
poskytuje přehled zdrojů, odkazy na komunitní skupiny mezinárodní i národní.

.. _proc-gis:

Co je GIS?
----------

.. index:: GIS

:wikipedia:`Geografický informační systém` (GIS) je na počítačích
založený informační systém pro získávání, ukládání, analýzu a
vizualizaci dat, která mají prostorový vztah k povrchu Země. V této
souvislosti mluvíme o geografických datech, zkráceně *geodatech*,
angl. *geospatial data*, *geospatial information*.

Počátek geoinformačních technologií a souvisejícího vědního oboru
geoinformatiky sahá do 60. let 20. století. Tehdy se přišlo na to, že
úkoly jako například plánování regionálního rozvoje území jsou jako
stvořené pro geografické informační technologie.

Prostorově orientovaný geografický informační systém shromažďuje a
zpracovává data, poskytuje informace a poznatky vázané k místu vzniku
jevu a jeho použití. Vyvinul se z map středních a malých
měřítek. Obecně klade nižší požadavky na podrobnost a polohovou
přesnost, naproti tomu je většinou důležitá aktuálnost dat.

Možno říci, že GIS se skládá z:

 * hardwaru,
 * softwaru,
 * dat,
 * pracovníků (operátorů a uživatelů).

.. index:: Složky GIS
              
.. _gis-slozeni:
      
.. figure:: ./images/gis-slozeni.svg
   :class: middle
    
   Hlavní složky GIS.

GIS využívá data z různých zdrojů jako digitální fotogrammetrie,
dálkový průzkum Země (DPZ), geodézie a dalších. Pomocí dostupných
softwarových a hardwarových prostředků umožňuje vytvářet digitální
modely části zemského povrchu, geografické průzkumy, analýzy a
statistiky. Takto vytvořený model lze pak využít například při
evidenci katastru nemovitostí, předpovídání vývoje počasí, určování
záplavových zón řek, výběru vhodné lokace pro čistírnu odpadních vod,
plánování výstavby silnic, krizové řízení a podobně.

.. index:: geodata, geoprvky

.. _geodata-geoprvky:

Geodata, geoprvky
^^^^^^^^^^^^^^^^^

Jak bylo již zmíněno, GIS pracuje s prostorovými (geografickými) daty,
tzv. *geodaty*.  Ty se skládají z jednotlivých (geo)prvků. Každý
*geoprvek* představuje model fenoménu reálného světa. Od jiných
objektů jej lze rozlišit na základě prostorové polohy, tematických
charakteristik, polohových vztahů k jiným geoprvkům a časových změn.

Geoprvek je teda tvořen dvěma základními složkami:

* *geometrickou* (informaci o tvaru, umístění na zemském povrchu),
* *popisnou* (nejčastěji popisné vlastnosti každého prvku, tzv. *atributy*).

Další složky popisují tzv. *topologii* (prostorový vztah k jiným
geoprvkům), případně *dynamiku* (časové změny geoprvku).  Reprezentace
reálného světa v GIS se od reality liší, jelikož tato interpretace
vždy zahrnuje určitou míru abstrakce, která je pro zpracování v GIS
nezbytná.

.. _mira-abstrakce:
      
.. figure:: ./images/mira-abstrakce.png
   :class: middle
    
   Digitální reprezentace reálného světa (zdroj: `GIS v regionálním
   rozvoji
   <https://is.mendelu.cz/eknihovna/opory/index.pl?opora=5784>`_).

.. index::
   pair: prostorová dimenze; dimenze prostorová
              
Důležitá je prostorová *dimenze geoprvků*, která charakterizuje jeho
rozšíření v různých směrech prostoru. V GIS se můžeme setkat s
následujícími pojmy:

.. table::
   :class: border
        
   +-----------------------------------------------------+
   |         Prostorová dimenze geoprvků                 |
   +===========+=======+===========+=========+===========+
   | **Modely**| **0D**|**1D**     |**2D**   |  **3D**   |
   +-----------+-------+-----------+---------+-----------+
   |geometrický|  bod  | polylinie | polygon |  těleso   |
   +-----------+-------+-----------+---------+-----------+
   |topologický| uzel  | hrana     | plocha  | polyhedron|
   +-----------+-------+-----------+---------+-----------+
   |dynamický  | čas                                     |
   +-----------+-------+-----------+---------+-----------+
  
Bezrozměrné objekty (0D) svou definovány svojí polohu, nedisponují
délkou nebo plochou. Jednorozměné objekty (1D) mají konečnou délku,
ale ne plochu, dvojrozměné objekty (2D) mají konečnou plochu.

.. index:: reprezentace geodat

.. index::
   pair: rastrová data; geodata

.. index::
   pair: vektorová data; geodata

Reprezentace dat
^^^^^^^^^^^^^^^^

Jak již bylo řečeno, pomocí nástrojů GIS vytváříme modely objektů
(fenoménů) reálného světa. Je důležité správně určit datovou strukturu
(reprezentaci dat) a navrhnout vhodnou kartografickou reprezentaci při
jejich vizualizaci. Rozlišuje se dvě základní reprezentace dat:

**a) vektorová reprezentace**
    prvek je popsán nejčastěji svým obrysem
    pomocí párů (ve 3D tripletů) souřadnic lomových bodů; nejčastěji
    si v rámci vektorového modelu vystačíme s body nebo liniemi a
    polygony

**b) rastrová reprezentace**
    představuje nejčastěji uspořádanou matici
    hodnot (buňek), které označujeme jako pixely; buňky mohou být 3D,
    pak hovoříme o tzv. *voxelech* (*volume pixel*)

.. _datovy-model:
      
.. figure:: ./images/datovy-model.png
   :class: middle
    
   Vektorová a rastrová reprezentace objektů (podle Voženílek, 1998).

*Diskrétní fenomény* jako například katastr, uliční síť nebo mapa výskytu vorvaňů, 
se nejčastěji modeluje pomocí vektorového reprezentace dat. *Spojité fenomény* 
jako například nadmořská výška, srážková mapa, teplotní mapa a podobně, se nejčastěji 
modelují pomocí rastrové reprezentace dat. Obě reprezentace jsou blíže popsány 
v částech :doc:`vektorová <formaty/vektor>` a :doc:`rastrová <formaty/rastr>` data.

.. index:: open source
   pair: open source; otevřený software
   pair: free software; svobodný software

Co je open source?
------------------

:wikipedia:`Otevřený software` (open source) je počítačový software,
jehož licence podle definice `FSF
<https://www.gnu.org/philosophy/free-sw.en.html>`_ (Free Software
Foundation, resp. Nadace svobodného software) umožňuje:

* **freedom 0**: spouštět program jakýmkoli způsobem pro jakýkoliv účel,
* **freedom 1**: modifikovat program, aby co nejlépe vyhovoval uživateli (pomoci sami sobě),
* **freedom 2**: distribuovat kopie programu (pomoci přátelům, kolegům),
* **freedom 3**: publikovat dokonalejší verzi i pro ostatní (pomoci vybudovat komunitu).

Open source není business model, ale *vývojový model*. Způsob práce se
software předurčuje k tomu jakým způsobem probíhá komunikace mezi
vývojáři a mezi uživateli a vývojáři.

.. tip:: Blog GISMentors: `Otázka: Vieš čo je open source GIS?
         <http://www.gismentors.cz/blog/otazka-vies-co-je-open-source-gis/>`__.
         
.. index:: komunita, mailing list, IRC

Komunita
^^^^^^^^

U dobrých open source projektů existuje silná a zdravá komunita
vývojářů a uživatelů. Rozhodovací procesy jsou otevřené a
dokumentovatelé. Komunita je často prvním místem podpory, kterou může
uživatel nebo začínající vývojář dostat. Často se řeší problémy a
otázky, které by jinak zůstaly skryty.  Organizují se konference,
:wikipedia:`code sprinty <Sprint (software development)>`, project
steering setkání. Problémy se řeší veřejně na :wikipedia:`mailing
listech <Elektronická konference>`, :wikipedia:`IRC` a podobně.

Další výhodou open source projektů je, že v případě jakýchkoliv
problémů je odezva poměrně rychlá - hodně očí hodně najde.  Malé týmy
pracují na menších projektech a hledají propojení většinou postavené
na standardech (více v kapitole :doc:`standardy/index`). Tato spojení
se děje spíše náhodně než plánovaně. V proprietárním GIS jsou
jednotlivé komponety často více propojené. Což může být problém ve
chvíli, kdy se při návrhu systému na něco zapomene. Potom je obtížnější
daný systém o novou komponentu rozšířit.

.. index:: financování

Způsob financování
^^^^^^^^^^^^^^^^^^

Nic není zadarmo, ani práce vývojářů otevřeného software. Protože
každý může získat zdrojový kód, nelze stavět podnikání na prodeji
krabicových verzí. Business model je častěji stavěn na poskytování
podpory, služeb, plnění určitých úloh pomocí open source
software. Cena za software není součástí plnění.

.. index:: OSGeo
           
OSGeo.org
^^^^^^^^^

`Open Source Geospatial Foundation <http://osgeo.org>`_ je ve
Spojených státech amerických registrovaná nezisková organizace, která
se stará o podporu open source software projektů zaměřených na práci s
geografickými daty. Podpora je právní, infrastrukturní i technická.
Většina nejrozšířenějších open source GIS projektů je registrována
jako tzv. *OSGeo Projekt*, což znamená, že prošly inkubační fází, která
garantuje určitou kvalitu software, zrojový kód nezatížený patentovými
spory a dostatečně velkou a zdravou komunitu okolo projektu.

.. _osgeo-logo:
      
.. figure:: ./images/osgeo-logo.png
   :width: 250px
    
   Logo Open Source Geospatial Foundation.

.. tip:: Další informace o OSGeo v kapitole :ref:`OSGeo - standardy
         <osgeo-standardy>`.

.. index:: OSGeo.cz
                    
OSGeo.cz
^^^^^^^^

Občanské sdružení `Otevřená GeoInfrastruktura <http://osgeo.cz>`_ je v
ČR registrované občanské sdružení, které se stará o podporu otevřeného
software pro GIS a otevřených prostorových dat v České
republice. Základními cíli sdružení jsou zejména:

* propagovat používání a vývoj nástrojů FOSS (Free and Open Source
  Software) pro geomatiku, geoinformatiku, geodézii a kartografii,
* podporovat tvorbu, sdílení a publikování volně dostupných a
  otevřených dat a informací, zejména geodat, v souladu s obecně
  uznávanými standardy,
* vyhledávat, aktivizovat a podporovat v České republice síly k
  naplňování těchto cílů.

.. _osgeo-cz-logo:
      
.. figure:: ./images/osgeo-cz-logo.png
   :width: 300px
    
   Logo občanského sdružení Otevřená GeoInfrastruktura České
   republiky.
