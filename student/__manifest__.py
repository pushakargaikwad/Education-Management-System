# See LICENSE file for full copyright and licensing details.

{
    'name' : 'Student Module',
    'version' : '1.0.0',
    'summary': 'Student Module',
    'sequence': 30,
    'description': """
        Student Module
    """,
    'category': 'Education',
    'website': 'https://pushakar.com/odoo-development/',
    'depends' : ['base','web'],
    'data': ['security/security.xml','security/ir.model.access.csv','views/student_view.xml'],
    'demo': [],
    'qweb': [ ],
    'author': 'Pushakar Gaikwad',
    'license':'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
