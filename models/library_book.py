# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'LibraryBook'

    name = fields.Char('Nombre del libro')
    
