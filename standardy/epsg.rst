=================================
EPSG - Geodetic Parameter Dataset
=================================

Dataset `EPSG <http://epsg.org>`_ byl spravován původně konsorciem `International
Association of Oil and Gas Producers <http://www.iogp.org/>`_. Jedná se o široce
akceptovaný dataset šířený v databázích MS Access, MySQL, PostgreSQL a dalších.
Je ale přítomen a především aktualizován ve všech softwarech v oboru GIS.

V části :ref:`souřadnicové systému <sour-systemy>` se tímto datasetem zabýváme podrobněji. Proto zde
pouze zopakujeme, že databáze EPSG obsahuje číselné kódy reprezentující
jednotlivé definice souřadnicových systémů používaných v oboru geodézie a GIS.

Velice praktické rozhraní k této databázi lze nalézt na stránkách http://epsg.io.

Zásadní kódy EPSG z pohledu českého uživatele
---------------------------------------------

:epsg:`5514`
    S-JTSK používané v GIS (souřadnice `x` a `y` nesou záporné hodnoty - data se
    nelézají ve třetím kartézkém kvadrantu).
:epsg:`4326`
    Souřadnicový systém WGS84 používaný např. v zařízeních GPS.
:epsg:`3857`
    Systém využívající Mercatorovo zobrazení, populární v různých mapových
    službách (Google Maps, OpenStreetMap, Bing, nově i Mapy.cz).
:epsg:`3035`
    Evropský terestrický referenční systém, používaný v Evropské unii,
    odvozený od vesmírních konstant, zajišťující neměnnost evropského kontinentu
    vlivem kontinentálního driftu.

Různé softwary zapisují definice souřadnicových systému různě. Nejpoužívanější formou
zápisu je formát knihovny `Proj4 <http://proj4.org>`_ a tzv. **Well Known Text**
(WKT).
