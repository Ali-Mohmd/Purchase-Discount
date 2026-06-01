# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    avoid_global_discount = fields.Boolean(copy=False, default=False)
