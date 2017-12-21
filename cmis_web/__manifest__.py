# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "CMIS Web interface",
    'summary': """
        Embeddable CMIS Web components""",
    'author': 'ACSONE SA/NV',
    'website': "http://alfodoo.org/",
    'version': '10.0.2.0.0',
    'license': 'AGPL-3',
    'price': 500,
    'currency': 'EUR',
    'depends': [
        'web',
        'cmis_field',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'data': [
        'views/cmis_web.xml',
    ],
}
