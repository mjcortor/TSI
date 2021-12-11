# -*- coding: utf-8 -*-
{
    'name': "municitic",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purposekkkkkkkk
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/trabajadores_report.xml',
        'views/incidencias_views.xml',
        'views/citas_views.xml',
        'views/usuarios_views.xml',
        'views/valoraciones_views.xml',
        'views/trabajadores_views.xml',
        'views/comunicados_views.xml',
        'views/tipotrabajador_views.xml',
        'views/cursos_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
