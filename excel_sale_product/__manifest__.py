# -*- coding: utf-8 -*-
{
    'name': "Excel sale report",
    'summary': """""",
    'description': """ """,
    'author': "Ronny Montano <<rmontano1992@gmail.com>>",
    'category': 'Accounting',
    'version': '17.0.0.0.1',
    'license': 'LGPL-3',
    'depends': ['base', 'product', 'report_xlsx', 'account'],
    'data': [
        "report/reports_actions.xml",
        "wizard/excel_report_wizard.xml",
        "security/ir.model.access.csv"
    ],
}
