from odoo import models, fields

class LibraryBook(models.Model):
   _name = 'library.book'

   name = fields.Char(string="Nombre del libro")
   isbn = fields.Char(string="ISBN")
   autor = fields.Char(string="Autor")
   fecha = fields.Date(string="Fecha de publicación")
