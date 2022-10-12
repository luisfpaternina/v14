from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    has_credit = fields.Boolean(
        string="Has a current credit",
        related="partner_id.has_credit")
    credit_value = fields.Float(
        string="Credit value",
        related="partner_id.credit_value")
