
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint


class FamilyStructure:
    def __init__(self, last_name, members):
        
        self.last_name = last_name
    # Example list of members
        self._members = members

    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        pass

    def delete_member(self, id):
        # Fill this method and update the return
        for person in self._members:
            if id == person['id']:
                self._members.remove(person)
                return True
        return None

    def get_member(self, id):
        # Fill this method and update the return
        for person in self._members:
            if id == person['id']:
                return person
        return None
        
    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
