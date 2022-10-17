# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ReportXlsx(models.AbstractModel):
    _name = 'report.generate_reports.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, partners):
        # reporte
        format1 = workbook.add_format({'font-size': 14, 'align': 'vcenter', 'bold': True})
        sheet = workbook.add_worksheet('reporte lfpv')
        sheet.write(2, 2, 'Name', format1)
