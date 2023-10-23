.. index:: EPSG
   pair: EPSG; European Petroleum Survey Group

EPSG
====

:wikipedia:`European Petroleum Survey Group` byla od roku 1986 do roku
2005 vědecká organizace s vazbou k evropskému naftovému průmyslu. Od
roku 2005 se pod `EPSG <http://www.epsg.org/>`_ rozumí dataset
spravovaný nástupnickou organizací `IOGP <http://www.iogp.org/>`_ (The
International Association of Oil & Gas producers).

Jde o databázi zemských elipsoidů, geodetických dat, zeměpisných a
kartografických souřadnicových systémů, měrných jednotek a podobně.
Každé kartografické zobrazení, resp. souřadnicový systém má dán
jedinečný kód.  Tento kód je celé nezáporné číslo vyjma nuly, které se
v databázi nesmí opakovat. Například :epsg:`4326` vyjadřuje
souřadnicový systém :doc:`wgs84` o souřadnicích zeměpisné šířky a
délky v celých stupních s Greenwichem jako nultým poledníkem.
Databáze je podporována a rozšířena ve všech programech pracujících s
geografickými daty. Oficiální stránka této databáze je `www.epsg.org
<http://epsg.org>`_, transformaci mezi různými souřadnicovými systémy
lze zkoušet na `www.epsg-registry.org
<http://www.epsg-registry.org>`_.

.. tip:: Nejnovější přehled včetně exportu do různých formátů naleznete na
         stránce http://epsg.io

.. figure:: ./images/epsg_page.png
    :class: middle

    Hlavní stránka `epsg.io <https://epsg.io/>`_.


Významné kódy EPSG
------------------

:epsg:`3857`

    sférické :doc:`mercatorovo-zobrazeni`, používaný například
    :wikipedia:`Google`, :wikipedia:`Bing`, :wikipedia:`OpenStreetMap`

:epsg:`4326`
                     
   :doc:`wgs84`, souřadnicový systém používaný mimo jiné v
   zařízeních GPS, zeměpisné souřadnice

:epsg:`5513`
         
   systém :doc:`sjtsk`, jih :math:`x` / západ :math:`y` (*S-JTSK /
   Krovak*), definováno od nultého poledníku Greenwich, kladné
   souřadnice

:epsg:`5514`
         
   systém :doc:`sjtsk`, východ :math:`x` / sever :math:`y` (*S-JTSK /
   Krovak East North*), definováno od nultého poledníku Greenwich,
   záporné souřadnice

Kódy, se kterými se také můžete setkat
--------------------------------------

Tyto kódy jsou zastarelé a neměli by se používat.

:epsg:`2065`

    systém :doc:`sjtsk`, jih :math:`x` / západ :math:`y` (S-JTSK /
    Krovak), definováno od Ferrova poledníku, kladné souřadnice; někdy
    se chybně využívá jako ekvivalent :epsg:`5514` (S-JTSK / Krovak
    East North); tyto systémy však nejsou ekvivaletní a tento kód by
    se takto používat neměl

:epsg:`5221`

    systém :doc:`sjtsk`, východ :math:`x` / sever :math:`y` (S-JTSK
    / Krovak East North), definováno od Ferrova poledníku, záporné
    souřadnice

:epsg:`102067`

    systém :doc:`sjtsk`, východ :math:`x` / sever :math:`y`
    (S-JTSK / Krovak East North), kód využívaný v softwarech firmy
    ESRI, často přejímaný do jiných softwarů; provizorní náhrada,
    dokud kód :epsg:`5514` nebyl oficiálně přidán do databáze EPSG;
    dnes je již zastaralý a není nutné jej využívat

:epsg:`900913`

    alternativní zápis Mercatorova zobrazení využívané v Google Maps;
    číslo :math:`900913` představuje grafickou podobu slova *google*;
    dnes již není nutné, lepší je využívat oficiální kód :epsg:`3857`

.. important:: V oblasti užití dat v geografických informačních
    systémech není užíván EPSG :epsg:`2065` S-JTSK/Krovak s kladnými
    souřadnicemi v pořadí jih :math:`x`, západ :math:`y`, který naopak
    užívají geodeti pro měření v terénu a zobrazují pak ve svých
    měřických výstupech kladné souřadnice :math:`x`, :math:`y`. Pokud
    je tento výstup použit přímo jako zdroj pro GIS aplikaci či
    mapovou službu, data se nezobrazí správně, neboť aplikace jsou
    naprogramovány na užití Křovákova zobrazení se **zápornými**
    souřadnicemi.  Vztah mezi souřadnicemi „záporného“ :math:`x`,
    :math:`y` a „kladného“ :math:`x`, :math:`y` Křováka, tedy mezi
    :epsg:`5514` a :epsg:`5513`, je **x = -y a y = -x**.

.. _srovnani-epsg:

.. figure:: ./images/srovnani_epsg.png
    :class: middle
    
    Srovnání některých EPSG kódů - Mercator, WGS84, S-JTSK Krovak a
    S-JTSK Krovak East North (zdroj: `epsg.io`_).
