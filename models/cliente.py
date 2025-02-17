# Sergio Gómez
from odoo import models, fields

class Cliente(models.Model):
    _name = 'quintobeer.cliente'
    _inherit = 'quintobeer.persona'
    _description = 'Modelo de Cliente'

    direccion_envio = fields.Char(string='Dirección de Envío')
    ccv = fields.Integer(string='CCV')
    caducidad_tarjeta = fields.Char(string='Caducidad de Tarjeta')
    num_tarjeta = fields.Char(string='Número de Tarjeta')
    pedidos_ids = fields.One2many(
        comodel_name='quintobeer.pedido',
        inverse_name='cliente_id',
        string='Pedidos'
    )
    

    def method(self, param):
        """
        Sobrescribe el método base con funcionalidad específica para cliente.
        """
        return f"Cliente: {self.name} - Método sobrescrito con parámetro: {param}"