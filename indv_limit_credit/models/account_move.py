from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    has_credit = fields.Boolean(
        string="Has a current credit",
        related="partner_id.has_credit")
