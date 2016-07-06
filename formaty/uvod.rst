Rastrová data
=============

**Rastrová data** (:wikipedia-en:`Raster data`) jsou strukturována nejčastěji do
matice uspořádaných hodnot. Struktura matice je většinou pravidelná
mrížka, teoreticky lze použít i hexagonální tvar. Jednotlivé buňky rastrové mapy
se nazývají *pixely*.

.. figure:: images/The_use_of_a_raster_data_structure_to_summarize_a_point_pattern.png

    Reprezentace frekvence výskytu fenoménu reálného světa jako
    rastrová data (zdroj: :wikipedia-en:`wikipedia <Raster data>`)

Hodnoty jednotlivých rastrových buněk jsou většinou číselné - ať už
celočíselné hodnoty (*integer*) nebo hodnoty s plovoucí desetinnou
čárkou (*float*).

.. figure:: images/rast-num.png

   Příklad rastrové mřížky s celočíselnými hodnotami

.. figure:: images/rast-num-float.png
               
   Příklad rastrové mřížky s hodnotami s plovoucí desetinnou čárkou

Rastrová data jsou vhodná zejména pro reprezentaci *spojitých fenoménů*, jako je

* Teplota vzduchu a vody
* Výška nad mořem
* Geologická data
* Mapa srážek
* Hustota povrchového odtoku
* Letecké a družicové snímkování
* ...

.. figure:: images/slope.png

    Mapa sklonu svahu v České republice

Velikost hrany rastrové buňky určuje tzv. *prostorové rozlišení*
rastrové mapy. Tím je dána polohovou přesnost - celá rastrová buňka
reprezentuje hodnotu, která se nachází v jejím ideálním středu.

.. figure:: images/raster-res.png
   :width: 175px

   Prostorové rozlišení rastrových dat

Atributy rastrových dat
-----------------------

Hodnota rastrové buňky může nést informaci sama o sobě (teplota,
výška, ...) nebo může sloužit jako celočíselný klíč k přidružené
informační tabulce, např.

.. table::
   :class: border
           
   +----------------+---------------------+
   | Hodnota pixelu | Význam              |
   +================+=====================+
   | 1              | lehké půdy          |
   +----------------+---------------------+
   | 2              | středně zrnité půdy |
   +----------------+---------------------+
   | 3              | těžké půdy          |
   +----------------+---------------------+

Další atributy nelze rastrovým datům přiřazovat.

Vektorová data
==============

**Vektorová data** (:wikipedia-en:`Vector graphics`) jsou souborem
geometrických elementů, reprezentující fenomény reálného světa jako
diskrétní prvky. Prvky jsou podle svého charakteru reprezentovány jako
*bod*, *linie* nebo *polygon*.

.. figure:: images/vektor.png
   :class: middle
        
   Vektorové prvky - bod, linie a polygon

.. note:: V anglické literatuře je "vektorový prvek" označován jako *feature*.
    Slovo "feature" je pak tradičně do češtiny překládáno jako "charakteristický
    rys", vlastnost objektu.

    Aby zmatení bylo dokonalé, v českých normách je anglické "feature" ve
    významu vektorového objektu v GIS překládáno jako "vzhled jevu".

    Závěr: narazíte-li v anglické literatuře na slovo *feature* nebo v čekých
    normách na *vzhled jevu*, vždy se jedná o "vektorový objekt v GIS s
    geometrií a atributy".

Vektorová data jsou vhodná všude tam, kde se jedná o *diskrétní*
objekty, jako ideální reprezentace nějakého fenoménu:

* Výskyt jedince sledovaného druhu (bod)
* Významný orientační prvek (bod)
* Středová linie silnice, silniční síť (linie)
* Průběh elektrického vedení (linie)
* Říční síť, dráhy povrchového odtoku (linie)
* Hranice parcel katastru nemovitostí (polygon)
* Hranice vodních ploch (polygon)
* Hranice půdního krytu (polygon)
* ...

.. figure:: images/vector-model-sfa.png
   :width: 350px
        
   Ukázka vektorových dat *bod*, *linie* a *polygony*.

Vektorová data jsou většinou uložena ve formě uspořádaných dvojic souřadnic X,Y.
Linie a plocha je zapsána pomocí množiny těchto uspořádaných dvojic definující 
jejich lomové body. Přesnost
takto zadaných souřadnic tak může být teoreticky nekonečná (co umožní počítačové
systémy).

Zvláštním případem jsou tzv. *multiprvky* (multipoints, multilinies,
multipolygons) - vektorové objekty skládající se z více vzájemně
nepropojených geometrických objektů (např. dálnice D8 je v úseku přes
České středohoří přerušena - lze ji tak reprezentovat jako objekt
*multiline* sestávající se ze dvou liniových geometrických elementů).

Atributy vektorových dat
------------------------

Kromě informace o *geometrických vlastnostech* prvků nesou vektorová data
také popisnou informaci uloženou v *atributech*. Atributy
jsou většinou zaznamenány do formy databázové tabulky. V závislosti na
použitém software se jedná buď o souborý formát (např. DBF u formátu Esri Shapefile) nebo plnohodnotný
databázový server (např. PostgreSQL).

.. figure:: images/vector-attributes.png
    :class: middle

    Mapa velkoplošných chráněných území spolu s atributy uloženými v
    databázi (zdroj: `AOPK OGC WFS Server
    <https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer>`_)

