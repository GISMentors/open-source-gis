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

    Obdobně můžeme *worldfile* použít pro formáty JPG (`.jgw`) a někdy PNG (`.pgw`).

Float ....

overviews 

metadata

color

compression

.. todo:: doplnit
