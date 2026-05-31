# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'
    _check_company_auto = True

    purchase_discount_product_id = fields.Many2one(
        comodel_name='product.product',
        string="Purchase Discount Product",
        domain=[
            ('type', '=', 'service'),
            ('invoice_policy', '=', 'delivery'),
        ],
        help="Default product used for discounts",
        check_company=True,
    )
