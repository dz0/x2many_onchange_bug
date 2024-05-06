# ,
{
    'name': 'Your Module Name',
    'version': '1.0',
    'category': 'Category',
    'summary': 'Module Summary',
    'description': """
        Module Description
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['tms_base', 'web'],
    'data': [
        "bug_view.xml",
        'ir.model.access.csv',
        # Add other data files here
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
