# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words


class Num2WordsCZTest(TestCase):
    def test_cardinal(self):
        self.assertEqual(num2words(1, lang='cz', case='nominative', gender='f'), "jedna")
        self.assertEqual(num2words(1, lang='cz', case='nominative'), "jeden")
        self.assertEqual(num2words(1, lang='cz', case='genitive'), "jednoho")
        self.assertEqual(num2words(1, lang='cz', case='dative'), "jednomu")
        self.assertEqual(num2words(1, lang='cz', case='accusative'), "jednoho")
        self.assertEqual(num2words(1, lang='cz', case='locative'), "jednom")
        self.assertEqual(num2words(1, lang='cz', case='instrumental'), "jedním")
        self.assertEqual(num2words(100, lang='cz'), "sto")
        self.assertEqual(num2words(101, lang='cz'), "sto jedna")
        self.assertEqual(num2words(101, lang='cz', gender='f'), "sto jedna")
        self.assertEqual(num2words(110, lang='cz'), "sto deset")
        self.assertEqual(num2words(115, lang='cz'), "sto patnáct")
        self.assertEqual(num2words(123, lang='cz'), "sto dvacet tři")
        self.assertEqual(num2words(1000, lang='cz'), "tisíc")
        self.assertEqual(num2words(1001, lang='cz'), "tisíc jedna")
        self.assertEqual(num2words(1001, lang='cz', gender='f'), "tisíc jedna")
        self.assertEqual(num2words(1001, lang='cz', gender='n'), "tisíc jedna")
        self.assertEqual(num2words(2012, lang='cz'), "dva tisíce dvanáct")
        self.assertEqual(num2words(2758, lang='cz', case='genitive'), "dvou tisíc sedmi set padesáti osmi")
        self.assertEqual(num2words(21001, lang='cz'), "dvacet jedna tisíc jedna")
        self.assertEqual(num2words(21001, lang='cz', gender='f'), "dvacet jedna tisíc jedna")
        self.assertEqual(num2words(41, lang='cz', case='genitive'), "čtyřiceti jednoho")
        self.assertEqual(num2words(50, lang='cz', case='nominative'), "padesát")
        self.assertEqual(num2words(50, lang='cz', case='genitive'), "padesáti")
        self.assertEqual(num2words(50, lang='cz', case='dative'), "padesáti")
        self.assertEqual(num2words(50, lang='cz', case='accusative'), "padesát")
        self.assertEqual(num2words(51, lang='cz', case='nominative'), "padesát jedna")
        self.assertEqual(num2words(51, lang='cz', case='genitive'), "padesáti jednoho")
        self.assertEqual(num2words(51, lang='cz', case='dative'), "padesáti jednomu")
        self.assertEqual(num2words(51, lang='cz', case='accusative'), "padesát jedna")
        self.assertEqual(num2words(52, lang='cz', case='nominative'), "padesát dva")
        self.assertEqual(num2words(52, lang='cz', case='genitive'), "padesáti dvou")
        self.assertEqual(num2words(52, lang='cz', case='genitive', gender='f'), "padesáti dvou")
        self.assertEqual(num2words(52, lang='cz', case='dative'), "padesáti dvěma")
        self.assertEqual(num2words(52, lang='cz', case='accusative'), "padesát dva")
        self.assertEqual(num2words(53, lang='cz', case='nominative'), "padesát tři")
        self.assertEqual(num2words(53, lang='cz', case='genitive'), "padesáti tří")
        self.assertEqual(num2words(53, lang='cz', case='dative'), "padesáti třem")
        self.assertEqual(num2words(53, lang='cz', case='accusative'), "padesát tři")
        self.assertEqual(num2words(58, lang='cz', case='nominative'), "padesát osm")
        self.assertEqual(num2words(58, lang='cz', case='genitive'), "padesáti osmi")
        self.assertEqual(num2words(58, lang='cz', case='dative'), "padesáti osmi")
        self.assertEqual(num2words(58, lang='cz', case='accusative'), "padesát osm")
        self.assertEqual(num2words(58, lang='cz', case='locative'), "padesáti osmi")
        self.assertEqual(num2words(58, lang='cz', case='instrumental'), "padesáti osmi")
        self.assertEqual(num2words(74, lang='cz', case='genitive'), "sedmdesáti čtyř")
        self.assertEqual(
            num2words(1.2, lang='cz'),
            "jedna celá dva"
        )
        self.assertEqual(
            num2words(2.16, lang='cz'),
            "dva celá šestnáct" # TODO sklonovat celá? nebo napevno dva celá šestnáct ?
        )
        self.assertEqual(
            num2words(10.02, lang='cz'),
            "deset celá nula dva"
        )
        self.assertEqual(
            num2words(15.007, lang='cz'),
            "patnáct celá nula nula sedm"
        )
        self.assertEqual(
            num2words(12519.85, lang='cz'),
            "dvanáct tisíc pět set devatenáct celá osmdesát pět"
        )
        self.assertEqual(
            num2words(123.50, lang='cz'),
            "sto dvacet tři celá pět"
        )
        self.assertEqual(
            num2words(1234567890, lang='cz'),
            "miliarda dvě stě třicet čtyři miliony pět set šedesát "
            "sedm tisíc osm set devadesát"
        )
        self.assertEqual(
            num2words(215461407892039002157189883901676, lang='cz'),
            "dvě stě patnáct quintillionů čtyři sta šedesát jedna kvadriliard "
            "čtyři sta sedm kvadrilionů osm set devadesát dva triliardy třicet "
            "devět trilionů dva biliardy sto padesát sedm bilionů sto "
            "osmdesát devět miliard osm set osmdesát tři miliony "
            "devět set jedna tisíc šest set sedmdesát šest"
        )
        self.assertEqual(
            num2words(719094234693663034822824384220291, lang='cz'),
            "sedm set devatenáct quintillionů devadesát "
            "čtyři kvadriliardy dvě stě třicet čtyři "
            "kvadriliony šest set devadesát tři triliardy "
            "šest set šedesát tři triliony třicet čtyři biliardy osm set "
            "dvacet dva biliony osm set dvacet čtyři "
            "miliardy tři sta osmdesát čtyři miliony dvě stě dvacet "
            "tisíc dvě stě devadesát jedna"
        )

    def test_to_ordinal(self):
        # @TODO: implement to_ordinal
        with self.assertRaises(NotImplementedError):
            num2words(1, lang='cz', to='ordinal')

    def test_currency(self):
        self.assertEqual(
            num2words(10.0, lang='cz', to='currency', currency='EUR'),
            "deset euro, nula centů")
        self.assertEqual(
            num2words(1.0, lang='cz', to='currency', currency='CZK'),
            "jedna koruna, nula haléřů")
        self.assertEqual(
            num2words(1234.56, lang='cz', to='currency', currency='EUR'),
            "tisíc dvě stě třicet čtyři euro, padesát šest centů")
        self.assertEqual(
            num2words(1234.56, lang='cz', to='currency', currency='CZK'),
            "tisíc dvě stě třicet čtyři koruny, padesát šest haléřů")
        self.assertEqual(
            num2words(101.11, lang='cz', to='currency', currency='EUR',
                      separator=' a'),
            "sto jedna euro a jedenáct centů")
        self.assertEqual(
            num2words(101.21, lang='cz', to='currency', currency='CZK',
                      separator=' a'),
            "sto jedna korun a dvacet jedna haléřů"
        )
        self.assertEqual(
            num2words(-12519.85, lang='cz', to='currency', cents=False),
            "mínus dvanáct tisíc pět set devatenáct euro, 85 centů"
        )
        self.assertEqual(
            num2words(123.50, lang='cz', to='currency', currency='CZK',
                      separator=' a'),
            "sto dvacet tři koruny a padesát haléřů"
        )
        self.assertEqual(
            num2words(19.50, lang='cz', to='currency', cents=False),
            "devatenáct euro, 50 centů"
        )
