.. _gpkg:

OGC GeoPackage
--------------

`GPKG <http://geopackage.org>`_  je relativně nový formát OGC, postavený na
souborové databázi a knihovně `SQLite <http://sqlite.org>`_.  Umožňuje uložit
jak rastrová, tak vektorová data a umožňuje obojí uložit v tzv. "dlaždicované"
struktuře.

GeoPackage umožňuje k datům přistupovat jako k SQL databázi (vytvářet pohledy,
číselníky, ...). Netrpí nešvary formátu Shapefile, jako je omezení na
jednoduché datové typy, nchybějící podpora pro `BIGInt`, maximální velikost
textového atributu na 256 znaků, maximálně 10 znaků na název atributu
(sloupečku) nebo maximální velikost 2GB pro data.

Výchozím formátem pro ukládání vektorových dat v prostředí QGIS je OGC
GeoPackage.
