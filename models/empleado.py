# Sergio Gómez
from odoo import models, fields

class Empleado(models.Model):
    _name = 'quintobeer.empleado'
    _inherit = 'quintobeer.persona'
    _description = 'Modelo de Empleado'

    horario_trabajo = fields.Selection(
        [('mañana', 'Mañana'), ('tarde', 'Tarde')],
        string='Horario de Trabajo',
        required=True
    )
    salario = fields.Float(string='Salario')
    zona_trabajo = fields.Char(string='Zona de Trabajo')
    fecha_contratacion = fields.Date(string='Fecha de Contratación')
    pedidos_ids = fields.One2many(
        comodel_name='quintobeer.pedido',
        inverse_name='empleado_id',
        string='Pedidos Atendidos'
    )
    

    def method(self, param):
        """
        Sobrescribe el método base con funcionalidad específica para empleado.
        """
        return f"Empleado: {self.name} - Método sobrescrito con parámetro: {param}"
