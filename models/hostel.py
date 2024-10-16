from odoo import api, fields, models


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = "Information about hostel"
    _rec_name = 'hostel_code'

    name = fields.Char(string="hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    # Hostel has many rooms
    room_ids = fields.One2many('hostel.room', 'hostel_id', string='Rooms')
    active = fields.Boolean("Active", default=True, help="Activate/Deactivate hostel record")

    type = fields.Selection([("male", "Boys"), ("female", "Girls"),
        ("common", "Common")], "Type", help="Type of Hostel", required=True, default="common")
    
    rector = fields.Many2one("res.partner", "Rector", help="Select hostel rector")

    # @api.depends('hostel_code')
    # def _compute_display_name(self):
    #     for record in self:
    #         name = record.name
    #         if record.hostel_code:
    #             name = f'{name} ({record.hostel_code})'
    #         record.display_name = name
