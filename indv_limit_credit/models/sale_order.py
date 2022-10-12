from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    has_credit = fields.Boolean(
        string="Has a current credit")
