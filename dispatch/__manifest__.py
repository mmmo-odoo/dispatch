{
    'name' : 'Dispatch Management System',
    'version' : '1.0',
    'author': "Mayank Mangal Mourya",
    'summary' : 'Track Real Time Requirements For Dispatch Management',
    'description' : """
        The Dispatch Management System is designed to streamline and optimize the process of dispatching goods and managing 
        logistics. This system efficiently handles order fulfillment, tracking, and delivery coordination. 
        It encompasses features such as order processing, route optimization, real-time tracking, and communication with drivers. 
        By automating and centralizing these tasks, the Dispatch Management System enhances operational efficiency, 
        reduces errors, and improves overall logistics performance. This system is crucial for businesses involved in 
        transportation, delivery services, and supply chain management, ensuring timely and cost-effective dispatch operations.
    """,
    'depend' : [
        'base'
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/dispatch_property_view.xml',
        'views/dispatch_property_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}