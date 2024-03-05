from odoo import fields, models

class DispatchPropertyDoc(models.Model):
    _name = "dispatch.property.doc"
    _description = "Property Documents"
    name = fields.Char()
    