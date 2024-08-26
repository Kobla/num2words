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

from .base import Num2Word_Base
from .utils import get_digits, splitbyx

ZERO = ('nula',)

NAME_TO_CASE = {
    "nominative": 0,
    "genitive": 1,
    "dative": 2,
    "accusative": 3,
    "vocative": -1, # not implemented
    "locative": 4,
    "instrumental": 5,
}

GENDER = ('m_inanimate', 'm_animate', 'f', 'n')

ONES_FEMININE = {
    1: ('jedna', 'jedné', 'jedné', 'jednu', 'jedné', 'jednou'),
    2: ('dvě', 'dvou', 'dvěma', 'dvě', 'dvou', 'dvěma'),
}

ONES_NEUTER = {
    1: ('jedno', 'jednoho', 'jednomu', 'jedno', 'jednom', 'jedním'),
    2: ('dvě', 'dvou', 'dvěma', 'dvě', 'dvou', 'dvěma'),
}

ONES = { # musculine
    1: ('jeden', 'jednoho', 'jednomu', 'jednoho', 'jednom', 'jedním'),
    2: ('dva', 'dvou', 'dvěma', 'dva', 'dvou', 'dvěma'),
    3: ('tři', 'tří', 'třem', 'tři', 'třech', 'třemi'),
    4: ('čtyři', 'čtyř', 'čtyřem', 'čtyři', 'čtyřech', 'čtyřmi'),
    5: ('pět',),
    6: ('šest',),
    7: ('sedm',),
    8: ('osm',),
    9: ('devět',),
}

TENS = {
    0: ('deset',),
    1: ('jedenáct',),
    2: ('dvanáct',),
    3: ('třináct',),
    4: ('čtrnáct',),
    5: ('patnáct',),
    6: ('šestnáct',),
    7: ('sedmnáct',),
    8: ('osmnáct',),
    9: ('devatenáct',),
}

TWENTIES = {
    2: ('dvacet',),
    3: ('třicet',),
    4: ('čtyřicet',),
    5: ('padesát',),
    6: ('šedesát',),
    7: ('sedmdesát',),
    8: ('osmdesát',),
    9: ('devadesát',),
}

HUNDREDS = {
    1: ('sto', 'sta', 'stům', 'sto,', 'stech', 'stem'),
    2: ('dvě stě', 'dvou set', 'dvěma stům', 'dvě stě', 'dvou stech', 'dvěma sty'),
    3: ('tři sta', 'tří set', 'třem stům', 'tři sta', 'třech stech', 'třemi sty'),
    4: ('čtyři sta', 'čtyři sta', 'čtyřem stům', 'čtyři sta', 'čtyřech stech', 'čtyřmi sty'),
    5: ('pět set', 'pěti set', 'pěti stům', 'pět set', 'pěti stech', 'pěti sty'),
    6: ('šest set', 'šesti set', 'šesti stům', 'šest set', 'šesti stech', 'šesti sty'),
    7: ('sedm set', 'sedmi set', 'sedmi stům', 'sedm set', 'sedmi stech', 'sedmi sty'),
    8: ('osm set', 'osmi set', 'osmi stům', 'osm set', 'osmi stech', 'osmi sty'),
    9: ('devět set', 'devíti set', 'devíti stům', 'devět set', 'devíti stech', 'devíti sty'),
}

THOUSANDS = {
    # 10^3
    1: (('tisíc', 'tisíce', 'tisíc'),
        ('tisíce', 'tisíc', 'tisíců'),
        ('tisíci', 'tisícům', 'tisícům'),
        ('tisíc', 'tisíce', 'tisíc'),
        ('tisíci', 'tisících', 'tisících'),
        ('tisícem', 'tisíci', 'tisíci'),),
    # 10^6
    2: (('milion', 'miliony', 'milionů'),
        ('milionu', 'milionů', 'milionů'),
        ('milionu', 'milionům', 'milionům'),
        ('milion', 'miliony', 'milionů'),
        ('milionu', 'milionech', 'milionech'),
        ('miliónem', 'miliony', 'miliony'),),
    # 10^9
    3: (('miliarda', 'miliardy', 'miliard'),
        ('miliardy', 'miliard', 'miliard'),
        ('miliardě', 'miliardám', 'miliardám'),
        ('miliarda', 'miliardy', 'miliard'),
        ('miliardě', 'miliardách', 'miliardách'),
        ('miliardou', 'miliardami', 'miliardami'),),
    # 10^12
    4: (('bilion', 'biliony', 'bilionů'),
        ('bilionu', 'bilionů', 'bilionů'),
        ('bilionu', 'bilionům', 'bilionům'),
        ('bilion', 'biliony', 'bilionů'),
        ('bilionu', 'bilionech', 'bilionech'),
        ('biliónem', 'biliony', 'biliony'),),
    # 10^15
    5: (('biliarda', 'biliardy', 'biliard'),
        ('biliardy', 'biliard', 'biliard'),
        ('biliardě', 'biliardám', 'biliardám'),
        ('biliarda', 'biliardy', 'biliard'),
        ('biliardě', 'biliardách', 'biliardách'),
        ('biliardou', 'biliardami', 'biliardami'),),
    # 10^18
    6: (('trilion', 'triliony', 'trilionů'),
        ('trilionu', 'trilionů', 'trilionů'),
        ('trilionu', 'trilionům', 'trilionům'),
        ('trilion', 'triliony', 'trilionů'),
        ('trilionu', 'trilionech', 'trilionech'),
        ('triliónem', 'triliony', 'triliony'),),
    # 10^21
    7: (('triliarda', 'triliardy', 'triliard'),
        ('triliardy', 'triliard', 'triliard'),
        ('triliardě', 'triliardám', 'triliardám'),
        ('triliarda', 'triliardy', 'triliard'),
        ('triliardě', 'triliardách', 'triliardách'),
        ('triliardou', 'triliardami', 'triliardami'),),
    # 10^24
    8: (('kvadrilion', 'kvadriliony', 'kvadrilionů'),
        ('kvadrilionu', 'kvadrilionů', 'kvadrilionů'),
        ('kvadrilionu', 'kvadrilionům', 'kvadrilionům'),
        ('kvadrilion', 'kvadriliony', 'kvadrilionů'),
        ('kvadrilionu', 'kvadrilionech', 'kvadrilionech'),
        ('kvadriliónem', 'kvadriliony', 'kvadriliony'),),
    # 10^27
    9: (('kvadriliarda', 'kvadriliardy', 'kvadriliard'),
        ('kvadriliardy', 'kvadriliard', 'kvadriliard'),
        ('kvadriliardě', 'kvadriliardám', 'kvadriliardám'),
        ('kvadriliarda', 'kvadriliardy', 'kvadriliard'),
        ('kvadriliardě', 'kvadriliardách', 'kvadriliardách'),
        ('kvadriliardou', 'kvadriliardami', 'kvadriliardami'),),
    # 10^30
    10: (('quintillion', 'quintilliony', 'quintillionů'),
         ('quintillionu', 'quintillionů', 'quintillionů'),
         ('quintillionu', 'quintillionům', 'quintillionům'),
         ('quintillion', 'quintilliony', 'quintillionů'),
         ('quintillionu', 'quintillionech', 'quintillionech'),
         ('quintillionem', 'quintilliony', 'quintilliony'),),
}


