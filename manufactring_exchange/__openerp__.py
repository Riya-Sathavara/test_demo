# -*- coding: utf-8 -*-
{
    'name': "Manufacturing Changing ",

    'summary': """Manufacturing trainings""",

    'description': """
        Starting of the Odooo Developer 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','mrp' , 'demo','sale' ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'templates.xml',
       'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'auto_install': False,

}
