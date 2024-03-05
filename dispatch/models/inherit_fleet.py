from odoo import api, fields, models

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    max_weight = fields.Integer(string="Max Weight (Kg)")
    max_volume = fields.Integer(string="Max Volume (m^3)")

    @api.depends("name", "max_weight", "max_volume")
    def _compute_display_name(self):
        for line in self:
            name = f"{line.name}({line.max_weight}kg, {line.max_volume}m\u00B3)"
            line.display_name = name