class Num2Word_CZ(Num2Word_Base):
    CURRENCY_FORMS = {
        'CZK': (
            ('koruna', 'koruny', 'korun'), ('halíř', 'halíře', 'haléřů')
        ),
        'EUR': (
            ('euro', 'euro', 'euro'), ('cent', 'centy', 'centů')
        ),
    }

    def setup(self):
        self.negword = "mínus"
        self.pointword = "celá"

    def to_cardinal(self, number, gender="m_inanimate", case="nominative"):
        """Convert number to cardinal numeral.
        Args:
            number: Number to convert.
            gender: Gender of the numberal (see self._int2word() for
                supported values).
            case: Grammatical case of the numeral (see self._int2word()
                for supported values).
        Returns:
            Converted number.
        """
        case_number = NAME_TO_CASE[case]
        if gender not in GENDER:
            raise ValueError("gender must be 'm_inanimate', 'm_animate', 'f' or 'n'")

        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            leading_zero_count = len(right) - len(right.lstrip('0'))
            decimal_part = ((ZERO[0] + ' ') * leading_zero_count +
                            self._int2word(int(right), 'm_inanimate', case_number))
            return u'%s %s %s' % (
                self._int2word(int(left), 'f' if left == '1' else 'm_inanimate', case_number),
                self.pointword,
                decimal_part
            )
        else:
            return self._int2word(int(n), gender, case_number)

    def pluralize(self, n, forms):
        if n == 1:
            form = 0
        elif 5 > n % 10 > 1 and (n % 100 < 10 or n % 100 > 20):
            form = 1
        else:
            form = 2
        return forms[form]

    def to_ordinal(self, number):
        raise NotImplementedError()

    def _add_suffix_for_5_to_99(self, place_value, n, case=0):
        word = place_value[n][0]
        if case != 0 and case != 3:
            word = f"{word}i"
        return word

    def _money_verbose(self, number, currency):
        if currency == 'CZK':
            return self._int2word(number, gender='f')
        elif currency == 'EUR':
            return self._int2word(number, gender='n')
        return self._int2word(number, gender='m')

    def _cents_verbose(self, number, currency):
        return self._int2word(number, gender='f')

    def _int2word(self, n, gender='m_inanimate', case: int=0):
        """Convert integer `n` to word.
        Args:
            n: Number to convert.
            gender:  Use "f" for feminine, "n" for neuter, any other value defaults to the masculine inanimate.
            case: Currently supports:
                 0 (nominative)
                 1 (genitive)
                 2 (dative)
                 3 (accusative)
                 4 (locative)
                 5 (instrumental)
        Returns:
            Converted number.
        """
        if case not in {0, 1, 2, 3, 4, 5}:
            raise NotImplementedError()
        if gender == 'f':
            gender_index = 1
        elif gender in {'m_animate', 'm_inanimate', 'n'}:
            gender_index = 0
        else:
            raise NotImplementedError()

        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0: # hundreds
                words.append(HUNDREDS[n3][case])

            if n2 > 1: # 20 .. 90
                words.append(self._add_suffix_for_5_to_99(TWENTIES, n2, case))

            if n2 == 1: # 10 .. 19
                words.append(self._add_suffix_for_5_to_99(TENS, n1, case))
            elif n1 > 0 and not (i > 0 and x == 1):
                if n1 == 1 and n != 1 and case in [0, 3]: # X1, ... always in femine
                    words.append(ONES_FEMININE[n1][0]) # accusative -> nominative
                elif n1 == 1 or n1 == 2: # 1, 2
                    if gender == 'f':
                        words.append(ONES_FEMININE[n1][case])
                    elif gender == 'n':
                        words.append(ONES_NEUTER[n1][case])
                    else: # masculine
                        words.append(ONES[n1][case])
                elif n1 == 3 or n1 == 4: # 3, 4
                    words.append(ONES[n1][case])
                else: # 5 .. 9
                    words.append(self._add_suffix_for_5_to_99(ONES, n1, case))

            if i > 0:
                thousands_val = THOUSANDS[i][case]
                words.append(self.pluralize(x, thousands_val))

        return ' '.join(words)
