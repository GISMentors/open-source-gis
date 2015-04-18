.. _ogc:

================================
Open Geospatial Consortium - OGC
================================

`OGC <http://opengeospatial.org>`_ je mezinárodní standardizační organizace pro
oblast prostorových dat a služeb, které funguje na relativně otevřené bázi
(poplatky za členství nejsou nijak přemrštěné). Standardy jsou vyvíjeny v rámci
relativně otevřeného procesu, každopádně po svém schválení jsou bez omezení
dostupné všem a jsou v praxi vždy implementovány.

Jednotlivé pracovní skupiny pracují na na problémech, které identifikovaly jako
potřebné. OGC standardizuje oblast datových formátů, ale především webových
služeb 

.. note:: `wikipedia:`Webová služba` je služba popsaná formátem WSDL, se kterou lze
    automaticky interagovat pomocí vlastního software. Webová služba OGC je na
    druhou stranu na XML založený komunikační protokol, který ovšem nemá s výše
    zmíněnou "obecně programátorskou technologií" mnoho společného.

Některé standardy byly akceptovány i organizací :ref:`iso`, seznam standardů lze
nalézt na stránce http://opengeospatial.org/standards.

.. _ogc-ows:

OGC OWS
-------
OGC Open Web Services (OGC OWS) je soubor standardů komunikačních protokolů
postavených na formátu XML, popisujících komunikaci mezi serverem a klientem.
Server nabízí prostřednictvím služeb data, rendery map či výpočetní služby, na
které klient může dosáhnout. Vlastnosti společné všem službám lze nalézt ve
specifikaci `Web Service Common <http://www.opengeospatial.org/standards/common>`_.
Ta popisuje zejména XML kódování metadat dalších webových služeb a některé
společné charakteristiky (např. definici hraničnícho BoundingBoxu, ...).

.. _ogc-wms:

OGC Wab Map Service - WMS
-------------------------
`WMS <http://opengeospatial.org/standards/wms>`_ je asi nejrozšířenější
standard. WMS slouží k popisu toho, jakým způsobem požaduje klient po serveru
vygenerovat mapový náhled z dat uložených (z pohledu klienta) na serveru.
Kartografii mapy lze do určité míry ovlivnit, vstupní data nikoliv.

WMS definuje 3 typy *requestů* na server od klienta:

* GetCapabilities
* GetMap
* Nepovinný GetFeatureInfo

WMTS
WFS
WCS
WPS
GML
KML
SOS
CS-W
SimpleFeature
