{'name': 'Library Management Application 2',
 'description': 'Company',
 'author': 'Batur Gezici',
 'depends': ['base', 'hr'],
 'data': [
     'security/groups.xml',
     'security/ir.model.access.csv',
     'security/company_security.xml',
     'views/company.xml',
     'views/company_view.xml',
     'views/employee.xml'

 ],
 'application': True,
 'installable': True,
 }
