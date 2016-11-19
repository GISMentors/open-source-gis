.. _epsg-standardy:

=====
EPSG 
=====

.. index::
   pair: datasety; epsg
           
Dataset `EPSG <http://epsg.org>`__ (Geodetic Parameter Dataset) byl
spravován původně konsorciem `International Association of Oil and Gas
Producers <http://www.iogp.org/>`_. Jedná se o široce akceptovaný
dataset šířený v databázích *MS Access*, *MySQL*, *PostgreSQL* a
dalších.  Je ale přítomen a především aktualizován ve všech softwarech
v oboru GIS.

.. index::
   pair: knihovny; proj4
      
V kapitole :doc:`../sour-systemy/index` se tímto datasetem zabýváme
podrobněji, viz. :ref:`EPSG <ss-epsg>`. Proto zde pouze zopakujeme, že
databáze EPSG obsahuje číselné kódy reprezentující jednotlivé definice
souřadnicových systémů používaných v oboru geodézie a GIS a že velice
praktické rozhraní k této databázi lze nalézt na stránkách
http://epsg.io.  Různé softwary zapisují definice souřadnicových
systému různě. Nejpoužívanější formou zápisu je formát knihovny `Proj4
<http://proj4.org>`_ a tzv. **Well Known Text** (:wikipedia-en:`WKT
<Well-known text>`).
