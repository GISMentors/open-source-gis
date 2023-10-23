.. _ogc-wps:

OGC Web Processing Service - WPS
--------------------------------

.. warning:: :red:`Tato část je pahýl`

`OGC Web Processing service <https://opengeospatial.org/standards/wps>`_
umožňuje, aby server nabídnul určité předdefinované procesy - výpočetní operace
nad daty - směrem ke klientským aplikacím.

Druh výpočetních operací - tzv. *procesů* - není definovaný, každý server tak
nabízí jiné. Server může nabízet jednoduché úlohy, jako je součet hodnot pixelů
dvou rastrových map, nebo komplexní, jako je výpočet globální klimatické změny.

WPS komunikuje na bázi XML dokumentů posílaných prostřednictvím HTTP POST
requestů.

Jsou definovány tři typy requestů: 

* GetCapabilities - vrací XML dokument s metadaty služby a seznamem procesů
* DescribeProcess - vrací XML dokument s detailním popisem vstupních a
  výstupních datových typů pro vybraný proces
* Execute - spustí výpočet na serveru a předá mu vstupní data zaslaná klientem

Jsou definovány 3 datové typy pro vstupy a výstupy z procesu:

* LiterlData - textové řetězce libovolné velikosti či datového typu
* ComplexData - rastrové nebo vektorové datasety
* BoundingBoxData - hraniční souřadnice zájmového území

