
import json
import time
import subprocess


base_url = "https://api.github.com/repos/exosite/"
jq_cmd = " | jq  -r '.[] .name ' "

#headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8','Authorization': 'token 74b47f001a57ced6794b6a6d16518ab87593b2f5'}
#apod_url = "curl -H 'Authorization: token 74b47f001a57ced6794b6a6d16518ab87593b2f5' -o All_repos_name.json" +  base_url + "/repos?per_page=100" + jq_cmd


f_repos = open("All_repos_name.json", "r")
f_teams = open("All_repos_teams.json", "a")
lines = f_repos.readlines()
for line in lines:
    request_url = base_url + line.rstrip() + "/teams?per_page=100"
 #   print(request_url)
    apod_url= "curl -H 'Authorization: token 74b47f001a57ced6794b6a6d16518ab87593b2f5' " +  request_url + jq_cmd
 #   print(apod_url)
    p = subprocess.Popen(apod_url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for team in p.stdout.readlines():
        f_teams.write(team.decode().rstrip() + ',')
    f_teams.write("\n")
#    time.sleep(1)


f_teams.close()
