from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'

    name = fields.Char(string="Nombre del libro", required=True)
    res_partner_id = fields.Many2one(comodel_name="res.partner", string="Nombre del lector", required=True)
    loan_date = fields.Date(string="Fecha de préstamo")
    return_date = fields.Date(string="Fecha límite de devolución")
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('pendiente', 'Pendiente'),
        ('devuelto', 'Devuelto')
    ], string="Estado", default='borrador')

    def boton_devuelto(self):
        self.estado = 'devuelto'