.. index:: proj4
           
Knihovna Proj.4 pro transformaci souřadnic
------------------------------------------

`Proj.4 <https://trac.osgeo.org/proj/>`_ (Cartographic Projection
Library) je jedna ze základních knihoven využívaných v mnoha open
source GIS projektech jako `GRASS GIS
<http://www.gismentors.cz/skoleni/grass-gis/>`_, `QGIS
<http://www.gismentors.cz/skoleni/qgis/>`_, `PostGIS
<http://www.gismentors.cz/skoleni/PostGIS/>`_ a dalších. Má své klony
v jazyce `JavaScript <http://proj4js.org/>`_, `PHP
<https://sourceforge.net/projects/proj4php/>`_
(https://github.com/jachym/proj4php), `Python
<https://github.com/jswhit/pyproj>`_ a dalších. Kromě možnosti
používat tuto knihovnu z různých programů, existují i užitečné
nástroje v příkazové řádce:

* :ref:`cs2cs <cs2cs>`, 
* :ref:`geod a invgeod <geod-a-invgeod>`, 
* :ref:`proj a invproj <proj-a-invproj>`.

.. index:: cs2cs
             
.. _cs2cs:

**cs2cs**

Provádí transformaci souřadnic mezi jednotlivými souřadnicovými systémy.

.. notecmd:: Použití 

    - převod souřadnice ze souřadnicového systému S-JTSK (kód
      :epsg:`5514` do WGS84 (:epsg:`4326`):
              
    .. code-block:: bash

        echo "-868208.53 -1095793.57 512.30" | cs2cs +init=epsg:5514 \
            +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56 +to +init=epsg:4326

        12d48'25.16"E	49d27'8.146"N 559.261

    - místo EPSG kódu můžeme použít kompletní definici souřadnicového
      systému; ukázka pro převod souřadnic z WGS84 na S-JTSK (z důvodu
      přesnějšího převodu používáme tzv. transformační parametry
      ``+towgs84``):

    .. code-block:: bash

        echo "12d48'25.15992 49d27'8.14571 559.417" | cs2cs +proj=longlat \
            +datum=WGS84 +to +proj=krovak +lat_0=49.5 +lon_0=24.83333333333333 \
            +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0 +ellps=bessel \
            +pm=greenwich +units=m +no_defs \
            +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56

        -868208.54	-1095793.58 512.46

.. index:: geod
   pair: geod; invgeod

.. _geod-a-invgeod:

**geod a invgeod**

Řeší tzv. základní `geodetické úlohy
<http://gis.zcu.cz/studium/gen1/html/ch07s02.html>`__ pro určení
zeměpisní šířky a délky, při zadání výchozího bodu, azimutu, délky a
naopak.

.. notecmd:: Použití 

    - výpočet azimutu a vzdálenosti mezi Prahou a Brnem:

    .. code-block:: bash

        geod +ellps=bessel <<EOF -I +units=m
        15d20'55.444"E47d43'10.405"N 14d28'7.821"E50d4'2.641"N
        EOF

        110d53'32.868"	-68d30'12.184"	270855.602

.. index:: proj
   pair: proj; invproj

.. _proj-a-invproj:

**proj a invproj**

Provádí transformaci souřadnicových systému z/do systému
:doc:`../soursystemy/wgs84`. Funguje podobně jako :ref:`cs2cs <cs2cs>`,
který ale umí transformovat mezi libovolnými souřadnicovými systémy.
