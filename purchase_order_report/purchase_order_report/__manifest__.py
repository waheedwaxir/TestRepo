# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Report",

    'summary': """
         Purpose of the module is to modify the layout and added some new fields in OP""",
    'author': "Waheed",
    'website': "https://www.xydata.com",
    'version': '15.1',
    'depends': ['base','purchase'],
    'data': [
        'views/views.xml',
        'report/inherit_purchase_report_header.xml',
        'report/inherit_purchase_report_temp.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
