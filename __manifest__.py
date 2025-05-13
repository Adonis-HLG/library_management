# -*- coding: utf-8 -*-
{
    'name': "library_management",
    'version': '16.0.1.0.0',
    'summary': "Basic library management module",
    'description': """
        A module to manage books for a library system.
    """,
    'author':"Grupo Hernández S.U.R.L",
    'company':"Grupo Hernández S.U.R.L",
    'website':"https://www.grupohernandez.cu",
    'category':"Education",
    'license':"OPL-1",
    'depends':['contacts'],
    'data':[
            'views/menu_view.xml',
            'views/libros_view.xml',
            'views/prestamos_view.xml',
            'views/library_book_views.xml',
            'views/library_loan_views.xml',
            'views/res_partner_view.xml',
            'security/library_security.xml',
            'security/ir.model.access.csv'
            
             
    ],
    
    
}