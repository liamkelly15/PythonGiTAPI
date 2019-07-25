Gitlab Management Tool

Initial virtual setup for non Python ID (such as Visual Studio - For Python ID such as PyCharm the Virtual Env Intrepretor
can be set in the GUI)
From the project root directory:
    Run: "python3 -m venv ./env" to create the virtual environment
    Run: "source ./env/bin/activate" to activate the environment 



Run: "pip3 install -r ./requirements.txt" in the virtual python env to install the requirements listed in
requirements.txt


Add User Login details for Gitlab to logindetails.py
Populate the list of projects with namespaces to the file ProjectList.json
Populate the baseAttributes to be used for each new project to the file baseAttributes.json
Populate the pushrules to be used for all new and existing projects to the file pushrules.json
Add Data file locations (ProjectList,baseAttributes,pushrules) to the logindetails.py 



DEVELOPMENT

Complete
---- New Projects in ProjectList.json automatically added to the Gitlab namespace given in the list
---- Old Projects removed from the ProjectList.json automatically removed from Gitlab
---- All the Projects automatically are set with the current pushrules (in Pushrules.json) 

To Do
----- 




TESTING

Complete
----- Test for connection to API complete - see test_auth.py

To Do
----- Tests which require a mock of the API return data  - see test_projects.py 


DOCUMENTATION

Complete
------ Added in Sphinx recognized documentation - run Sphinx to pick up the documentation notes and generate the report