================
Rastrové formáty
================
Mezi nejčastěji používané rastrové formáty v GIS patří 

* :wikipedia-en:`GeoTIFF`
* :wikipedia-en:`JPEG`

Zejména v prostředí webových prohlížečů se pak ještě sektáváme s formáty :wikipedia-en:`PNG <Portable Network Graphics>` a
:wikipedia-en:`GIF`. Ty však nejsou pro geografická data příliš vhodné.

Programátorská knihovna pro práci s rastrovými daty `GDAL <http://gdal.org>`_
obsahuje v tuto chvíli podporu pro `140 rastrových formátů
<http://gdal.org/formats_list.html>`_.

.. tip:: Více informace na školení :skoleni:`GeoPython <geopython>`.

Formát GeoTIFF
--------------

:wikipedia-en:`GeoTIFF` je tvořen v základu standardním formátem :wikipedia-en:`TIFF`, ke kterému
jsou přidána metadata určující jeho polohu a souřadnicový systém. 

.. note:: Alternativou k formátu GeoTIFF je použití standardního formátu TIFF a
    tzv. :wikipedia-en:`World file` - externího souboru, obsahujícím 6 řádků textu:

    * velikost pixelu ve směru osy X
    * rotace okolo osy Y
    * rotace okolo osy X
    * velikost pixelu ve směru osy Y
    * souřadnice X středu levého-horního pixelu
    * souřadnice Y středu levého-horního pixelu

    Pokud se soubor *worldfile* jmenuje stejně jako soubor TIFF a má koncovku
    `tfw`, tak jej většina GIS automaticky použijí. Příklad: `dmt.tif, dmt.tfw`.

    Obdobně můžeme *worldfile* použít pro formáty JPG (`.jgw`) a někdy PNG

Některé speciality formátu GeoTIFF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Číselné formáty
    Formát GeoTIFF umožňuje uložit data v celočíselné podobě nebo jako čísla s
    plovoucí desetinnou čárkou.

Interní maska a hodnota NODATA
    Do souboru GeoTIFF lze uložit interní masku hodnot, označující místa, která
    "nemají být vidět".
    
    GeoTIFF umožňuje nastavit zapsat hodnotu "žádná data" - na tomto místě je
    mapa prázdná.

Přehledové mapy
    GeoTIFF umožňuje vytvářet vnitřní přehledové mapky

Barvy a kanály
    Většina prohlížečů se snaží interpretovat data v GDAL jako tři barevné
    kanály. GeoTIFF umožňuje zapsat více kanálová data (ne pouze 3), s čímž se
    prohlížečky obrázků smiřují jen těžko. Obsahuje-li soubor GeoTIFF 3 pásma s
    hodnotami 0-255, je výsledek většinou očekávatelný.

Vnitřní komprese
    Data ve formátu GeoTIFF mohou být vnitřně komprimována některou z metod či
    knihoven. Kromě běžného ZIP lze použít např. i kompresi JPEG. Výsledný rastrový
    soubor je pak fyzicky menší, než pokoušeli-li bychom se soubor bez vnitřní
    komprese zkomprimovat externím algoritmem. Více na toto téma píše např.
    `Paul Ramsey ve svém blogu
    <http://blog.cleverelephant.ca/2015/02/geotiff-compression-for-dummies.html>`_.
