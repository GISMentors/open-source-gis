=================
Vektorové formáty
=================
Mezi nejčastěji používané vektorové formáty v GIS patří 

* ESRI :wikipedia:`Shapefile`
* :wikipedia:`KML`
* :wikipedia-en:`GML`
* :wikipedia-en:`GeoJSON`

Formát, který by si zasloužil větší pozornost je :wikipedia-en:`OGC GeoPackage`

Vektorová data se také tradičně ukládají do prostorových databází (popsaných v
další části).

.. tip:: Více informace na školení :skoleni:`GeoPython <geopython>`.

Formát ESRI Shapefile
---------------------

Formát ESRI Shapefile je tradičně nejpoužívanějším formátem pro vektorová data.
Tento systém je dnes již zastaralý, nicméně pro některé jednodušší typy dat
stále dostačující. Je podporován prakticky všemi nástroji GIS a ve své době se
stal prakticky oborovým standardem. Důvodem je, že firma ESRI uvolnila
dokumentaci k tomuto formátu a jeho licence nezakazuje jeho implementaci v
software, který by se mohl označit za konkureční.

Data jsou uložena ve třech souborech, lišících se od sebe navzájem koncovkou:

* \*.shp - geometrie (shape)
* \*.dbf - atributy (databáze)
* \*.shx - propojení geometrie a atributů (index)

Data jsou uložena v tepologické formě - každá plocha má svou vlastní hranici.

Důvody proč dnes již ESRI Shapefile nepoužívat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Z dnešního pohledu obsahuje formát Shapefile tato slabá místa:

* data nejsou uložena v jednom souboru, ale hned ve trojici (shp+shx+dbf). Různé
  softwarové produkty si navíc přidávají vlastní metadatové soubory, které
  nejsou součástí specifikace tohoto formátu.
* Názvy atributů jsou omezeny pouze na deset znaků.
* Data neobsahují informaci o znakové sadě, což vede k problémům při automatické
  konverzi dat a používání na více operačních systémech.
* Velikost souborů je maximálně 2GB.
* Neumožňuje ukládat topologické informace o vzájemných vztazích mezi prvky
  geodat.
* Každý soubor SHP umožňuje ukládat pouze jeden typ geometrie (bod,
  linie, polygon)
* neumožňuje uložit stromovou strukturu dat

Důvody proč se ESRI Shapefile stále používá
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Je podporován prakticky všemy softwary

Formát KML
----------
OGC :wikipedia:`KML` je určen především pro vizualizaci jednotlivých prvků
geodat. Formát byl původně vyvinut firmou Google a je postavený na jazyce XML.
Data v souborech KML, na rozdíl od GML (viz níže), umožňují použít pouze
souřadnicový systém WGS 84.

KML podporují produkty firmy Google, ale i řada služeb a programů třetích stran.
Bývá často podporován moderními GPS přijímači. V minulosti býval nasazován ve
webových mapových aplikacích, protože je v porovnání s GML menší a obsahuje
zmíněnou informaci o vizualizaci jednotlivých prvků geodat. Ačkoliv byl v době
před cca 3 lety tento formát populární, dnes je často nahrazován formátem
GeoJSON.

Formát GML
----------
OGC :wikipedia:`GML` (Geography Markup Language) jako otevřený standard je
perspektivním formátem pro přenos vektorových dat. Jedná se o jednosouborový
textový formát založený na značkovacím jazyce XML, je proto interpretovatelný i
bez speciálního software.  Kromě standardizace na úrovni OGC je definován
technickou normou ISO 19136.  Vzhledem k tomu je podporován většinou moderních
GIS nástrojů. GML je také předepsaný technickými dokumenty INSPIRE a výchozím
formátem služby WFS.

GML se používá jako univerzální formát pro data, která mohou mít i
komplikovanější stromovou strukturu. Díky tomu, že je postaven na XML, je jeho
strojové zpracování jednoduché i běžnými systémy, například pomocí transformace
XSLT.

Formáty GeoJSON a TopoJSON
--------------------------
Populárními formáty se v poslední době stávají formáty odvozené z formátu JSON,
především GeoJSON a TopoJSON. Formáty JSON mají své uplatnění především mezi
webovými technologiemi. Oproti formátům odvozených z XML (GML, KML) mají kratší
zápis, což je výhodné při přenosech v prostředí Internetu. Stejně jako při
využití formátů odvozených z XML, je i zde je možné zabezpečit správnost
struktury dat to pomocí schémat.

JSON je velice přívětivý k netypovým programovacím jazykům, je srozumitelný
prostým lidským okem. Souřadnicový systém není v těchto formátech jak
specifikovat, předpokládá se, že se jedná o WGS 84. Data lze libovolným způsobem
zanořovat a větvit.

`GeoJSON <http://geojson.org>`_ je využíván u webových služeb pro svůj malý
objem a jednoduchost. Je méně náročný na zpracování, což je vhodné zejména u
webových prohlížečů. U uživatelů mimo svět GIS je oblíbený, protože jeho
strukturu je možné rychle pochopit a připravit vlastní parser.

`TopoJSON <https://github.com/mbostock/topojson>`_ je druhým formátem odvozeným
z formátu JSON, který ale zatím nenabyl takové popularity jako GeoJSON. Hlavním
úkolem formátu TopoJSON je minimalizace datového toku mezi webovým serverem a
klientem. Formát je částečně ztrátový, neboť souřadnice bodů a lomových bodů
jsou zapisovány v relativní poloze od daného počátku a v celých číslech (ztrácí
se přesnost). K úspoře datové velikosti vede také fakt, že např. hranice
polygonů jsou uloženy pro dvě sousedící plochy pouze jednou (formát je tedy
topologický).
