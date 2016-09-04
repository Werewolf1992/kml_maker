# -*- coding: utf-8 -*-
import pandas
import geocoder
from pykml.factory import KML_ElementMaker as KML
from lxml import etree


class engine(object):

    def handle_uploaded_file(self, file):
        dicts = []
        excel = pandas.read_excel(file, parse_cols="I:L", header=0)
        for index, row in excel.iterrows():
            print row
            storedict = {
                'city': row[str('Miejscowosc')],
                'voivodeship': row[str('Wojewodztwo')],
                'county': row[str('Powiat')],
                'commune': row[str('Gmina')],
                'latitude': 0,
                'longitude': 0,
            }
            g = geocoder.google(row[str('Miejscowosc')])
            print g.latlng
            storedict['latitude'] = g.latlng[0]
            storedict['longitude'] = g.latlng[1]
            dicts.append(storedict)
        return dicts

    def kml_maker(self, dicts):

        fid = KML.Folder()
        for row in dicts:

            pm1 = KML.Placemark(
                # row[str('Wojewodztwo')] +
                #              KML.name(unicode(row[str('Miejscowosc')],'utf-8')),
                KML.name('Szczecin'),
                KML.Point(
                    KML.coordinates([row.latitude, row.longitude])
                )
            )
            fid.append(pm1)
        # print g.latlng
        #     print row[str('Wojewodztwo')], row[str('Miejscowosc')]
        etree.tostring(fid)
        print etree.tostring(fid, pretty_print=True)
        return etree.tostring(fid)