.. _ogc:

================================
Open Geospatial Consortium - OGC
================================

`OGC <http://opengeospatial.org>`__ je mezinárodní standardizační organizace pro
oblast prostorových dat a služeb, která funguje na relativně otevřené bázi
(poplatky za členství nejsou nijak přemrštěné). Standardy jsou vyvíjeny v rámci
relativně otevřeného procesu. Po svém schválení jsou bez omezení
dostupné všem a jsou v praxi vždy implementovány.

Jednotlivé pracovní skupiny pracují na problémech, které identifikovaly jako
potřebné. OGC standardizuje oblast datových formátů, ale především webových
služeb. 

.. note:: :wikipedia:`Webová služba` je služba popsaná formátem :wikipedia:`WSDL`, se kterou lze
    automaticky interagovat pomocí vlastního software. Webová služba OGC je na
    druhou stranu na XML založený komunikační protokol, který ovšem nemá s výše
    zmíněnou "obecně programátorskou technologií" mnoho společného.

Některé standardy byly akceptovány i organizací :ref:`iso`. Seznam standardů lze
nalézt na stránce http://opengeospatial.org/standards.

.. _ogc-ows:

OGC OWS
-------

**OGC Open Web Services** (OGC OWS) je soubor standardů komunikačních protokolů
postavených na formátu :wikipedia:`XML` popisujících komunikaci mezi serverem a klientem.
Server nabízí prostřednictvím služeb data, rendery map či výpočetní služby, na
které klient může dosáhnout. Vlastnosti společné všem službám lze nalézt ve
specifikaci `Web Service Common <http://www.opengeospatial.org/standards/common>`_.
Ta popisuje zejména XML kódování metadat dalších webových služeb a některé
společné charakteristiky (např. definici minimálního ohraničujícího obdélníku (`BoundingBox`), ...).

Snad všechny standardy podporují více typů dotazů z klienta na server (tzv.
*requestů*). Základním dotazem je vždy dotaz *GetCapabilities* - server v
odpovědi zformátované jako dokument XML vrátí metadata o serveru, jeho
provozovateli a dostupných službách. Další dotazy jsou již pro každou službu
jiné.

U většiny dotazů je potřeba specifikovat i verzi standardu, podle kterého se
klient se serverem mají "domluvit". Tento parametr není ale u GetCapabilities
requestu povinný.

Formát dotazu na server vypadá pro všechny služby např. následovně::

    http://foo.bar/cgi-bin/service?service=WMS&request=GetCapabilities&version=1.3.0
                                  ^         ^                 ^               ^
                                  |         |                 |               |
    Adresa serveru a služby ------+         |                 |               |
    Specifikace  požadované služby ---------+                 |               |
    Specifikace requestu -------------------------------------+               |
    Případné další parametry (zde jako příklad verze standardu) --------------+

Tento způsob zápisu se nazývá *Key-Value-Pair* (KVP). Parametry jsou definovány přímo jako součást URL. Parametry dotazu začínají za znakem ``?`` a jednotlivé parametry jsou
od sebe odděleny znakem ``&``.

Nejdůležitější standardy OGC rozebereme v dalších částech:

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
