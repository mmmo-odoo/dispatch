{
    'name' : 'Stock Transport',
    'version' : '1.0',
    'license':'LGPL-3',
    'author': "Mayank Mangal Mourya",
    'summary' : 'Track Real Time Requirements Stock Transport and Dispatch Management',
    'description' : """
        The Dispatch Management System is designed to streamline and optimize the process of dispatching goods and managing 
        logistics. This system efficiently handles order fulfillment, tracking, and delivery coordination. 
        It encompasses features such as order processing, route optimization, real-time tracking, and communication with drivers. 
        By automating and centralizing these tasks, the Dispatch Management System enhances operational efficiency, 
        reduces errors, and improves overall logistics performance. This system is crucial for businesses involved in 
        transportation, delivery services, and supply chain management, ensuring timely and cost-effective dispatch operations.
    """,
    'depends' : [
        'fleet',
        'stock_picking_batch',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/inherit_fleet_view.xml',
        'views/inherit_batch_transfer_transfer.xml',
        'views/inherit_batch_transfer_view.xml',
        'views/dispatch_property_doc.xml',
        'views/dispatch_property_view.xml',
        'views/dispatch_property_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
