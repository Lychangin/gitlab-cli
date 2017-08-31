#!/usr/bin/env python3
import argparse
import json
import requests


class Gitlab_project():
    def listProjects(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects'
        header = {'PRIVATE-TOKEN': args.token}
        projects_list = []
        for page in range(1, 100):
            projects = requests.get(api_url, headers=header, params={'page': page})
            if len(projects.json()) == 20:
                for project in projects.json():
                    projects_list.append(project)
            else:
                for project in projects.json():
                    projects_list.append(project)
                break
        if args.output:
            for project in projects_list:
                [print(project[output], end='\t') for output in args.output]
                print()
        else:
            return print(json.dumps(projects_list, ensure_ascii=False, indent=4))

    def getProject(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects'
        header = {'PRIVATE-TOKEN': args.token}
        project = requests.get(api_url, headers=header, params={'search': args.project_name})
        projects_list = project.json()
        if args.output:
            for project in projects_list:
                [print(project[output], end='\t') for output in args.output]
                print()
        else:
            return print(json.dumps(projects_list, ensure_ascii=False, indent=4))

    def deleteProject(self):
        pass

    def archiveProject(self):
        pass

    def starProject(self):
        pass

    def unstarProject(self):
        pass

    def editProject(self):
        pass

    def unarchiveProject(self):
        pass

    def createProject(self):
        pass

    def listMember(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects/' + args.project_id + '/members'
        header = {'PRIVATE-TOKEN': args.token}
        users = requests.get(api_url, headers=header)
        users_json = users.json()
        return print(json.dumps(users_json, ensure_ascii=False, indent=4))

    def addMember(self):
        access_level = {'guest': 10,
                        'reporter': 20,
                        'developer': 30,
                        'master': 40,
                        'owner': 50}
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects/' + args.project_id + '/members'
        header = {'PRIVATE-TOKEN': args.token}
        user = requests.post(api_url, headers=header, params={'user_id': args.user_id, \
                                                              'access_level': access_level[args.access]})
        return print(json.dumps(user.json(), ensure_ascii=False, indent=4))

    def editMember(self):
        access_level = {'guest': 10,
                        'reporter': 20,
                        'developer': 30,
                        'master': 40,
                        'owner': 50}
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects/' + args.project_id + '/members/' + args.user_id
        header = {'PRIVATE-TOKEN': args.token}
        user = requests.put(api_url, headers=header, params={'user_id': args.user_id, \
                                                             'access_level': access_level[args.access]})
        return print(json.dumps(user.json(), ensure_ascii=False, indent=4))

    def removeMember(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/projects/' + args.project_id + '/members/'
        header = {'PRIVATE-TOKEN': args.token}
        print(args.user_id)
        for member in args.user_id:
            user = requests.delete((api_url + member), headers=header)
        return print(user.ok)


class Gitlab_group():
    def getGroup(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/groups'
        header = {'PRIVATE-TOKEN': args.token}
        groups_list = []
        for page in range(1, 100):
            groups = requests.get(api_url, headers=header, params={'page': page})
            if len(groups.json()) == 20:
                for group in groups.json():
                    groups_list.append(group)
            else:
                for group in groups.json():
                    groups_list.append(group)
                break
        if args.output:
            for group in groups_list:
                [print(group[output], end='\t') for output in args.output]
                print()
        else:
            return print(json.dumps(groups_list, ensure_ascii=False, indent=4))

    #
    # def getGroupPage(self):
    #     url = args.server + '/api/v' + args.api
    #     api_url = url + '/groups'
    #     header = {'PRIVATE-TOKEN': args.token}
    #     groups_json = []
    #     for page in range(1, 100):
    #         groups = requests.get(api_url, headers=header, params={'page': page})
    #         if len(groups.json()) == 20:
    #             for group in groups.json():
    #                 groups_json.append(group)
    #         else:
    #             for group in groups.json():
    #                 groups_json.append(group)
    #             break
    #     return print(json.dumps(users_json, indent=4))

    def deleteGroup(self):
        pass

    def editGroup(self):
        pass

    def createGroup(self):
        pass


class Gitlab_user():
    def getUsers(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/users'
        header = {'PRIVATE-TOKEN': args.token}
        users_json = []
        for page in range(1, 100):
            users = requests.get(api_url, headers=header, params={'page': page})
            if len(users.json()) == 20:
                for user in users.json():
                    users_json.append(user)
            else:
                for user in users.json():
                    users_json.append(user)
                break
        if args.output:
            for user in users_json:
                [print(user[output], end='\t') for output in args.output]
                print()
        else:
            return print(json.dumps(users_json, ensure_ascii=False, indent=4))

    def getUserById(self):
        api_url = self.url + '/users'
        header = {'PRIVATE-TOKEN': self.token}
        user_json = []
        users = requests.get(api_url, headers=header, params={'page': page})
        if len(users.json()) == 20:
            for user in users.json():
                user_json.append(user)
        else:
            for user in users.json():
                user_json.append(user)
                break
        return json.dumps(users_json, ensure_ascii=False, indent=4)

    def getUserByUsername(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/users'
        header = {'PRIVATE-TOKEN': args.token}
        user = requests.get(api_url, headers=header, params={'username': args.username})
        answer = user.json()
        if args.output:
            for output in args.output:
                [print(json[output]) for json in answer]
        return print(json.dumps(answer, ensure_ascii=False, indent=4))

    def createUser(self):
        url = args.server + '/api/v' + args.api
        api_url = url + '/users'
        header = {'PRIVATE-TOKEN': args.token}
        answer = []
        with open(args.file, encoding='UTF-8') as file:
            text = file.read().splitlines()
        users = []
        for list in text:
            users.append([x.strip() for x in list.split(',')])
        for name, email, username, external in users:
            data = {'name': name, 'email': email, 'username': username, 'external': external, 'reset_password': 'true'}
            res = requests.post(api_url, headers=header, data=data)
            answer.append(res.json())
        return print(json.dumps(answer, ensure_ascii=False, indent=4))


def get_args():
    parser = argparse.ArgumentParser(description="Gitlab cli")
    parser.add_argument('-s', '--server', required=True, action='store', help='ip or fqdn of Gitlab server')
    parser.add_argument('-t', '--token', required=True, action='store', help='Token Gitlab server')
    parser.add_argument('-a', '--api', action='store', type=str, default='4', help='Version api Gitlab server')
    parser.add_argument('-o', '--output', action='store', help='Write output in file')

    subparsers = parser.add_subparsers(title='object')
    gitlab_user = subparsers.add_parser('user', help='User object')
    gitlab_group = subparsers.add_parser('group', help='Group object')
    gitlab_project = subparsers.add_parser('project', help='Project object')

    ## Call Users Function
    subparsers = gitlab_user.add_subparsers(title='action')

    list_users = subparsers.add_parser('list', help='Get list users')
    list_users.add_argument('-o', '--output', nargs='*', help='Output parameters', choices=['name', 'username' \
        , 'id', 'state'])
    list_users.set_defaults(func=Gitlab_user.getUsers)

    search_user = subparsers.add_parser('search', help='Search user by username')
    search_user.add_argument('username', help='type this way username ')
    search_user.add_argument('-o', '--output', nargs='*', help='Output parameters', choices=['name', 'username' \
        , 'id', 'state'])
    search_user.set_defaults(func=Gitlab_user.getUserByUsername)

    create_user = subparsers.add_parser('create',usage='gitlab-cli.py -s https://gitlab.ru -t TOKEN '
                                                    'user create -f text.txt',
                                            description='Structure file: '
            'Фамилия Имя Отчество, test@gmail.com, username, true',help='Create user')
    create_user.add_argument('-f', '--file', required=True, help='name, email, username, external')
    create_user.set_defaults(func=Gitlab_user.createUser)

    ## Call Group Function
    subparsers = gitlab_group.add_subparsers(title='action')
    list_groups = subparsers.add_parser('list')
    list_groups.add_argument('-o', '--output', nargs='*', help='Output parameters', choices=['name', 'id'])
    list_groups.set_defaults(func=Gitlab_group.getGroup)

    # Call Project Function
    subparsers = gitlab_project.add_subparsers(title='action')
    list_projects = subparsers.add_parser('list', help='Get list projects')
    list_projects.add_argument('-o', '--output', nargs='*', help='Output parameters',
                               choices=['name', 'id', 'path_with_namespace'])
    list_projects.set_defaults(func=Gitlab_project.listProjects)

    search_project = subparsers.add_parser('search', help='Get list projects')
    search_project.add_argument('project_name')
    search_project.add_argument('-o', '--output', nargs='*', help='Output parameters', choices=['name', 'id'])
    search_project.set_defaults(func=Gitlab_project.getProject)

    members_project = subparsers.add_parser('member', help='Get list members project')
    members_project.add_argument('project_id', help='The project ID of the new member, Required!!')

    subparsers = members_project.add_subparsers()

    member_list = subparsers.add_parser('list')
    member_list.add_argument('-o', '--output', nargs='*', help='Output parameters', choices=['name', 'id'])
    member_list.set_defaults(func=Gitlab_project.listMember)

    member_add = subparsers.add_parser('add', help='Add member in project')
    member_add.add_argument('user_id', help='The user ID of the new member')
    member_add.add_argument('-a', '--access', required=True, help='A valid access', choices=['guest', 'reporter', \
                                                                                             'developer', 'master'])
    #member_add.add_argument('-e', '--expired', help='A date string in the format YEAR-MONTH-DAY')
    member_add.set_defaults(func=Gitlab_project.addMember)

    member_add = subparsers.add_parser('edit', help='Edit member in project')
    member_add.add_argument('user_id', help='The user ID of the new member')
    member_add.add_argument('-a', '--access', required=True, help='A valid access', choices=['guest', 'reporter', \
                                                                                             'developer', 'master'])
    #member_add.add_argument('-e', '--expired', help='A date string in the format YEAR-MONTH-DAY')
    member_add.set_defaults(func=Gitlab_project.editMember)

    member_add = subparsers.add_parser('delete', help='Delete member from project')
    member_add.add_argument('user_id', nargs='*', help='The user ID of the new member')
    member_add.set_defaults(func=Gitlab_project.removeMember)

    args = parser.parse_args()

    return args


def test():
    print('Herecrello')


def main():
    pass


if __name__ == '__main__':
    args = get_args()
    args.func(args)
