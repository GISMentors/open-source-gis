.. warning:: :red:`Kapitola je ve výstabě`

`MapServer <http://mapserver.org>`__ je jeden z nejstarších programů sloužících k
distirbuci prostorových dat. Původně byl vývoj financován NASA a odehrával se
primárně na University of Minnesota (ve starší literatuře se o něm hovoří jako o
UMN MapServer).

MapServer je dnes řada nástrojů - vedle vlastního mapvého serveru obsahuje i
cash server, WFS server a sadu nástrojů pro příkazovou řádku, umožňujících
provádět některé operace

* MapScript
* MapCache
* TinyOWS

Konzolové nástroje pro MapServer
--------------------------------

Většina nástrojů pracuje se vstupním konfiguračním souborem `Mapfile`, případně
se vstupním souborem `ESRI Shapefile`.

`legend`
    Nástroj pro generování obrázků s legendou, definovanou v mapfile.

`mapserv`
    Vlastní MapServer - většinou je spouštěn přes CGI rozhraní webového serveru

`msencrypt`
    Nástroj pro vytváření kryptovacích klíčů pro připojení k databázím
    (`CONNECTION` v `MapFile`). Soubor se potom použije v parametru
    `MS_ENCRYPTION_KEY`.
    
`scalebar`
    Podobně jako `legend` - vytvoří obrázek s měřítkem na základně vstupního
    `mapfile`

`shp2img`
    Vytvoří obrázek na základně `mapfile` a dalších parametrů. Je vhodný pro
    testování mapfilů, při nastavení úrovně *ukecanosti* se může podařit odhalit
    problémy s připojením a podobně.

`shptree`
    Vytváří :wikipedia-en:`Quadtree` prostorový index pro zadaný Shapefile. Měl by
    se podstatně zrychlit běh aplikace.

`shptreetst` a `shptreevis`
    Slouží ke kontrole vytvořeného indexu. `shptreevis` vyrobí shapefile, který
    si lze prohlídnout, `shptreetst` k výpisu informací o prvcích na základě
    indexu.

`sortshp`
    Seřadí prvky v shapefile podle zadaného sloupce (opět by mělo vézt ke
    zrychelní).

`tile4ms`
    Vytvoří soubor s indexem shapefilů, podobně jako `ogrtindex`.
