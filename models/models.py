# from mongoengine import *
#
# from datetime import datetime
#
# import json
#
# connect('rice')
#
#
# class CustomerModel(Document):
#     first_name = StringField(required=True)
#     last_name = StringField(required=True)
#     phone_no = StringField(required=True, max_length=16)
#     office_no = StringField(required=True, max_length=16)
#     email = EmailField(unique=True)
#     address = StringField(required=True)
#     date_created = DateTimeField(default=datetime.utcnow)
#
#     def json(self):
#         customer_dict = {
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'phone_no': self.phone_no,
#             'office_no': self.office_no,
#             'email': self.email,
#             'address': self.address
#         }
#         return json.dumps(customer_dict)
#
#     # meta = {
#     #     'indexes': ['first_name', 'last_name', 'phone_no'],
#     #     'ordering': ['']
#     # }
