# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestProjectMilestone(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.test_project = self.env['project.project'].create({
            'name': 'TestProject'})
        self.test_project_milestone_1 = self.env['project.milestone'].create({
            'name': 'TestMilestone_1',
            'project_id': self.test_project.id})
        self.test_project_milestone_2 = self.env['project.milestone'].create({
            'name': 'TestMilestone_2',
            'project_id': self.test_project.id})
        self.test_open_stage = self.env['project.task.type'].create({
            'name': 'TestOpenStage'})
        self.test_close_stage = self.env['project.task.type'].create({
            'name': 'TestCloseStage',
            'closed': True})
        self.env['project.task'].create({
            'name': 'TestTask',
            'project_id': self.test_project.id,
            'milestone_id': self.test_project_milestone_1.id,
            'stage_id': self.test_open_stage.id})
        self.env['project.task'].create({
            'name': 'TestTask',
            'project_id': self.test_project.id,
            'milestone_id': self.test_project_milestone_1.id,
            'stage_id': self.test_close_stage.id})

    def test_milestone_sequences(self):
        milestone1 = self.test_project_milestone_1
        milestone2 = self.test_project_milestone_2

        self.assertEqual(milestone1.sequence, 1)
        self.assertEqual(milestone2.sequence, 2)

    def test_milestone_progress(self):
        milestone1 = self.test_project_milestone_1

        self.assertEqual(milestone1.progress, 50)
