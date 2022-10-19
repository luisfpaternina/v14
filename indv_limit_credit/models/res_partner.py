# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    has_credit = fields.Boolean(
        string="Has a current credit",
        compute="compute_has_a_credit")
    credit_value = fields.Float(
        string="Credit value",
        compute="compute_has_a_credit")
    new_vat = fields.Char(
        string="New vat")
    validate_vat = fields.Boolean(
        string="Validator VAT")


    def compute_has_a_credit(self):
        for record in self:
            credit_obj = record.env['credit.limit'].search([
                ('partner_id', '=', record.id),
                ('state', '=', 'approved')], limit=1)
            if credit_obj:
                record.has_credit = True
                record.credit_value = credit_obj.credit_amount
            else:
                record.has_credit = False
                record.credit_value = 0

    @api.depends('vat','name')
    def _compute_new_vat(self):
        for record in self:
            if record.vat:
                record.new_vat = record.vat
            else:
                record.new_vat = False

    @api.constrains('vat','name')
    def records_partners(self):
        exis_records = []
        for record in self:
            if record.vat:
                if record.vat not in exis_records:
                    raise ValidationError('No se puede modificar el vat del contacto')
                exis_records.append(record.vat)
