# -*- coding: utf-8 -*-
{
    'name': "ejercicio2_Odoo",

    'summary': """
        Esta aplicacion esta realiza por Alejandro Moles Hurtado""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alejandro Moles Hurtado",
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
        'security/cliente_security.xml',
        'security/ejercicio2__odoo_security.xml',
        'security/pedido_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/ejercicio2__odoo_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/demo_cliente.xml',
        'demo/demo_pedido.xml',
    ],
}
