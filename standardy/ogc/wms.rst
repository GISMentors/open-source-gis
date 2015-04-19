.. _ogc-wms:

OGC Web Map Service - WMS
-------------------------
`WMS <http://opengeospatial.org/standards/wms>`_ je asi nejrozšířenější
standard. WMS slouží k popisu toho, jakým způsobem požaduje klient po serveru
vygenerovat mapový náhled z dat uložených (z pohledu klienta) na serveru.
Kartografii mapy lze do určité míry ovlivnit, vstupní data nikoliv.

WMS definuje 3 typy *requestů* na server od klienta (většina slušeb funguje
podobně, proto se pokusíme WMS rozebrat podrobněji):

* GetCapabilities
* GetMap
* Nepovinný GetFeatureInfo

.. _wms-capabilities:

WMS GetCapabilities
^^^^^^^^^^^^^^^^^^^
Jako příklad zvolíme službu ČUZK, poskytující letecké snímky, dostupnou na
adrese http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx

Tzv. `Capabilities` dokument dostaneme po zavolání requestu *GetCapabilities*:

http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx?service=WMS&request=GetCapabilities

Opět se pokusíme tuto adresu více rozebrat::

    http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx?service=WMS&request=GetCapabilities
                                                           ^          ^                 ^
    Adresa serveru ČUZK a služby s leteckým snímkem -------+          |                 |
    Specifikace požadované služby OGC WMS ----------------------------+                 |
    Specifikace requestu GetCapabilities -----------------------------------------------+

Po zadání této adresy do prohlížeče server ČUZK vrátí dokument XML s
*Capabilitiers* - schopnostmi serveru. V případě OGC WMS má 2 části (první část
bývá pro všechny služby OGC OWS stejná nebo alespoň hodně podobná) - metadata
serveru (v části *Service*) a informace o dostupných službách (*Capability*):

.. code-block:: xml

    <WMS_Capabilities xsi:schemaLocation="http://www.opengis.net/wms ....>
        <Service>
            <Name>WMS</Name>
            <Title>Prohlížecí služba WMS - Ortofoto</Title>
            <Abstract>Prohlížecí služba WMS-ORTOFOTO je poskytována jako veřejná prohlížecí služba nad aktu...</Abstract>
            ...
            <ContactInformation>
            ...
            </ContantInformation>
            <Fees>Neplatí</Fees>
            <AccessConstraints>http://geoportal.cuzk.cz/Dokumenty/Podminky_sluzby_CUZK.pdf</AccessConstraints>
        </Service>
        <Capability>
            <Request>
                ...
            </Request>
            <inspire_vs:ExtendedCapabilities>
                ...
            </inspire_vs:ExtendedCapabilities>
            <Layer>
                ...
            </Layer>
        </Capability>
    </WMS_Capabilities>

Service
"""""""
V části dokumentu označené jako *Service* jsou uloženy metadata služby. Její
*jméno*, *titulek* a širší popis *abstrakt*. Dále zde nalezneme kontaktní
informace na provozovatele služby, informace o poplatcích a omezeních přístupu.

Capability
""""""""""
V části *Capability* jsou již praktické informace pro připojení služby, adresy
URL na jednotlivé dotazy (*GetCapabilities*, *GetMap* a *GetFeatureInfo*, které
mohou být různé(!)) a seznam dostupných vrstev (ten může být hierarchicky
zanořený).

V tomto dokumentu také můžeme vidět obsáhlou část, kterou jsou metadata doplněna
o atributy vyžadované směrnicí INSPIRE. V původní definici dokumentu toto
vyžadováno není. INSPIRE tak pouze rozšiřuje existující standard (což považujeme
za příhodné a elegantní řešení).

Layer
"""""
Podíváme se blíže na část `Layer`

