from odoo import api, fields, models

class FleetVehicle(models.Model):
    _inherit = 'stock.picking'

    volume_transfer = fields.Float(compute="_compute_volume_transfer", string="Volume")

    @api.depends("move_ids.product_id.volume")
    def _compute_volume_transfer(self):
        for record in self:
            record.volume_transfer = sum(line.product_id.volume*line.quantity for line in record.move_ids)
            