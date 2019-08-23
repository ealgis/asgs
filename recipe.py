#
# EAlGIS loader: ASGS boundaries
#

from ealgis_common.db import DataLoaderFactory
from ealgis_common.util import make_logger
from ealgis_common.loaders import ZipAccess, ShapeLoader, MapInfoLoader, KMLLoader, GeoPackageLoader
from datetime import datetime
import os.path


logger = make_logger(__name__)


def one(l):
    if len(l) == 0:
        raise Exception('one(): zero entries')
    elif len(l) > 1:
        raise Exception('one(): more than one entry (%s)' % repr(l))
    return l[0]


def load_shapes(factory, basedir, tmpdir):
    def load_mapinfo(table_name, filename):
        with ZipAccess(None, tmpdir, filename) as z:
            mipath = z.getdir() + '/'
            logger.debug([tmpdir, filename, mipath])
            instance = MapInfoLoader(loader.dbschema(), mipath, table_name=table_name)
            instance.load(loader)

    def load_shapefile(table_name, filename, srid):
        with ZipAccess(None, tmpdir, filename) as z:
            shpfile = one(z.glob('*.shp'))
            instance = ShapeLoader(loader.dbschema(), shpfile, srid, table_name=table_name)
            instance.load(loader)

    def load_kml(table_name, filename):
        instance = KMLLoader(loader.dbschema(), filename, table_name=table_name)
        instance.load(loader)

    def load_geopackage(table_name, filename, layer_name):
        with ZipAccess(None, tmpdir, filename) as z:
            gpkgfile = one(z.glob('*.gpkg'))
            instance = GeoPackageLoader(loader.dbschema(), gpkgfile, layer_name, table_name=table_name)
            instance.load(loader)

    GDA94 = 4283
    shapes = {
        ('asgs_2019_boundaries', 'ASGS 2019 Boundaries'): [
            ('asgs_2019_lga', 'Local Government Areas 2019', '2019/1270055003_asgs_2019_vol_3_aust_gpkg.zip', load_geopackage, ('LGA_2019_AUST',)),
        ],
        ('asgs_2018_boundaries', 'ASGS 2018 Boundaries'): [
            ('asgs_2018_lga', 'Local Government Areas 2018', '2018/1270055003_asgs_2018_vol_3_aust_gpkg.zip', load_geopackage, ('LGA_2018_AUST',)),
            ('asgs_2018_ced', 'Commonwealth Electoral Divisions 2018', '2018/1270055003_asgs_2018_vol_3_aust_gpkg.zip', load_geopackage, ('CED_2018_AUST',)),
            ('asgs_2018_sed', 'State Electoral Divisions ASGS 2018', '2018/1270055003_asgs_2018_vol_3_aust_gpkg.zip', load_geopackage, ('SED_2018_AUST',)),
        ],
        ('asgs_2017_boundaries', 'ASGS 2017 Boundaries'): [
            ('asgs_2017_lga', 'Local Government Areas 2017', '2017/1270055003_asgs_2017_vol_3_aust_gpkg.zip', load_geopackage, ('LGA_2017_AUST',)),
            ('asgs_2017_ced', 'Commonwealth Electoral Divisions 2017', '2017/1270055003_asgs_2017_vol_3_aust_gpkg.zip', load_geopackage, ('CED_2017_AUST',)),
            ('asgs_2017_sed', 'State Electoral Divisions ASGS 2017', '2017/1270055003_asgs_2017_vol_3_aust_gpkg.zip', load_geopackage, ('SED_2017_AUST',)),
        ],
        ('asgs_2016_boundaries', 'ASGS 2016 Boundaries'): [
            ('asgs_2016_add', 'Australian Drainage Divisions 2016', '2016/1270055003_asgs_2016_vol_3_aust_gpkg.zip', load_geopackage, ('ADD_2016_AUST',)),
            ('asgs_2016_nrmr', 'Natural Resource Management Regions 2016', '2016/1270055003_asgs_2016_vol_3_aust_gpkg.zip', load_geopackage, ('NRMR_2016_AUST',)),
            ('asgs_2016_tr', 'Tourism Regions 2016', '2016/1270055003_asgs_2016_vol_3_aust_gpkg.zip', load_geopackage, ('TR_2016_AUST',)),
            ('asgs_2016_dzn', 'Destination Zones 2016', '2016/80000_dzn_2016_aust_geopackage.zip', load_geopackage, ('DZN_2016_AUST',)),
            ('asgs_2016_mb', 'Mesh Blocks 2016', '2016/1270055001_ASGS_2016_vol_1_geopackage.zip', load_geopackage, ('MB_2016_AUST',)),
        ],
        ('asgs_2015_boundaries', 'ASGS 2015 Boundaries'): [
            ('asgs_2015_lga', 'Local Government Areas 2015', '2015/1270055003_lga_2015_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2015_tr', 'Tourism Regions 2015', '2015/1270055003_tr_2015_aust_shape.zip', load_shapefile, (GDA94,)),
        ],
        ('asgs_2014_boundaries', 'ASGS 2014 Boundaries'): [
            ('asgs_2014_lga', 'Local Government Areas 2014', '2014/1270055003_lga_2014_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2014_tr', 'Tourism Regions 2014', '2014/1270055003_tr_2014_aust_shape.zip', load_shapefile, (GDA94,)),
        ],
        ('asgs_2013_boundaries', 'ASGS 2013 Boundaries'): [
            ('asgs_2013_lga', 'Local Government Areas 2013', '2013/1270055003_lga_2013_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2013_tr', 'Tourism Regions 2013', '2013/1270055003_tr_2013_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2013_ced', 'Commonwealth Electoral Divisions 2013', '2013/1270055003_ced_2013_aust_shp.zip', load_shapefile, (GDA94,)),
        ],
        ('asgs_2012_boundaries', 'ASGS 2012 Boundaries'): [
            ('asgs_2012_lga', 'Local Government Areas 2012', '2012/1270055003_lga_2012_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2012_tr', 'Tourism Regions 2012', '2012/1270055003_tr_2012_aust_shape.zip', load_shapefile, (GDA94,)),
        ],
        ('asgs_2011_boundaries', 'ASGS 2011 Boundaries'): [
            ('asgs_2011_add', 'Australian Drainage Divisions 2011', '2011/1270055003_add_2011_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2011_nrmr', 'Natural Resource Management Regions 2011', '2011/1270055003_nrmr_2011_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2011_tr', 'Tourism Regions 2011', '2011/1270055003_tr_2011_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2011_dzn', 'Destination Zones 2011', '2011/80000_dzn_2011_aust_shape.zip', load_shapefile, (GDA94,)),
            ('asgs_2011_mb', 'Mesh Blocks 2011', '2011/1270055001_mb_2011_shape.zip', load_shapefile, (GDA94,)),
        ],
    }

    results = []
    for (schema_name, schema_description), to_load in shapes.items():
        with factory.make_loader(schema_name, mandatory_srids=[3112, 3857]) as loader:
            loader.set_metadata(
                name=schema_description,
                family="Australian Statistical Geography Standard Boundaries",
                date_published=datetime(2019, 8, 23, 0, 0, 0),  # Set in UTC
                description='Collected geometries from the ABS\'s ASGS')
            loader.session.commit()
            for table_name, description, zip_path, loader_fn, loader_args in to_load:
                loader_fn(table_name, os.path.join(basedir, zip_path), *loader_args)
                loader.set_table_metadata(table_name, {'description': description})
            results.append(loader.result())
    return results


def main():
    tmpdir = "/app/tmp"
    basedir = '/app/'
    factory = DataLoaderFactory(db_name="ealgis", clean=False)
    shape_results = load_shapes(factory, basedir, tmpdir)
    for result in shape_results:
        result.dump(tmpdir)


if __name__ == '__main__':
    main()
