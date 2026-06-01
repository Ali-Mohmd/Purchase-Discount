# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _get_lang(self):
        self.ensure_one()

        if self.partner_id.lang and not self.partner_id.is_public:
            return self.partner_id.lang

        return self.env.lang

    def action_open_discount_wizard(self):
        self.ensure_one()
        return {
            'name': _("Discount"),
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order.discount',
            'view_mode': 'form',
            'target': 'new',
        }
