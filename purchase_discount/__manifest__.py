{
    'name': "Purchase Discount",
    'summary': """Apply Global, Fixed Amount and Line Discounts on Purchase Orders""",
    'description': """Purchase Discount Management for Odoo Purchase Orders'""",
    'version': '17.0.1.0.0',
    'author': 'Ali Mohamed',
    'category': 'Purchase',
    'license': 'LGPL-3',
    'price': 20,   
    'currency': 'USD',
    'images': [
        'static/description/icon.png',
    ],
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/purchase_order_views.xml',
        'wizard/purchase_order_discount_views.xml',
    ],
    'installable': True,
    'application': False,
}
