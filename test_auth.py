import unittest
#import gitlab
import gitlabtoken
import requests
#from gitlab import ProjectManager
from unittest.mock import patch
from projects import Project
from auth import Auth
from projects import MockProject
from gitlab.v4.objects import ProjectManager


class TestAuth(unittest.TestCase):
      
      @classmethod
      def setupClass(cls):
         pass

      @classmethod
      def tearDownClass(cls):
         pass


      def setUp(self):
        print('this is the setup')
        #retObj=MockProject('1','testname')  
    

      def tearDown(self):
         pass

      def test_generateSession(self): 
        """This test confirms that the session object defined to customize the HTTP configuration is setup properly"""
        auth = Auth(username = 'f33kv0p', token = gitlabtoken.token )
        #activeGitlab = auth.getActiveGitlab()
        session=auth.generateSession()
        #print(session.verify)
        self.assertEqual(False,session.verify)
             

      def test_authorizeUser(self):
        """This test confirms that the GET call to the HTTP server responds correctly"""
        auth = Auth(username = 'f33kv0p', token = gitlabtoken.token )
        session = auth.generateSession()
        #response = requests.get('https://gitlab.com')
        response = requests.get('https://gitlab.com', private_token=gitlabtoken.token, session=session)
        #print(gl.ssl_verify)
        self.assertEqual(200,response.status_code)

if __name__=='__main__':
    unittest.main()
