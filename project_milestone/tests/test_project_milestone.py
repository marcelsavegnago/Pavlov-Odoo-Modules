# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestProjectMilestone(common.TransactionCase):

    def test_create_data(self):
        # Create a new project with the tests
        test_project = self.env['project.project'].create({
            'name': 'TestProject'})

        # Add a test Milestone to the project
        test_project_milestone_1 = self.env['project.milestone'].create({
            'name': 'TestMilestone_1',
            'project_id': test_project.id})
        test_project_milestone_2 = self.env['project.milestone'].create({
            'name': 'TestMilestone_2',
            'project_id': test_project.id})

        # Check Milestone Sequences
        self.assertEqual(test_project_milestone_1.sequence, 1)
        self.assertEqual(test_project_milestone_2.sequence, 2)

        # Create stages
        test_open_stage = self.env['project.task.type'].create({
            'name': 'TestOpenStage'})
        test_close_stage = self.env['project.task.type'].create({
            'name': 'TestCloseStage',
            'closed': True})

        # Create a test Task to the project with the MILESTONE
        test_project_task_1 = self.env['project.task'].create({
            'name': 'TestTask',
            'project_id': test_project.id,
            'milestone_id': test_project_milestone_1.id,
            'stage_id': test_open_stage.id})
        test_project_task_2 = self.env['project.task'].create({
            'name': 'TestTask',
            'project_id': test_project.id,
            'milestone_id': test_project_milestone_1.id,
            'stage_id': test_close_stage.id})

        # Check Milestone progress
        self.assertEqual(test_project_milestone_1.progress, 50)
