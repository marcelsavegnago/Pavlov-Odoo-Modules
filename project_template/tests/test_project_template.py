# Copyright 2019 Patrick Wilson <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestProjectTemplate(common.TransactionCase):

    # Use case : Prepare some data for current test case
    def setUp(self):
        super().setUp()
        test_project = self.env['project.project'].create({
            'name': 'TestProject'})
        test_project_task = self.env['project.task'].create({
            'name': 'TestTask',
            'project_id': test_project.id})

    # TEST 01: Set project to be a template
    def test_template(self):
        test_project.is_template = True
        self.assertEqual(test_project.name, 'TestProject (TEMPLATE)')

    # TEST 02: Create project from templates
    def test_create_project_from_template(self):
