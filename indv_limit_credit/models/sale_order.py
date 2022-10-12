from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_credit = fields.Boolean(
        string="Has a current credit",
        related="partner_id.has_credit")
    credit_value = fields.Float(
        string="Credit value",
        related="partner_id.credit_value")
