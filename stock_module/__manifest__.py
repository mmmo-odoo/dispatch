{
    'name' : 'Stock Module Modifier',
    'version' : '1.0',
    'license':'LGPL-3',
    'author': "Mayank Mangal Mourya",
    'summary' : 'Modify the stock module',
    'description' : """
        Modify the stock module.
    """,
    'depends' : [
        'stock',
    ],
    'data' : [
        'views/inherit_stock_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
