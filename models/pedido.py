# -*- coding: utf-8 -*-
# Angel Gallego Zayas
from odoo import models,fields,api
from odoo.exceptions import ValidationError






class Pedido(models.Model) :
    @api.model
    def create(self, vals):
        # Validación: el precio total debe ser mayor que cero
        if vals.get('preciototal', 0) <= 0:
            raise ValidationError("El precio total debe ser mayor que cero.")
        
        # Crear el registro usando la lógica estándar
        pedido = super(Pedido, self).create(vals)

        # Comportamiento adicional: si el estado es 'enviado', enviar notificación al cliente
        if pedido.estado == 'enviado':
            cliente = pedido.cliente_id.name
            print(f"Notificación: Pedido {pedido.idpedido} enviado al cliente {cliente}.")
        
        return pedido
    
    
    
    _name='quintobeer.pedido'
    _description = 'Un pedido'
    
    idpedido = fields.Integer("Numero de pedido", required=True, primary_key=True)
    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('enviado', 'Enviado'),
            ('recibido', 'Recibido'),
            ('cancelado', 'Cancelado')
        ],
        string="Estado",
        required=True,
        default='pendiente'
    )
    
    
    fechapedido = fields.Date("Fecha de pedido",required=True)
    costo = fields.Float("Costo", required=True)
    iva = fields.Float("IVA", required=True)
    preciototal = fields.Float("Precio Total", compute='precio_total', store=True)

    @api.depends('costo', 'iva')
    def precio_total(self):
        for pedido in self:
            # Calcula el precio total sumando el costo y el IVA
            pedido.preciototal = pedido.costo + pedido.iva
    
    idenvio = fields.Many2one('quintobeer.envio', string="Codigo de Envío", ondelete='cascade')
    cliente_id = fields.Many2one('quintobeer.cliente', string="Codigo de Cliente", ondelete='cascade', required=True)
    idcerveza = fields.Many2many('quintobeer.cerveza', string="Cervezas")
    empleado_id = fields.Many2one('quintobeer.empleado', string="Codigo de Empleado", ondelete='cascade', required=True)
    
    
    
    def action_enviar(self):
        """Cambia el estado de 'Pendiente' a 'Enviado'."""
        if self.estado == 'pendiente':
            self.estado = 'enviado'

    def action_recibir(self):
        """Cambia el estado de 'Enviado' a 'Recibido'."""
        if self.estado == 'enviado':
            self.estado = 'recibido'

    def action_cancelar(self):
        """Cancela el pedido desde cualquier estado."""
        if self.estado in ['pendiente', 'enviado']:
            self.estado = 'cancelado'

    def action_reset(self):
        """Reinicia el pedido a 'Pendiente'."""
        if self.estado == 'cancelado':
            self.estado = 'pendiente'
            
            
    
    
    def unlink(self):
        for pedido in self:
         if pedido.estado == 'enviado':
            raise ValidationError("No se pueden eliminar pedidos enviados.")
        return super(Pedido, self).unlink()

