import unittest
# from gitlab import ProjectManager
from unittest.mock import patch
from gitlab.v4.objects import ProjectManager
import logindetails

from auth import Auth
from projects import Project
from projects import MockProject



MockProjectList=[]

MockProjectList.append(MockProject({ "id":"1", "path_with_namespace":"test1"}))
MockProjectList.append(MockProject({ "id":"2", "path_with_namespace":"test2"}))


class TestProject(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('this is the setup')

    def tearDown(self):
        pass

    @patch.object(ProjectManager, 'list', return_value=MockProjectList)
    def test_listProjectsPaths(self, list):
        print('starting now to auth')
        auth = Auth(username=logindetails.user, token=logindetails.token)
        activeGitlab = auth.authorizeUser()

        # create a Project object called project
        project = Project(projects=activeGitlab.projects, namespaces=activeGitlab.namespaces)
        # call the function to listProject paths - The API list function is mocked to return the Mockproject objects
        projpaths = project.listProjectsPaths()
        print(projpaths)
        #add asserts to confirm the return of the Mockprojects



if __name__ == '__main__':
    unittest.main()
