.. _ogc:

===
OGC
===

.. index:: OGC, Open Geospatial Consorcium
           
**Open Geospatial Consortium** (`OGC <http://opengeospatial.org>`__) je mezinárodní 
standardizační organizace pro
oblast prostorových dat a služeb, která funguje na relativně otevřené bázi
(poplatky za členství nejsou nijak přemrštěné). Standardy jsou vyvíjeny v rámci
relativně otevřeného procesu. Po svém schválení jsou bez omezení
dostupné všem a jsou v praxi vždy implementovány.

Jednotlivé pracovní skupiny pracují na problémech, které identifikovaly jako
potřebné. OGC standardizuje oblast *datových formátů*, ale především *webových
služeb*. 

.. note:: :wikipedia:`Webová služba` je služba popsaná formátem
    :wikipedia:`WSDL` (*Web Services Description Language*), se kterou
    lze automaticky interagovat pomocí vlastního software. *Webová
    služba OGC* je naproti tomu na XML založený komunikační protokol,
    který ovšem nemá s výše zmíněnou "obecně programátorskou
    technologií" mnoho společného.

Některé standardy byly akceptovány i organizací :doc:`ISO
<../iso>`. Seznam standardů OGC lze nalézt na stránce
http://opengeospatial.org/standards.

.. _ogc-ows:

.. index::
   pair: OGC OWS; OGC Open Web Services

OGC OWS
-------

**OGC Open Web Services** (OGC OWS) je soubor standardů komunikační
protokolů postavených na značkovacím jazyku :wikipedia:`XML`
popisujících komunikaci mezi serverem a klientem.  Server nabízí
prostřednictvím služeb data, vykreslené mapové dlaždice či výpočetní služby, na které
klient může dosáhnout. Vlastnosti společné všem službám lze nalézt ve
specifikaci `Web Service Common
<http://www.opengeospatial.org/standards/common>`_.  Ta popisuje
zejména XML kódování metadat dalších webových služeb a některé
společné charakteristiky (např. definici minimálního ohraničujícího
obdélníku (`BoundingBox`), ...).

Snad všechny standardy podporují více typů dotazů klienta na server
(tzv.  *requestů*). Základním dotazem je vždy dotaz
*GetCapabilities* - server v odpovědi zformátované jako dokument XML
vrátí metadata, o jeho provozovateli a dostupných službách. Další typy
dotazy se liší podle dané služby, viz níže.

U většiny dotazů je potřeba specifikovat i verzi standardu, na základě
kterého se má klient se serverem "domluvit". Tento parametr
(*version*) není ale u dotazu *GetCapabilities* povinný.

Formát dotazu *GeoCapabilities* vypadá následovně:

::
  
    http://foo.bar/cgi-bin/service?service=WMS&request=GetCapabilities&version=1.3.0
                                  ^         ^                 ^               ^
                                  |         |                 |               |
    Adresa serveru a služby ------+         |                 |               |
    Specifikace  požadované služby ---------+                 |               |
    Specifikace dotazu ---------------------------------------+               |
    Případné další parametry (zde jako příklad verze standardu) --------------+

Tento způsob zápisu se nazývá *Key-Value-Pair* (KVP). Parametry dotazu
jsou definovány přímo jako součást URL. Parametry začínají za znakem
``?`` a jsou od sebe odděleny znakem ``&``.

Přehled nejdůležitější standardů OGC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    wms
    wmts
    wfs
    wcs
    wps
    gml
    kml
    sos
    cs-w
    simplefeatures
