# Copyright 2022 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    custom_date_done = fields.Datetime(string='Date realized')
