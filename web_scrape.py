#!/usr/bin/python3 

import requests 
from bs4 import BeautifulSoup



input1 = input("Enter a URL to web scrape:\n")

# Making a Get Request 
r = requests.get(input1)

# Logic for status code 
if r.status_code == 200 or 301:
        print(input1, "can be navigated to\n")
else:
        print('An error has occured\n')
# Checking URL for robots.txt 
adding_url_robots = input1 + '/robots.txt'
print(adding_url_robots)
adding_url_robot = input1 + '/robot.txt'
robot_request = requests.get(adding_url_robots)
 
if robot_request.status_code == 200:
        print('\n')
else:
        print("robots.txt is not valid") 

# Parsing HTML 
soup = BeautifulSoup(robot_request.content, 'html.parser')
print(soup.prettify())
