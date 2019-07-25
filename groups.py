import gitlab

class Groups:
    """This is the Groups Class"""
    def __init__(self, groups):
        self.groups = groups

    def listGroups(self):
        """ This is the listGroups function-The function returns all the groups in the GitLab account """
        groups = self.groups.list(membership=True)
        groupList = []
        for group in groups: 
            groupDetails = {
                'group_id' : group.attributes['id'],
                'group_name' : group.attributes['full_name']
            }
            groupList.append(groupDetails)
        return groupList

    def listGroupMembers(self, groupname):
        """This is the listGroupMembers function-The function requires a Group name and returns all the
        members of the Group"""
        group = self.groups.get(groupname)
        members = group.members.list(all=True)
        memberList = []
        for member in members:
            memberDetails = {
                'member_id' : member.attributes['id'],
                'name' : member.attributes['name']
            }
            memberList.append(memberDetails)
        return memberList
    
    def addUserToGroup(self, userId, groupname, accessLevel):
        """This is the addUserToGroup function"""
        group = self.groups.get(groupname)
        group.members.create(
            {
                'user_id': userId,
                'access_level': accessLevel
            }
        )