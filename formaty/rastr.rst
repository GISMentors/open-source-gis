Rastrové formáty
================
Mezi nejčastěji používané rastrové formáty v GIS patří 

* GeoTIFF
* JPEG

Zejména v prostředí webových prohlížečů se pak ještě sektáváme s formáty PNG a
GIF. Ty však nejsou pro prostorová data příliš vhodné.

Programátorská knihovna pro práci s rastrovými daty `GDAL <http://gdal.org>`_
obsahuje v tuto chvíli podporu pro `140 rastrových formátů
<http://gdal.org/formats_list.html>`_.

Formát GeoTIFF
--------------
:wikipediaen:`GeoTIFF` je tvořen v základu standardním formátem TIFF, ke kterému
jsou přidána metadata určující jeho polohu a souřadnicový systém. 

.. note:: Alternativou k formátu GeoTIFF je použití standardního formátu TIFF a
    tzv. :wikipediaen:`World file` - externího souboru, obsahujícím 6 řádků textu:

    * velikost pixelu ve směru osy X
    * rotace okolo osy Y
    * rotace okolo osy X
    * velikost pixelu ve směru osy Y
    * souřadnice X středu levéhé-horního pixelu
    * souřadnice Y středu levéhé-horního pixelu

    Pokud se sobour worldfile jmenuje stejně jako soubor TIFF a má koncovku
    `tfw`, tak jej systémy naleznou. Příklad: `dmt.tiff, dmt.tfw`

    Obdobně můžeme worldfile použít pro formáty JPG (.jgw) a někdy PNG (.pgw).

Float ....

overviews 

metadata

color

compression


