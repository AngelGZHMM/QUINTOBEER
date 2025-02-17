# -*- coding: utf-8 -*-
# Angel Gallego Zayas

from odoo import models,fields,api

class envio(models.Model) :
    _name='quintobeer.envio'
    _description = 'Un envio'
    _rec_name = 'envio_id'
    
    envio_id = fields.Integer("Numero de pedido", required=True, primary_key=True, unique=True)
    fechasalidaenvio = fields.Date("Fecha de salida",)
    fechaentregaenvio =  fields.Datetime("Fecha de entrega")
    empresareparto  = fields.Selection([('hlc', 'HLC'),('amazon','AMAZON'),('correos','CORREOS'),('nacex','Nacex')])