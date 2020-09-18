# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    partner_id = fields.Many2one('res.partner', string='Vendor', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")


class ProductProduct(models.Model):
    _inherit = "product.product"

    partner_id = fields.Many2one('res.partner', string='Vendor', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
