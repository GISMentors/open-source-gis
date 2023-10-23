.. index:: SKKNNASADENIE

.. _nasadenieskkn:

Nasadenie nástroja
------------------

Viď. `Nasadenie <https://github.com/lfurtkevicova/kn-stuff/wiki/Nasadenie>`_ (*https://github.com/lfurtkevicova/kn-stuff/wiki/Nasadenie*)

.. note:: Predpoklad `QGIS <http://training.gismentors.eu/qgis-zacatecnik/instalace/index.html>`_
        (*http://training.gismentors.eu/qgis-zacatecnik/instalace/index.html*), existujúca 
        `databáza <https://github.com/lfurtkevicova/kn-stuff/wiki/Databaza>`_ (*https://github.com/lfurtkevicova/kn-stuff/wiki/Databaza*) 
	a `Vstupné dáta <https://github.com/lfurtkevicova/kn-stuff/wiki/Vstupne-data>`_ (*https://github.com/lfurtkevicova/kn-stuff/wiki/Vstupne-data*) 
	vo formáte `*.vgi` a `*.dbf`.

``sudo -u postgres psql postgres; sudo -u postgres createdb kataster; sudo -u postgres createuser ludka; psql kataster``

V ďalšom kroku nasleduje vytvorenie geodatabázy z databázy *kataster*, rozšírenie pre topologické vektorové dáta, upgrade na vyššiu verziu PostGIS, pridanie vlastného súradnicového systému do tabuľky `spatial_ref_sys`, napr. *5514*, viď. `tu <https://github.com/lfurtkevicova/kn-stuff/wiki/Databaza>`_.


