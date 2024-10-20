from odoo import fields, models, api, _


class HostelRoom(models.Model):

    _name = "hostel.room"
    _description = "Hostel Room Information"
    _rec_name = 'display_name' 

    name = fields.Char(string="Room Name", required=True)
    hostel_id = fields.Many2one("hostel.hostel", "Hostel", required=True)
    hostel_name = fields.Char("Hostel Name", compute='_get_hostel_name')
    category = fields.Integer('Category')
    occupancy = fields.Integer(string='Max Occupancy')
    student_ids = fields.One2many("hostel.student", "room_id", string="Students", help="Enter students")
    current_occupancy = fields.Integer(string='Currently Staying', compute='_compute_current_occupancy')
    display_name = fields.Char(string="Display Name", compute='_compute_display_name', store=True)
    
    _sql_constraints = [
       ("room_name_unique", "unique(name)", "Room name must be unique!")]

    @api.depends('student_ids')
    def _compute_current_occupancy(self):
        for room in self:
            room.current_occupancy = len(room.student_ids)

    @api.constrains('student_ids')
    def _check_occupancy(self):
        for room in self:
            if len(room.student_ids) > room.occupancy:
                raise ValidationError("Room '%s' has exceeded the maximum occupancy!" % room.name) 

    @api.depends('name', 'hostel_id.name')
    def _compute_display_name(self):
        for room in self:
            if room.hostel_id and room.name:
                room.display_name = f"{room.hostel_id.name} / {room.name}"
            else:
                room.display_name = room.name
    
    @api.depends('hostel_id')
    def _get_hostel_name(self):
        for room in self:
            room.hostel_name = room.hostel_id.name


