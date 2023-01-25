# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)

class Purchase_order_custom(models.Model):
    _inherit = 'purchase_order_line'
    _description = 'creamos campo l5 y reescribimos funcion'
    
    filed_l5 = fields.Char(string='Campo l5')