Geometrická a atributová složka bývají obvykle uloženy zvlášť a navzájem
propojeny pomocí jednoznačného interního identifikátoru (tzv. *feature id*).

Počet atributů vektorových prvků je teoreticky nekonečný. Pokud použijeme pro
uložení atributů databázový systém, je možné s daty dále pracovat jako

.. todo:: jako co?

.. note:: Některé softwary (např. databázový systém PostGIS nebo
    souborová databáze SpatialLite) ukládají geometrickou složku dat jako *jeden z atributů*
    vektorového prvku. Data jsou uspořádána do klasické databázové tabulky,
    geometrie je pouze další atribut - geometrie tak není od atributů nijak
    oddělena.

    Příklad: Výpis parcel s jejich identifikátorem, parcelním číslem a
    geometrií z databáze PostGIS:
    
    ::
          
          +------------+------------------------------------------------------+--------+
          |    fid     |                       geometry                       |  cislo |
          +============+======================================================+========+
          |45496175010 | POLYGON((-728524.789710812 -1066515.49883718,-728... | 515    |
          +------------+------------------------------------------------------+--------+
          |2982799209  | POLYGON((-723694.909701298 -1063302.12883134,-723... | 1331/10|
          +------------+------------------------------------------------------+--------+
          |2969999209  | POLYGON((-718640.439694238 -1037240.20878015,-718... | 1276   |
          +------------+------------------------------------------------------+--------+
          |17076174010 | POLYGON((-722180.859702737 -1027388.94876021,-722... | 260    |
          +------------+------------------------------------------------------+--------+
          |3825204209  | POLYGON((-715023.709686742 -1038171.52878245,-715... | 483    |
          +------------+------------------------------------------------------+--------+
          |3010454209  | POLYGON((-718516.42969393 -1037654.72878097,-7185... | 4169   |
          +------------+------------------------------------------------------+--------+
          |3756714209  | POLYGON((-716647.359686897 -1063110.74883183,-716... | 353/11 |
          +------------+------------------------------------------------------+--------+
          |3789127209  | POLYGON((-728971.089716029 -1031879.47876821,-729... | 496/124|
          +------------+------------------------------------------------------+--------+
          |3060136209  | POLYGON((-733967.459726413 -1030652.32876515,-733... | 322/2  |
          +------------+------------------------------------------------------+--------+
          |3142451209  | POLYGON((-735750.959725715 -1066084.18883546,-735... | 205    |
          +------------+------------------------------------------------------+--------+

Vektorová topologie
===================

:wikipedia:`Topologie` je vlastnost geometrií vektorových dat, pomocí které lze
určit vztahy mezi jednotlivými prvky. Pomocí topologie lze popsat charakteristiky dvou
vektorových prvků jako

* Prvek *leží v* jiném prvku
* Prvek *se kříží s* s jiným prvku
* Prvek *je nalevo/napravo od* prvku
* Prvek *je shodný* s prvkem

Různé softwary a jejich formáty přistupují k topologii různě, dnes ale
převládá takový přístup, že data jsou uložena v *netopologickém*
formátu (jako tzv. jednoduché prvky - *simple features*) a topologické
charakteristiky jsou počítány na vyžádání.

.. note:: `GRASS GIS <http://grass.osgeo.org>`_ naopak data vždy
          ukládá v topologickém formátu.

          
.. figure:: images/area-1-2.png

   Ukázka topologického datové modelu
   
Nejsou-li data tzv. *topologicky čistá*, obsahují různě závažné *chyby
topologie*. Např. společná hranice dvou parcel není stejná, ale každá parcela má
lehce posunuté hraniční lomové body a tudíž dochází v některých místech k
nedotažení společné hranice, na jiných místech zase obě parcely do sebe
zasahují.

Dalšími chybami jsou nedotažení lomových bodů nebo naopak jejich přetažení.

.. figure:: images/overshoot.png
   :width: 400px
        
.. figure:: images/v_clean_rmsa.png
   :class: small

.. todo:: Dopnit zdroj
                     
Většina pokročilích GIS obsahují nástroje pro *čištění topologie*.

Převod dat
==========

.. _rasterizace:
   
Rasterizace
-----------

Jak bylo napsáno výše, rastrovým pixelům můžeme přiřadit vždy pouze jeden
atribut. Tímto atributem může být buď některý z číselných atributů (nebo číselná
reprezentace textového atributu) vektorových objektů či nějaká geometrická
veličina (plocha, délka, ...).

V závislosti na prostorovém rozlišení se ztrácí přesnost vektorových dat a je
nahrazena rozlišením rastrových dat. Data od určitého zvětšení vypadají
"rozkostičkovaně".

.. figure:: images/vect2rast-1.png

   Příklad rasterizace (příprava)

.. figure:: images/vect2rast-2.png

   Příklad rasterizace (výsledek)

Vektorizace
-----------

Protože buňky rastrové mapy obsahují pouze jednu číselnou hodnotu (případně
je tato hodnota asociována s textovou informací), obsahuje u vektrových prvků 
výsledná tabulka atributů pouze jeden sloupeček.

V závislosti na zvoleném výstupním formátu dat - zda se jedná o data
bodová, liniová nebo polygonová - se softwary pokouší ideální
aproximovat a vyhlazovat kostrbatý tvar prvků, který by nutně vzniknul
při převodu rastrový buněk na liniové objekty.
