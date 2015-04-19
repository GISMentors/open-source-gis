.. _standardy-gis:

***************
Standardy v GIS
***************

GIS jako obor se etabloval v 80. letech 20 století. Za tu dobu se v praxi
prosadila celá řada oborových *de-facto* standardů (standardy prosazené tržní
silou, ale formálně nepotvrzené). Jako příklad můžeme zmínit ESRI
:wikipedia:`Shapefile` nebo v poslední době populární Google :wikipedia:`KML`.

V roce 1992 bylo ve Spojených státech amerických založeno sdružení *Open GRASS
Foundation (OGF)*. Cílem sdružení bylo mimo jiné i hledání koncensu při hledání
společných řešení v rámci komunity uživatelů softwaru GRASS. Většina řešení se
však točila okolo softwaru GRASS a také proto bylo v roce 1994 formováno
konzorcium Open GIS, dnes nazývané `Open Geospatial Consortium
<http://opengeospatial.org>`_ s cílem hledat způsoby, jakými by mohly systémy
komunikovat prostřednictvím počítačových sítí, pokud by využívali otevřených
rozhraní definovaných v rámci "Open Geodata Interoperability Specification"
(OGIS).

Open Geospatial Consortium bylo založilo v roce 1994 devět členů. V roce 2015 má
sdružení na 500 členů (komerčních firem, veřejných institucí, univerzit i
jednotlivců). 

Dnes OGC poskytuje více jako 35 implementačních standardů, které jsou *volně
dostupné* a adresují různé výzvy ve vztahu k prostorovým datům.

Další organizace (např. ISO, v České republice působící ČSN a podobně) se také
nějakým způsobem dotýkají problematiky prostorových dat, často ale pouze
přebírají standardy vydefinované na půdě OGC a zařazují je do svých schemat.

Pokud pracujete delší dobu v nějakém oboru, natož v oboru zabývajícím se IT,
brzy zjistíte, že standardy jsou

* vždy *zastaralé*, absolutně nereflektující současnou míru poznání a současně
  používané technologie
* vždy *nevyhovující* vašemu problému, který chcete aktuálně řešit
* vždy *zbytečně komplikované*, stačilo by to přeci udělat daleko jednodušeji.

Jak si všiml již autor komixu `XKCD <http://xkcd.com>`_, každý si myslí, že umí
vytvořit lepší standard, než je ten stávající

.. figure:: images/standards.png

    Zdroj: https://xkcd.com/927/

Standardy však každému oboru přinášejí několik pozitivních aspektů (jsou-li
uplatňovány dobře):

* komunikace mezi softwary
* sdílení mezi softwary
* nahraditelnost a zastupitelnost softwarových řešení

jedním slovem nám standardy zajišťují **interoperabilitu** v rámci oboru.

Z pohledu otevřenosti a formálnosti můžeme oborové standardy zatřídit do
následujícího schematu

.. figure:: images/standardy-trideni.png

    Standardy z pohledu otevřenosti a způsobu jejich vzniku

**Uzavřené de-facto standardy**
    Jsou asi nejméně vhodným příkladem následování. V oboru GIS se s těmito
    standardy příliš často nesetkáváme, jsou však známy případy de-facto
    standardů, jejichž licence přímo zabraňovala jejich implementaci v
    nástrojích třetích stran. Takové standardy brzdí inovaci a není možné s nimi
    být interoperabilní v softwarech třetích stran.

**Otevřené de-facto standardy**
    Příkladem takového standardu může být formát ESRI Shapefile. Ten nikdy nebyl
    formalizován mimo firmu ESRI, ta ale nekladla žádné překážky v jeho
    implementaci v softwarech třetích stran. Formát se již dále nevyvíjí, takže
    brzdí inovace, interoperabilita je však zaručena dostatečně.

**Uzavřené de-jure standardy**
    Standardy, které nějakým způsobem vylučují část veřejnosti na podílet se na
    jejich vývoji. Tím mohou být např. normy ISO nebo různé zákoné normy.
    Příkladem může být evropská směrnice INSPIRE. Interpoerabilita je zajištěna
    do té míry, do jaké je vynutitelné právo s těmito normami spojené. Inovace
    často vázne (což ostatně můžeme sledovat na směrnici INSPIRE).

**Otevřené de-jure standardy**
    Jsou pravěpodobně nejideálnějším stavem. Formálně potvrzené normy, na
    kterých se dohodla komunita uživatelů a vývojářů mají největší podporu, nic
    nebrání jejich implementaci do softwarů různých stran, zároveň mohou být
    dále rozvíjeny. Příkladem těchto standardů jsou normy konzorcia OGC.


.. toctree::
   :maxdepth: 2

   epsg
   iso
   ogc/index
   inspire
   csn
   osgeo
   firmy
