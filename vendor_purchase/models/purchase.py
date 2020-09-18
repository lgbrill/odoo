# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _compute_if_vendor(self):
        if self.env.user.has_group('vendor_purchase.group_vendor_user'):
            self.is_vendor = True
        else:
            self.is_vendor = False

    is_vendor = fields.Boolean(compute='_compute_if_vendor', string='Logged in user is a vendor')
