# -*- coding: utf-8 -*-
{
    'name': "Vendor User Group",

    'summary': """Vendor User Group for internal users""",

    'description': """
        [2240762]
        """,

    'author': 'Odoo',
    'website': 'https://www.odoo.com/',

    'category': 'Custom Development',
    'version': '1.0',
    'license': 'OEEL-1',

    # any module necessary for this one to work correctly
    'depends': ['purchase', 'stock'],

    # always loaded
    'data': [
        'security/vendor_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_views.xml',
        'views/product_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'application': False,
}
