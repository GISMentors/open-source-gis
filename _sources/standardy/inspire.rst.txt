.. _inspire:

=======
INSPIRE
=======

.. warning:: :red:`Obsahuje pouze osnovu kapitoly`

* http://inspire.gov.cz, Cenia
* Národní geoportál INSPIRE http://geoportal.gov.cz
* Příklad implementace http://portal.onegeology.org/
* Směrnice o geoprostorové infrastruktuře v Evropě
* Data o životním prostředí
* Harmonizace datových sad
* Harmonizace služeb (postaveno na OGC OWS)
    * Discovery service (--> OGC CS-W)
    * View service (--> OGC WMS, WMTS)
    * Download service (--> OGC WCS, WFS, Atom)

Stahovací služby jsou nejčastěji implementovány prostřednictvím XML dokumentů
`Atom <https://tools.ietf.org/html/rfc4287>`_. Tyto dokumenty pak odkazují na
předgenerované soubory v rastrových i vektorových formátech. Použití GML není
povinné.

Prohlížecí služby jsou stále častěji implementovány prostřednictvím některé z
dlaždicovacích služeb (WMTS, TMS).
