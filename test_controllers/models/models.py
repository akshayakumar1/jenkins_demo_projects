# -*- coding: utf-8 -*-

from odoo import models, fields, api
from twilio.rest import Client



class test_controllers(models.Model):
    _name = 'test_controllers.test_controllers'
    _description = 'test_controllers.test_controllers'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class TestingsPhone(models.Model):
    _inherit = 'crm.lead'

    # _name = 'sms.composer'
    my_phone = fields.Char(string='New Phone for Testing')


class TestActionSmas(models.TransientModel):
    _inherit = "sms.composer"

    def action_send_sms(self):
        print('#' * 13)
        print("send sms call")
        account_sid = 'AC3ec2bfab4e3a756f40d8759cf7305273'
        auth_token = 'afc2b08141faa669292a6effe4ae76fb'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=str(self.body),
            from_='+15737250153',
            to=str(self.recipient_single_number)
        )

        print(message.sid)
        print(message.body)
        # print(message.)

        # res = super(TestActionSmas, self).action_send_sms()
        # return res