.. code-block:: xml
    
    ...
    <Layer cascaded="1">
        <Name>GR_ORTFOTORGB</Name>
        <Title>Ortofoto</Title>
        <Abstract>Vrstva Ortofoto</Abstract>
        <KeywordList>
            <Keyword>ortofoto</Keyword>
        </KeywordList>
        <CRS>EPSG:5514</CRS>
        <CRS>EPSG:4326</CRS>
        <CRS>EPSG:3857</CRS>
        ...
        <BoundingBox CRS="EPSG:5514" minx="-950003.17502118601" miny="-1250003.1750036045" maxx="-399990.47499578597" maxy="-899996.82499090442" resx="6.3500127000253999" resy="-6.3500127000253999"/>
        <BoundingBox CRS="EPSG:4326" miny="11.214011580382529" minx="47.964914601259672" maxy="19.407662623095131" maxx="51.691664934538636"/>
        <BoundingBox CRS="EPSG:3857" minx="1248338.0588780562" miny="6101019.8582439059" maxx="2160451.1206905982" maxy="6744565.3811490489"/>
        ...
        <Attribution>
            <Title>© Český úřad zeměměřický a katastrální</Title>
            <OnlineResource xlink:href="http://www.cuzk.cz" xlink:type="simple"/>
            <LogoURL height="20" width="20">
                <Format>image/gif</Format>
                <OnlineResource xlink:href="http://geoportal.cuzk.cz/design/logo.gif" xlink:type="simple"/>
            </LogoURL>
        </Attribution>
        ...
        <Style>
            <Name>Default</Name>
            <Title>Default</Title>
            <LegendURL width="20" height="15">
            <Format>image/png</Format>
            <OnlineResource xlink:href="http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/service.svc/static/f/?url=cvRUdcV2CPFS0o8h5ybhxX6qEmzygaSiEtM9cmnqmf0aheaOd03QaWtixWLnm8KfxF2JRJSNQObGSKgtEvQU3g%3d%3d=lang=eng" xlink:type="simple"/>
            </LegendURL>
        </Style>
        <MinScaleDenominator>2.5253813613805272</MinScaleDenominator>
        <MaxScaleDenominator>7576144.0841415804</MaxScaleDenominator>
    </Layer>
    ...

Každá vrstva je identifikovaná svým jménem (*Name*), má nadpis (*Title*) a může
mít širší popis (*Abstract*). Za klíčovými slovy následuje seznam podporovaných
souř. systémů. Některé servery podporují ve výchozím nastavení "všechny", což
značně komplikuje parserování podobných odpovědí.

V další části lze dohledat hraniční souřadnice dat *BoundingBox*, *Attribution*
pak obsahuje informce o licenci a copyrightu. Některé vrstvy nabízejí více
možností, jak zobrazit legendu (*Style*). Nakonec následují inforace o
měřítcích, ve kterých se bude daná vrstva renderovat.

WMS GetMap
^^^^^^^^^^
Po prostudování dokumentu *Capabilities* jsme schopni (nebo námi napsaný
program) sestavit request *GetMap*, který vrátí mapu. WMS server vrací mapu na
základě dotazu, ve kterém musí být specifikováno:

* Identifikátor vrstev
* Souř. systém
* Hraniční souřadnice požadovaného výřezu
* Velikost obrázku
* Formát obrázku
* a některé nepovinné parametry

::

    http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx?
    ^   service=WMS&
    |   ^   request=GetMap&
    |   |   ^   version=1.3.0&
    |   |   |   ^   layers=GR_ORTFOTORGB&
    |   |   |   |   ^   format=image/jpeg&
    |   |   |   |   |   ^   width=800&height=600&
    |   |   |   |   |   |   ^   bbox=50.5,14.0,50.8,14.3&
    |   |   |   |   |   |   |   ^   crs=epsg:4326&
    |   |   |   |   |   |   |   |   ^   styles=
    |   |   |   |   |   |   |   |   |   ^
    |   |   |   |   |   |   |   |   |   +- Legenda
    |   |   |   |   |   |   |   |   +- Souř. systém
    |   |   |   |   |   |   |   +- Hraniční souřadnice výřezu
    |   |   |   |   |   |   +- Velikost obrázku
    |   |   |   |   |   +- Formát výstupního obrázku
    |   |   |   |   +- Seznam vrstev
    |   |   |   +- Verze standardu
    |   |   +- Požadavek GetMap
    |   +- Specifikace služby
    +- Server URL

http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx?service=WMS&request=GetMap&version=1.3.0&layers=GR_ORTFOTORGB&format=image/jpeg&width=800&height=600&bbox=50.5,14.0,50.8,14.3&crs=epsg:4326&styles= 

