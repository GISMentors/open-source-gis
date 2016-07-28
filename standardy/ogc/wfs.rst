.. _ogc-wfs:

OGC Web Feature Service - WFS
-----------------------------

http://opengeospatial.org/standards/wfs

.. warning:: :red:`Obsahuje pouze osnovu kapitoly`

* WMS vrací obrázky map, WFS slouží pro práci s "features" - vektorovými objekty
* Pokud to server podporuje, je možné provádět některé prostorové operace na
  straně serveru, stejně jako filtrovat podle požadavků klienta
* WFS-T (transactional WFS) umožňuje editovat elementy na straně serveru,
  zamykat jednotlivé záznamy
* Primárně pracuje s formátem GML, ale pokud to server podporuje, umožňuje i
  další

Přílad: ``AOPK WFS http://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?``

WFS GetCapabilities
^^^^^^^^^^^^^^^^^^^
https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?server=WFS&request=getcapabilities

.. code-block:: xml

  <wfs:WFS_Capabilities version="1.1.0" xsi:schemaLocation="http://w... >
    <ows:ServiceIdentification>
        <ows:Title>Chráněná území</ows:Title>
        <ows:Abstract>Služba zpřístupňuje geografická data zvláště a smluvně chráněných území v České republice</ows:Abstract>
        <ows:Keywords>
            <ows:Keyword>Chráněné území</ows:Keyword>
        </ows:Keywords>
        <ows:ServiceType>WFS</ows:ServiceType>
        <ows:ServiceTypeVersion>1.1.0</ows:ServiceTypeVersion>
        <ows:Fees>žádné</ows:Fees>
        <ows:AccessConstraints>licence (CC BY 3.0 CZ): Uveďte původ</ows:AccessConstraints>
    </ows:ServiceIdentification>
    <ows:ServiceProvider>
        <ows:ProviderName>Agentura ochrany přírody a krajiny České republiky</ows:ProviderName>
        <ows:ProviderSite xlink:href="http://www.ochranaprirody.cz"/>
        ...
    </ows:ServiceProvider>
    <ows:OperationsMetadata>
        ...
    </ows:OperationsMetadata>


seznam dostupných prvků

.. code-block:: xml

    <wfs:FeatureTypeList>
        <wfs:FeatureType>
            <wfs:Name>UzemniOchrana_ChranUzemi:Velkoplošné_zvláště_chráněné_území</wfs:Name>
            <wfs:Title>Velkoplošné_zvláště_chráněné_území</wfs:Title>
            <wfs:DefaultSRS>urn:ogc:def:crs:EPSG:6.9:5514</wfs:DefaultSRS>
            <wfs:OtherSRS>urn:ogc:def:crs:EPSG:6.9:4326</wfs:OtherSRS>
            <wfs:OutputFormats>
            <wfs:Format>text/xml; subType=gml/3.1.1/profiles/gmlsf/1.0.0/0</wfs:Format>
            </wfs:OutputFormats>
            <ows:WGS84BoundingBox>
                <ows:LowerCorner>12.135781691549301 48.405980213444934</ows:LowerCorner>
                <ows:UpperCorner>18.824874392730379 51.278530725092587</ows:UpperCorner>
            </ows:WGS84BoundingBox>
        </wfs:FeatureType>
        <wfs:FeatureType>
        ...
        <wfs:FeatureType>
            <wfs:Name>UzemniOchrana_ChranUzemi:Maloplošné_zvláště_chráněné_území__MZCHÚ_</wfs:Name>
            <wfs:Title>Maloplošné_zvláště_chráněné_území__MZCHÚ_</wfs:Title>
            <wfs:DefaultSRS>urn:ogc:def:crs:EPSG:6.9:5514</wfs:DefaultSRS>
            <wfs:OtherSRS>urn:ogc:def:crs:EPSG:6.9:4326</wfs:OtherSRS>
            <wfs:OutputFormats>
            <wfs:Format>text/xml; subType=gml/3.1.1/profiles/gmlsf/1.0.0/0</wfs:Format>
            </wfs:OutputFormats>
            <ows:WGS84BoundingBox>
                <ows:LowerCorner>11.996206262583122 48.270769845462425</ows:LowerCorner>
                <ows:UpperCorner>18.952872493443596 51.240248516869322</ows:UpperCorner>
            </ows:WGS84BoundingBox>
        </wfs:FeatureType>
        <wfs:FeatureType>
        ...
    </wfs:FeatureTypeList>

