# -*- coding: utf-8 -*-
{
    'name': "theme_variant",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_theme_install'],

    # always loaded
    'data': [
        'views/assets.xml',
	'views/opt.xml',
	'views/carousel.xml',
        #'views/view.xml',
    ],
    'application': False,
}