.. figure:: images/wms_ortofoto.jpg
    
    Letecký snímek stažený ze služby OGC WMS ze serverů ČUZK, `Zdroj <http://geoportal.cuzk.cz/WMS_ORTOFOTO_PUB/WMService.aspx?service=WMS&request=GetMap&version=1.3.0&layers=GR_ORTFOTORGB&format=image/jpeg&width=800&height=600&bbox=50.5,14.0,50.8,14.3&crs=epsg:4326&styles=>`_

.. note:: Všiměte si, že hraniční souřadnice jsou zadány ve formě `miny, minx,
    maxy, maxx` - cože je v rozporu s obecně platným zápisem párů souřadnic `[x, y]`. 

    To je způsobeno tím, že ve standardu WMS verze 1.3.0, se dbá na pořadí
    souřadnic, *jak jsou definovány v souřadicovém systému*. Systém WGS84
    preferuje zápis v pořadí Y, X. Stejně tak např. INSPIREm předepsaný
    ETRS (:epsg:`3035`). To samé by mohlo platit pro systém S-JTSK
    (`epsg:5514`), v praxi se ale pořadí os souřadnic `[x, y]` zachovává.

    Jak lze tušit, způsobuje tato nekonzistence množství problémů v komunikaci
    mezi servery klienty, i vzhledem k tomu, že ve starších verzích standardu
    WMS byl zápis pořadí souřadnic *vždy* `[x, y]`.

WMS GetFeatureInfo
^^^^^^^^^^^^^^^^^^
Pokud to daná vrstva na daném serveru podporuje, je možné se dotázat na hodnotu
pixelu na daných souřadnicích. To je-li to možné, se dozvíme z atributu
`queryable` u každé vrstvy. V případě této služby, není žádná vrstva
dotazovatelná, ale zdá se, že služba nabízející databázi ZABAGED takovou
dotazovatelnou vrstvu obsahuje:

http://geoportal.cuzk.cz/WMS_ZABAGED_PUB/WMService.aspx?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities

.. code-block:: xml

    ...
    <Layer queryable="1" opaque="0" noSubsets="0">
        <Name>GL_CA010</Name>
        <Title>Vrstevnice základní</Title>
        <Abstract>Vrstva Vrstevnice základní</Abstract>
        <KeywordList>
            <Keyword>vrstevnice základní</Keyword>
        </KeywordList>
        <CRS>EPSG:3035</CRS>
        <CRS>EPSG:3034</CRS>
        <CRS>EPSG:4326</CRS>
        <CRS>EPSG:4258</CRS>
        ...
        <MinScaleDenominator>1</MinScaleDenominator>
        <MaxScaleDenominator>15000</MaxScaleDenominator>
    </Layer>
    ...

*GetFeatureInfo* request potřebuje stejné parametry jako potřeje *GetMap*
request a k tomu ještě následující hodnoty:

* `request=GetFeatureInfo` hodnota parametru `request` je samozřejmě změněna
* `QUERY_LAYERS=GL_CA010` vrstvy o které se zajímáme
* `INFO_FORMAT=text/html` formát odpovědi
* `I=568&J=179` souřadnice dotazu v pixelech obrázku

http://geoportal.cuzk.cz/WMS_ZABAGED_PUB/WMService.aspx?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&BBOX=49.87085021713301103,15.03782399164211903,49.88182000062317911,15.05671808005681278&CRS=EPSG:4326&WIDTH=1247&HEIGHT=724&LAYERS=GL_CA010&STYLES=&FORMAT=image/png&QUERY_LAYERS=GL_CA010&INFO_FORMAT=text/html&I=568&J=179&FEATURE_COUNT=10

Odpověď ze serveru:

+---------------------+
| Vrstevnice základní |
+======+==============+
|ID    | 24358813     |
+------+--------------+
|MAPNO | 133221       |
+------+--------------+
|VYSKA | 408          |
+------+--------------+

.. note:: Dotaz byl poskládán pomocí programu QGIS. Odhadovat BBOX vrstvy a
    souřadnice obrázku samozřejmě lze (po dopočítání rozlišení pixelu), ale
    pomocí již napsaného software je to přesnější.
