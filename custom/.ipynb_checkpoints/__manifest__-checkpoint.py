# -*- coding: utf-8 -*-
{
    'name': "custom_L5",

    'summary': """
        Módulo CUSTOM L5""",

    'description': """
        Módulo CUSTOM L5...
    """,

    'author': "Israel Ubeda Bravo",
    'website': "https://israelubeda.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherit_purchase_order_line.xml',
        #'views/templates.xml',
        #'reports/visit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
