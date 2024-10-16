from odoo import fields, models, api
from odoo.exceptions import ValidationError



class HostelStudent(models.Model):
    _name = "hostel.student"
    _description = "Hostel Student Information"

    name = fields.Char("Student Name")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")
    room_id = fields.Many2one("hostel.room", "Room", required=True, help="Select hostel room")
    
    @api.model
    def create(self, vals):
        room = self.env['hostel.room'].browse(vals['room_id'])
        if len(room.student_ids) >= room.occupancy:
            raise ValidationError("The room '%s' is already full." % room.name)
        for student in self:
            if (room.hostel_id.type != 'common') and (student.gender != room.hostel_id.type):
                raise ValidationError(f"The {room.hostel_id.name} can not be allocated to {student.gender}.")
        return super(HostelStudent, self).create(vals)

    def write(self, vals):
        room = self.env['hostel.room'].browse(vals['room_id'])
        if len(room.student_ids) >= room.occupancy:
                raise ValidationError("The room '%s' is already full." % room.name)
        for student in self:
            if (room.hostel_id.type != 'common') and (student.gender != room.hostel_id.type):
                raise ValidationError(f"The {room.hostel_id.name} can not be allocated to {student.gender}.")
        return super(HostelStudent, self).write(vals)
