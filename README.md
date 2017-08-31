usage: gitlab-cli.py [-h] -s SERVER -t TOKEN [-a API][-o OUTPUT]

                     {user,group,project} ...

Gitlab cli

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        ip or fqdn of Gitlab server
  -t TOKEN, --token TOKEN
                        Token Gitlab server
  -a API, --api API     Version api Gitlab server
  -o OUTPUT, --output OUTPUT
                        Write output in file

object:
  {user,group,project}
    user                User object
    group               Group object
    project             Project object
Example:

./giltab-cli.py -s {server_name} -t {TOKEN} user create -f {file} (Create user from file)

{Firstname second name, email, username, false}



/giltab-cli.py -s {server_name} -t {TOKEN} project member {id project} add {id user} -a reporter (Add user in project with access reporter)