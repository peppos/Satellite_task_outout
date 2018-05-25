#!/usr/bin/python

import argparse
import json
import requests
import sys
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


parser = argparse.ArgumentParser(description="Show output for every hosts in a specific Job")
parser.add_argument("-n", "--server", type=str.lower, required=True, help="Satellite server (defaults to localhost)", default='localhost')
parser.add_argument("-u", "--username", type=str, required=True, help="Username to access Satellite")
parser.add_argument("-p", "--password", type=str, required=False, help="Password to access Satellite. The user will be asked interactively if password is not provided.")
parser.add_argument("-id", "--id", type=str.lower, required=True, help="Job ID")


args = parser.parse_args()

# Satellite specific parameters
url = "https://" + args.server
api = url + "/api/v2/"
katello_api = url + "/katello/api/v2/"
foreman_tasks_api = url + "/foreman_tasks/api/tasks"
job_api = api + "job_invocations/"

post_headers = {'content-type': 'application/json'}
ssl_verify=True



if args.password is None:
    args.password = getpass.getpass()

def get_with_json(location, json_data):
    """
    Performs a GET and passes the data to the url location
    """
    try:
        result = requests.get(location,
                            data=json_data,
                            auth=(args.username, args.password),
                            verify=ssl_verify,
                            headers=post_headers)

    except requests.ConnectionError, e:
        print sys.argv[0] + " Couldn't connect to the API, check connection or url"
        print e
        sys.exit(1)
    return result.json()

def job_report():
    # Print headline
    print "Hostname;Output"
    job = get_with_json(job_api +  args.id, json.dumps({"per_page": "10000000"}))["dynflow_task"]

    task_id = job["id"]
    tasks = get_with_json(foreman_tasks_api + "?search=parent_task_id=" + str(task_id), json.dumps({"per_page": "10000000"}))["results"]

    for task in tasks:
        output = task["humanized"]["output"]
        hostname = task["input"]["host"]["name"]
        output = output.replace("\n", " ")
        print str(hostname) + ";" + str(output)

if __name__ == "__main__":

        job_report()
 
