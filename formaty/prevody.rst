=====================================
Knihovna GDAL pro převod mezi formáty
=====================================

Programátorská knihovna `GDAL <http://gdal.org>`_ se stará o práci s množstvím
`rastrových <http://gdal.org/formats_list.html>`_ i `vektorových
<http://gdal.org/ogr_formats.html>`_ formátů používaných v GIS. GDAL je využíván
celou řadou dalších programů ja základní knihovna (GRASS GIS, QGIS, ...),
dokonce i v produktu ArcGIS.

.. note:: V dřívějšich verzích byla tato knihovna rozdělena na část GDAL,
    pracující s rastrovými daty a OGR, pracující s vektory. Dnes se však obě
    větve sloučily. Stále však můžete narazit na označení části pro práci s
    vektory jako *OGR*.

Knihovna je šířena s několika binárními konzolovými programy, které můžeme
použít na celou řadu operací. Detailnější práci s knihovnou z pohledu
programátora rozebíráme v části věnované programovacímu jazyku `Python z pohledu
GIS <http://training.gismentors.eu/geopython/>`_.

Příkazy pro práci s rastrovými daty
-----------------------------------

gdalinfo
    Příkaz `gdalinfo` umožňuje zobrazit některá metadat o rastrových souborech

    .. notecmd:: zobrazení metadat z rastrového souboru:
    
        .. code-block:: bash

            gdalinfo lsat7_2002_nir.tiff
            Driver: GTiff/GeoTIFF
            Files: lsat7_2002_nir.tiff
            Size is 1287, 831
            Coordinate System is:
            PROJCS["Lambert Conformal Conic",
                GEOGCS["NAD83",
                    DATUM["North_American_Datum_1983",
                        SPHEROID["GRS 1980",6378137,298.2572221010002,
                            AUTHORITY["EPSG","7019"]],
                        AUTHORITY["EPSG","6269"]],
                    PRIMEM["Greenwich",0],
                    UNIT["degree",0.0174532925199433],
                    AUTHORITY["EPSG","4269"]],
                PROJECTION["Lambert_Conformal_Conic_2SP"],
                PARAMETER["standard_parallel_1",36.16666666666666],
                PARAMETER["standard_parallel_2",34.33333333333334],
                PARAMETER["latitude_of_origin",33.75],
                PARAMETER["central_meridian",-79],
                PARAMETER["false_easting",609601.22],
                PARAMETER["false_northing",0],
                UNIT["metre",1,
                    AUTHORITY["EPSG","9001"]]]
            Origin = (630540.000000000000000,226980.000000000000000)
            Pixel Size = (10.000000000000000,-10.000000000000000)
            Metadata:
              AREA_OR_POINT=Area
            Image Structure Metadata:
              INTERLEAVE=PIXEL
            Corner Coordinates:
            Upper Left  (  630540.000,  226980.000) ( 78d46' 6.04"W, 35d47'45.23"N)
            Lower Left  (  630540.000,  218670.000) ( 78d46' 6.81"W, 35d43'15.59"N)
            Upper Right (  643410.000,  226980.000) ( 78d37'33.46"W, 35d47'43.96"N)
            Lower Right (  643410.000,  218670.000) ( 78d37'34.70"W, 35d43'14.31"N)
            Center      (  636975.000,  222825.000) ( 78d41'50.25"W, 35d45'29.85"N)
            Band 1 Block=1287x1 Type=Float32, ColorInterp=Gray
            Band 2 Block=1287x1 Type=Float32, ColorInterp=Undefined
            Band 3 Block=1287x1 Type=Float32, ColorInterp=Undefined

gdalsrsinfo 
    Pokud vám stačí pouze informace o použité projekci, zjistíte ji pomocí
    příkazu gdalsrsinfo, který vrátí definici souř. systému rastru ve formátu
    Proj4, ale  tzv. well known text (WKT)

    .. notecmd:: zobrazení informace o souř. systému

        .. code-block:: bash

            gdalsrsinfo lsat7_2002_nir.tiff

            PROJ.4 : '+proj=lcc +lat_1=36.16666666666666 +lat_2=34.33333333333334 +lat_0=33.75 +lon_0=-79 +x_0=609601.22 +y_0=0 +datum=NAD83 +units=m +no_defs '

            OGC WKT :
            PROJCS["Lambert Conformal Conic",
                GEOGCS["NAD83",
                    DATUM["North_American_Datum_1983",
                        SPHEROID["GRS 1980",6378137,298.2572221010002,
                            AUTHORITY["EPSG","7019"]],
                        AUTHORITY["EPSG","6269"]],
                    PRIMEM["Greenwich",0],
                    UNIT["degree",0.0174532925199433],
                    AUTHORITY["EPSG","4269"]],
                PROJECTION["Lambert_Conformal_Conic_2SP"],
                PARAMETER["standard_parallel_1",36.16666666666666],
                PARAMETER["standard_parallel_2",34.33333333333334],
                PARAMETER["latitude_of_origin",33.75],
                PARAMETER["central_meridian",-79],
                PARAMETER["false_easting",609601.22],
                PARAMETER["false_northing",0],
                UNIT["metre",1,
                    AUTHORITY["EPSG","9001"]]]
gdalwarp
    TODO
