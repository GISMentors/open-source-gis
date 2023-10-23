.. index:: SKKN

*************************
Katastrálne dáta SR v GIS
*************************

V predchádzajúcich kapitolách boli rozoberané súradnicové systémy, viď. :ref:`Souřadnicové systémy <souradnicovesystemy>`, dve základné reprezentácie dát v GIS, viď. :ref:`Reprezentace dat <reprezentacedat>`, priestorové databázy :ref:`Prostorové databáze <prostorovedatabaze>` a ďalšie. Všetky tieto znalosti sa dajú veľmi pekne a elegantne využiť aj pri práci s dátami slovenského katastra. Cieľom tejto kapitoly je predstaviť a ukázať možnosti pracovať so zásuvným modulom *SKKN tool*, resp. nástrojom *kataster-import*, nakoľko zásuvný modul *SKKN tool* aktuálne nie je funkčný. Samozrejme však plánujeme jeho aktualizáciu a opätovný chod.  

Nástroj *kataster-import* však funguje a dá sa plne využiť na konverziu a import grafických a popisných katastrálnych dát (KN) Slovenskej republiky (SR) do geografického informačného systému (GIS). 

Podrobná dokumentácia je na GitHube, viď. `lfurtkevicova/kataster-import <https://github.com/lfurtkevicova/kataster-import>`_ a pre plugin *SKKN tool* viď. `SKKN tool  <https://github.com/lfurtkevicova/kn-stuff/wiki/SKKN-tool>`_ *ako nový zásuvný modul v QGIS* (*https://github.com/lfurtkevicova/kn-stuff/wiki/SKKN-tool*).

Dnes existujú mnohé veľmi šikovné aplikácie ako napríklad tzv. *MAPKA* - `Mapový klient ZBGIS <https://zbgis.skgeodesy.sk/mkzbgis/sk/kataster?bm=zbgis&z=8&c=19.53000,48.80000#>`_ alebo interaktívna online mapa s vrstvami samospráv, obcí a miest, ktorá obsahuje aj ich územné plány, katastrálne dáta, zaujímavosti, atrakcie a vybavenosť `Mojamapa.sk <https://mojamapa.sk/?lang=sk>`_. Tieto nástroje sú veľmi nápomocné, no ich funkčnosť je často limitovaná.  

Webová mapová aplikácia *Mapový klient ZBGIS* slúži na interaktívnu prácu s údajmi ZBGIS (základná báza údajov pre geografický informačný systém), digitálnymi údajmi KN, registrom adries, registrom pôdy LPIS, referenčnými geodetickými bodmi, rastrovými mapami z archívu ako aj s digitálnym modelom reliéfu (terénu), ortofotosnímkami a geografickými názvami. Je to skrátka komplexný nástroj, ktorý zobrazuje, vyhľadáva a analyzuje priestorové údaje. 

Ako často prezentuje aj Úrad geodézie, kartografie a katastra SR (UGKK), je možné pracovať s dátami z externých zdrojov vo formáte *SHP*, *DGN*, *DXF*, *GML*, *GPX* alebo formou webových mapových služieb *WMS*, *WMTS*. V aplikácii je možné vytvárať tlačové výstupy a exporty do formátu *PDF*, vykonávať základné analýzy nad mapou ako meranie dĺžky a plochy, zobrazenie výškového profilu, získanie súradníc bodov alebo informácie o objektoch z mapy. 

Mapový klient ZBGIS je dokonca optimalizovaný na použitie priamo v mobilných zariadeniach, t.j. tablet, smartfón vďaka čomu možno pracovať priamo v teréne. Tiež je možné na základe aktuálnej polohy mobilného zariadenia identifikovať objekty na mape, napríklad nehnuteľnosť (parcelu) a následne získať o nej detailné informácie ako parcelné číslo, vlastník, číslo listu vlastníctva, druh pozemku, súpisné číslo stavby a podobne. Viac `tu <https://www.geoportal.sk/sk/sluzby/aplikacie/mapovy-klient-zbgis/>`_.

Ak vyššie uvedené platí, má význam rozmýšľať o tom, ako dostať grafické a popisné dáta KN SR do QGISu? 

Určite áno! Napriek tomu, že sa to za posledné roky ohromne posunulo vpred, sme presvedčení, že QGIS dokáže držať svoje čestné miesto. Viac v časti :ref:`Použitie v praxi <pouzitieskkn>`.


.. toctree::
   :maxdepth: 2

   nasadenie
   vstupne-data
   pouzitie
   
