***************
Standardy v GIS
***************

.. index:: standardy, Shapefile, KML
           
GIS se jako obor etabloval v 80. letech 20 století. Za tu dobu se v
praxi prosadila celá řada oborových **de-facto** standardů,
t.j. standardů prosazených tržní silou, ale formálně
nepotvrzených. Jako příklad můžeme zmínit Esri :wikipedia:`Shapefile`
nebo v poslední době populární Google :wikipedia:`KML` (který byl ale
na rozdíl od Shapefile později standardizován konsorciem OGC).

V roce 1992 bylo ve Spojených státech amerických založeno sdružení
*Open GRASS Foundation* (OGF). Cílem sdružení bylo mimo jiné i hledání
koncensu při řešení společných problémů v rámci komunity uživatelů
softwaru :skoleni:`GRASS <grass-gis-zacatecnik>`. Na základech OGF bylo v
roce 1994 formováno konzorcium *Open GIS*, dnes nazývané `Open
Geospatial Consortium <http://opengeospatial.org>`_ (OGC) s cílem hledat
způsoby, jakými by mohly systémy GIS komunikovat prostřednictvím
počítačových sítí, pokud by využívali otevřených rozhraní definovaných
v rámci tzv. *Open Geodata Interoperability Specification* (OGIS).

.. index:: Open GIS
           
**Open GIS** konzorcium bylo založeno v roce 1994 devěti členy. V současnosti (rok
2016) má jeho nástupce OGC více než 500 členů - komerčních firem,
veřejných institucí, univerzit i jednotlivců. Dnes OGC poskytuje více
jako 35 implementačních standardů, které jsou **volně dostupné** a
adresují různé výzvy ve vztahu k prostorovým datům.  Další organizace,
například :doc:`ISO <iso>`, v České republice působící :ref:`ČSN
<csn>` a podobně, se také nějakým způsobem dotýkají problematiky
prostorových dat, často ale pouze přebírají standardy vydefinované na
půdě OGC a zařazují je do svých schémat.

Pokud pracujete delší dobu v nějakém oboru, natož v oboru zabývajícím se IT,
brzy zjistíte, že standardy jsou vždy:

* **zastaralé**, absolutně nereflektující současnou míru poznání a současně
  používané technologie,
* **nevyhovující** vašemu problému, který chcete aktuálně řešit,
* **zbytečně komplikované**, stačilo by to přeci udělat daleko jednodušeji.

Toho si všiml i autor komixu `XKCD <http://xkcd.com>`_ - každý si myslí, že umí
vytvořit lepší standard, než je ten stávající:

.. figure:: images/standards.png

    Zdroj: https://xkcd.com/927/

Standardy však každému oboru přinášejí několik pozitivních aspektů, jsou-li
uplatňovány dobře:

* komunikaci mezi softwarovými systémy,
* sdílení mezi softwarovými systémy,
* nahraditelnost a zastupitelnost softwarových řešení.

.. index:: interoperabilita
             
Jedním slovem nám standardy zajišťují **interoperabilitu** v rámci oboru.
Z pohledu otevřenosti a formálnosti můžeme oborové standardy zatřídit do
následujícího schématu:

.. aafig::
                                        de jure
                                          o
                                          |
                                          |
                                          |
                                          |
                  zavřené o---------------+----------------o otevřené
                                          |
                                          |
                                          |
                                          |
                                          o
                                        de facto

Standardy z pohledu otevřenosti a způsobu jejich vzniku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   pair: standardy; de-facto
           
**Uzavřené de-facto standardy**
    Jsou asi nejméně vhodným příkladem následování. V oboru GIS se s těmito
    standardy příliš často nesetkáváme, jsou však známy případy de-facto
    standardů, jejichž licence přímo zabraňovala jejich implementaci v
    nástrojích třetích stran. Takové standardy brzdí inovaci a není možné s nimi
    být interoperabilní v softwarech třetích stran.

**Otevřené de-facto standardy**
    
    Příkladem takového standardu může být formát Esri
    :wikipedia:`Shapefile`. Ten nikdy nebyl formalizován mimo firmu
    :wikipedia:`Esri`, ta ale nekladla žádné překážky v jeho
    implementaci v softwarech třetích stran. Formát se již dále
    nevyvíjí, takže brzdí inovace, interoperabilita je však zaručena
    dostatečně.

.. index::
   pair: standardy; de-jure

**Uzavřené de-jure standardy**

    Standardy, které nějakým způsobem vylučují část veřejnosti se
    podílet na jejich vývoji. Tím mohou být např. technické normy
    :doc:`ISO <iso>` nebo různé zákoné normy.  Příkladem může být
    evropská směrnice :doc:`INSPIRE <inspire>`. Interpoerabilita je
    zajištěna do té míry, do jaké je vynutitelné právo s těmito
    normami spojené. Inovace často vázne (což ostatně můžeme sledovat
    na směrnici INSPIRE).

**Otevřené de-jure standardy**
    
    Jsou pravěpodobně nejideálnějším stavem. Formálně potvrzené normy,
    na kterých se dohodla komunita uživatelů a vývojářů, mají největší
    podporu, nic nebrání jejich implementaci do softwarů různých
    stran, zároveň mohou být dále rozvíjeny. Příkladem těchto
    standardů jsou normy konzorcia :doc:`OGC <ogc/index>`.

Přehled standardů
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   epsg-standardy
   iso
   ogc/index
   inspire
   csn
   osgeo
   firmy
