# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Lead to Issue',
    'summary': 'Create Issues from Leads',
    'sequence': '19',
    'category': 'Project Management',
    'complexity': 'easy',
    'description': """
Lead to Issues
==============

Link module to map leads to issues
        """,
    'data': [
        'wizard/crm_lead2projectissue_wizard_view.xml',
        'views/crm_lead_views.xml'
    ],
    'depends': ['crm', 'project_issue'],
}
