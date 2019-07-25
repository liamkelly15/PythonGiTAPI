import gitlab
import os
import gitlab.config
import json
import requests

class Auth:
    """The Auth Class represents a connection to the GitLab library with a Username and Token"""
    def __init__(self, username, token, certificatePath=None, httpProxy=None, httpsProxy=None):
        self.username = username
        self.token = token
        self.httpProxy = httpProxy
        self.httpsProxy = httpsProxy
        self.gitlab = None
        self.session = None
        self.gitlab = None
        self.certificatePath = certificatePath
        if username is None or token is None:
            raise Exception('Class - Auth, Username and Token cannot be None')

    def generateSession(self):
        """The function generateSession creates a Session Object with a customised HTTP configuration for GitLab"""
        session = requests.Session()
        if self.certificatePath is None:
            #This will likely need to be modified for systems with more than one self-signed certifacate
            self.certificatePath = os.environ.get('REQUEST_CA_BUNDLE')
        
        #session.verify=self.certificatePath
        session.verify=False


        if self.httpProxy is None:
            self.httpProxy = os.environ.get('http_proxy')
        if self.httpsProxy is None:
            self.httpsProxy = os.environ.get('https_proxy')

        session.proxies = {
            'http' : self.httpProxy,
            'https' : self.httpsProxy
        }
        return session

    def authorizeUser(self):
        """The function authorizeUser connects to the Gitlab HTTP, creates a gitlab.Gitlab Object
         a gitlab.Gitlab.user object and returns the gitlab.Gitlab Object"""
        self.session = self.generateSession()
        gl = gitlab.Gitlab('https://gitlab.com', private_token=self.token, session=self.session)
        gl.auth()
        return gl
    
    #def getActiveGitlab(self):
    #    self.gitlab = self.authorizeUser()
    #    return self.gitlab
        








