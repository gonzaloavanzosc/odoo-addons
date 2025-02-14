# Copyright 2022 Leire Martinez de Santos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Website Payment Method Custom",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    'category': 'website',
    'version': '14.0.1.0.0',
    'depends': [
        'website_bank_account',
        'payment_acquirer_payment_mode'
    ],
    'data': [
        'security/res_partner_bank_security.xml',
        'views/templates.xml',
    ]
}