Filtrovací operace podporované serverem

.. code-block:: xml

    <ogc:Filter_Capabilities>
        <ogc:Spatial_Capabilities>
            <ogc:GeometryOperands>
                <ogc:GeometryOperand>gml:Envelope</ogc:GeometryOperand>
                <ogc:GeometryOperand>gml:Point</ogc:GeometryOperand>
                <ogc:GeometryOperand>gml:Polygon</ogc:GeometryOperand>
                <ogc:GeometryOperand>gml:LineString</ogc:GeometryOperand>
            </ogc:GeometryOperands>
            <ogc:SpatialOperators>
                <ogc:SpatialOperator name="BBOX"/>
                <ogc:SpatialOperator name="Equals"/>
                <ogc:SpatialOperator name="Disjoint"/>
                <ogc:SpatialOperator name="Intersects"/>
                <ogc:SpatialOperator name="Crosses"/>
                <ogc:SpatialOperator name="Touches"/>
                <ogc:SpatialOperator name="Within"/>
                <ogc:SpatialOperator name="Contains"/>
                <ogc:SpatialOperator name="Overlaps"/>
            </ogc:SpatialOperators>
        </ogc:Spatial_Capabilities>
        <ogc:Scalar_Capabilities>
            <ogc:LogicalOperators/>
            <ogc:ComparisonOperators>
                <ogc:ComparisonOperator>EqualTo</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>NotEqualTo</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>LessThan</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>GreaterThan</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>LessThanEqualTo</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>GreaterThanEqualTo</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>Like</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>Between</ogc:ComparisonOperator>
                <ogc:ComparisonOperator>NullCheck</ogc:ComparisonOperator>
            </ogc:ComparisonOperators>
        </ogc:Scalar_Capabilities>
        <ogc:Id_Capabilities>
            <ogc:EID/>
            <ogc:FID/>
        </ogc:Id_Capabilities>
        </ogc:Filter_Capabilities>
    </wfs:WFS_Capabilities>

Stáhnutí dat
------------

Výchozí souř. systém (EPSG:5514)
  https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?server=WFS&request=getfeature&typename=UzemniOchrana_ChranUzemi:Velkoplo%C5%A1n%C3%A9_zvl%C3%A1%C5%A1t%C4%9B_chr%C3%A1n%C4%9Bn%C3%A9_%C3%BAzem%C3%AD

To samé jako WGS84
(Pozor na pořadí souřadnic (viz Capabilities response) )
  https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?server=WFS&request=getfeature&typename=UzemniOchrana_ChranUzemi:Velkoplo%C5%A1n%C3%A9_zvl%C3%A1%C5%A1t%C4%9B_chr%C3%A1n%C4%9Bn%C3%A9_%C3%BAzem%C3%AD&srsname=epsg:4326

S prostorovým filtrem (zatím se nepodařilo zprovoznit):
  https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?server=WFS&request=getfeature&typename=UzemniOchrana_ChranUzemi:Velkoplo%C5%A1n%C3%A9_zvl%C3%A1%C5%A1t%C4%9B_chr%C3%A1n%C4%9Bn%C3%A9_%C3%BAzem%C3%AD&srsname=epsg:4326&FILTER=<ogc:Filter><ogc:Within><ogc:PropertyName>SHAPE</ogc:PropertyName><gml:Envelope><gml:lowerCorner>48.4744444 12.7083628</gml:lowerCorner><gml:upperCorner>49.4017450 14.8397106</gml:upperCorner></gml:Envelope></ogc:Within></ogc:Filter>

S atributovým filtrem:

  https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?server=WFS&request=getfeature&typename=UzemniOchrana_ChranUzemi:Velkoplo%C5%A1n%C3%A9_zvl%C3%A1%C5%A1t%C4%9B_chr%C3%A1n%C4%9Bn%C3%A9_%C3%BAzem%C3%AD&srsname=epsg:4326&FILTER=<ogc:Filter><ogc:PropertyIsLike wildCard="%" singleChar="?" escapeChar="!"><ogc:PropertyName>NAZEV</ogc:PropertyName><ogc:Literal>Český kras</ogc:Literal></ogc:PropertyIsLike></ogc:Filter>' 

Vhodný klient - QGIS::
  
  NAZEV LIKE 'Český les'

.. figure:: images/wfs-filter.png
  :width: 600px
