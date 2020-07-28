# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    @api.model_create_multi
    def create(self, values_list):
        if self.env.user.has_group('vendor_purchase.group_vendor_user') and values_list[0]['subtype_id'] == 2:
            res = super(MailMessage, self.with_user(user=self.env.user).sudo()).create(values_list)
        else:
            res = super(MailMessage, self).create(values_list)
        return res
