# Sergio Gómez
from odoo import models, fields

class Persona(models.Model):
    _name = 'quintobeer.persona'  # Nombre único del modelo
    _description = 'Modelo de Persona'

    name = fields.Char(string='Nombre', required=True)  # Nombre
    apellidos = fields.Char(string='Apellidos', required=True)  # Apellidos
    email = fields.Char(string='Correo Electrónico', required=True)  # Email
    telefono = fields.Integer(string='Teléfono')  # Teléfono
    direccion = fields.Char(string='Dirección')  # Dirección
    foto = fields.Binary(string='Foto')  # Foto
    fecha_nac = fields.Date(string='Fecha de Nacimiento')  # Fecha de nacimiento
    dni = fields.Char(string='DNI', required=True)  # DNI

    def method(self, param):
        """
        Método genérico que puede ser sobrescrito por modelos heredados.
        """
        return f"Persona: {self.name} - Método ejecutado con parámetro: {param}"