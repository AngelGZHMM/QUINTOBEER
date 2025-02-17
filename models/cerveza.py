from odoo import models, fields,api

class Cerveza(models.Model):
    _name = 'quintobeer.cerveza'
    _description = 'Modelo de Cerveza'
 
    nombre = fields.Char("Nombre", required=True)
    descripcion = fields.Char("Descripcion", required=True)
    foto = fields.Binary("Foto" , required=True)
    grados = fields.Float("Grados del Alchol", required=True)
    maduracion = fields.Integer("Meses de maduracion", required=True)
    envasado = fields.Selection(
        [
            ('botella', 'Botella'),
            ('lata', 'Lata'),
            ('barril', 'Barril')
        ],
        string="Envasado",
        required=True,
        default='botella'
    )
    pack = fields.Integer("Pack", required=True)
    precio_unidad = fields.Float("Precio Unidad", required=True)
    precio_pack = fields.Float("Precio Pack", compute='_compute_precio_pack', store=True)
    capacidad =  fields.Selection(
        [
            ('20cl', '20cl'),
            ('25cl', '25cl'),
            ('33cl', '33cl'),
            ('50cl', '50cl'),
            ('75cl', '75cl'),
            ('1l', '1l'),
            ('2l', '2l'),
            ('3l', '3l'),
            ('5l', '5l'),
        
        ],
        string="Capacidad",
        required=True,
        default='33cl'
    )
    ingrediente_ids = fields.Many2many("quintobeer.ingrediente",string="Ingredientes")
    pedido_ids = fields.Many2many("quintobeer.pedido",string="Pedidos")

    @api.model
    def create (self, vals):
        cerveza = super(Cerveza, self).create(vals)
        return cerveza

    @api.depends('pack', 'precio_unidad')
    @api.onchange('pack', 'precio_unidad')
    def _compute_precio_pack(self):
        """Calcula automáticamente el precio del pack basado en el número de unidades."""
        for cerveza in self:
            cerveza.precio_pack = cerveza.pack * cerveza.precio_unidad if cerveza.pack else 0