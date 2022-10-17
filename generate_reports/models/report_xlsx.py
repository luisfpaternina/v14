# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ReportXlsx(models.AbstractModel):
    _name = 'report.generate_reports.report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        for obj in lines:
            report_name = obj.name
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)