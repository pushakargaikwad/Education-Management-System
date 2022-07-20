# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Education Base',
    'version' : '1.0.1',
    'summary': 'Base module for Education Management System',
    'sequence': 30,
    'description': """
        Student Module
    """,
    'category': 'Education',
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','web'],
    'data': ['security/security.xml','security/ir.model.access.csv','views/menus_view.xml','views/student_view.xml','views/academic_year_view.xml'],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
