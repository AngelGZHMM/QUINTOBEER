from odoo import models,fields,api


class Ingrediente(models.Model) :
    _name= 'quintobeer.ingrediente'
    _description = 'Modelo de Ingrediente'


    nombre = fields.Char("Nombre", required=True)
    foto = fields.Binary(string="Foto")  # Foto 
    tipo = fields.Selection(
        [
            ('agua', 'Agua'),
            ('malta base', 'Malta basae'),
            ('malta especial', 'Malta Especial'),
            ('lupulo amargo', 'Lupulo Amargo'),
            ('lupulo aroma', 'Lupulo Aroma'),
            ('lupulo dual', 'Lupulo Dual'),
            ('levadura ale', 'Levadura Ale'),
            ('levadura lager', 'Levadura Lager'),
            ('levadura salvaje', 'Levadura Salvaje'),
            ('cereal maiz', 'Cereal Maiz'),
            ('cereal arroz', 'Cereal Arroz'),
            ('cereal trigo', 'Cereal Trigo'),
            ('cereal avena', 'Cereal Avena'),
            ('cilantro', 'Cilantro'),
            ('miel', 'Miel'),
            ('azucar cana', 'Azucar Caña'),
            ('hiervas', 'Hiervas'),
        ],
        string="Tipo",
        required=True,
        default='malta especial'
    )
    descripcion  = fields.Char("Descripcion", required=True)
    cerveza_ids = fields.Many2many("quintobeer.cerveza",string="Cerveza")

    @api.model
    def create (self,vals):

        ingrediente = super(Ingrediente, self).create(vals)
        return ingrediente
     
