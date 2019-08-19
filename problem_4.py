class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_user_in_group(self, user, group):
        if user in group.get_users():
            return True
        new_groups = group.get_groups()
        for current_group in new_groups:
            result = self.is_user_in_group(user, current_group)
            if result:
                return True
        return False

def test_user_in_sub_child():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group(sub_child_user, parent))


def test_user_in_child():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group(sub_child_user, child))


def test_user_doesnt_exist():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(parent.is_user_in_group("none existing",child))


test_user_in_sub_child()
test_user_in_child()
test_user_doesnt_exist()