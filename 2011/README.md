Downloaded 23/08/2019 from

Volume 3 - Non ABS Structures
https://www.abs.gov.au/AUSSTATS/abs@.nsf/Lookup/1270.0.55.003Main+Features1July%202011?OpenDocument

Destination Zones
https://www.abs.gov.au/AUSSTATS/abs@.nsf/Lookup/8000.0Main+Features1August%202011?OpenDocument

Volume 1 - Main Structure and Greater Capital City Statistical Areas (Meshblocks)
https://www.abs.gov.au/AUSSTATS/abs@.nsf/Lookup/1270.0.55.001Main+Features1July%202011?OpenDocument

# Comments

LGAs, CEDs, SEDs, and other Non-ABS Structures are loaded as part of the [2011 Census Loader](https://github.com/ealgis/aus-census-2011).

# Mesh Blocks

The individual mesh block shapefiles provided by the ABS were merged into the single shapefile here using `ogr2ogr`.

```
ogr2ogr -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_act_shape/MB_2011_ACT.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_nt_shape/MB_2011_NT.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_nsw_shape/MB_2011_NSW.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_ot_shape/MB_2011_OT.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_qld_shape/MB_2011_QLD.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_sa_shape/MB_2011_SA.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_tas_shape/MB_2011_TAS.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_vic_shape/MB_2011_VIC.shp -nlt PROMOTE_TO_MULTI

ogr2ogr -update -append -f "ESRI Shapefile" /app/2011/MB_2011.shp /app/2011/mb/1270055001_mb_2011_wa_shape/MB_2011_WA.shp -nlt PROMOTE_TO_MULTI
```
