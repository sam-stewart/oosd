from documentfactory import DocumentFactory

test_dict = { 'name' : 'Sam Stewart',
        'role' : 'Lecturer',
        'hobbies' : ['Running', 'Hunting'],
        'favourite beer' : {'Brewer' : 'Harringtons',
                            'Name' : 'Rogue hop pilser'}
        }

print DocumentFactory.get_doc("xml", test_dict)

