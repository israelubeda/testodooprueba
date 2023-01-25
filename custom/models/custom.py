# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)

class Purchase_order_custom(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'creamos campo l5 y reescribimos funcion'
    
    filed_l5 = fields.Char(string='Campo l5')
    
    #def _prepare_account_move_line(self, move=False):
        #reescribiendo funcion
        #res = super()._prepare_account_move_line(move=False)
        #field_dato va a pasar hacia la factura
        #res.update(filed_l4=self.filed_l5)
        #de la linea subo a la orden de compra
        #res.update(field_dato=self.order_id.field_l5)
        #return res

    def _prepare_account_move_line(self, move=False):
        #reescribiendo funcion
        res = super()._prepare_account_move_line(move=False)
        #field_dato va a pasar desde la factura
        res.update(filed_l4=self.order_id.filed_l6)
        #de la linea subo a la orden de compra
        #res.update(field_dato=self.order_id.field_l5)
        return res
    
    
    #####################################################

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'
    _description = 'Agrega campo L5 a la Información de Solicitudes de presupuesto'

    habitat_partner_id2 = fields.Many2one(string="L5", related="ht_budget_tr_id.habitat_partner_id")

class Purchase_order_custom(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'creamos campo l5 y reescribimos funcion'

    def _prepare_account_move_line(self, move=False):
        current_uid = self.env.uid
        user = self.env['res.users'].browse(current_uid)
        res = super()._prepare_account_move_line(move)
        res.update({"habitat_partner_id" : self.order_id.habitat_partner_id2,"habitat_branch_id" : user.branch_office_tr_id.id})
        return res 


    
    
    #####################################################
        
        
    
class Factura_compras(models.Model):
    _inherit = 'account.move.line'
    _description = 'creamos campo l5'
    
    filed_l4 = fields.Char(string='Campo l5')
    
class Cabecera_custom(models.Model):
    _inherit = 'purchase.order'
    _description = 'creamos cabezera campo l5 y reescribimos funcion'
    
    filed_l6 = fields.Char(string='Campo cabecera l5')
    
    '''
    def _prepare_account_move_line(self, move=False):
        #reescribiendo funcion
        res = super()._prepare_account_move_line(move=False)
        #field_dato va a pasar desde la factura
        res.update(filed_l4=self.filed_l6)
        #de la linea subo a la orden de compra
        #res.update(field_dato=self.order_id.field_l5)
        return res
       ''' 
