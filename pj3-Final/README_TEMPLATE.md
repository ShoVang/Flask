# Overview

Vision Statement:
Are you tired of always getting lost in the zoo while trying to find an animal, only to realize it's not there? Well, now with our website, you can easily view our inventory of animals and even access information about their whereabouts within the zoo. But our website isn't just for clients; as an admin of the corporation, you can also view and edit the zoo's inventory. Say goodbye to Excel sheets for tracking your Year-to-Date (YTD) goals! With our platform, you can effortlessly monitor your corporation's goals and income from customers. This information is presented in a pie chart format, making it easy to understand and interpret. 
# Design

## User Stories

Common functionalities for both Customer and Admin:

US#1 Registration and Sign-in: Both customers and administrators should be able to create accounts and log in to access the system.
Functionalities for Customers (cx): 2 

US#2 View Inventory: Customers should be able to view animals, once they are loged in thet can view more detailes about the animals :2

US#3 Edit Inventory: Admins should be able to see animal inventory and add or delet the inventory. :4

US#4 Edit Inventory: Admins should be abel to edit the details insde of the animal table  :5

US#5 View Status report: Admins should be able to view status report a pie chart representing YTD goals and amount remanding and what % is coming from what member ships.  : 7

Us#5.5 automation status report should be automated no need for admin interferance : 5

US#6 change pw: the user should be able to change passwords. : 3


To implement these functionalities, you'll need a web application with different user roles (customer and administrator) and appropriate interfaces for each role. The system should have a database to store information about animals, locations, user accounts, memberships, and quotas. Additionally, you'll need to implement secure authentication mechanisms for user registration and login. 6avg ? 

## Sequence Diagram

At least one user story, not related to user creation or authentication, must be detailed using a sequence diagram.

## Model 

At a minimum, this section should have a class diagram that succinctly describes the model classes used in the project, including their associations.


# Development Process 

This section should be used to describe how the scrum methodology was used in this project. As a suggestion, include the following table to summarize how the sprints occurred during the development of this project.

|Sprint#|Goals|Start|End|Done|Observations|
|---|---|---|---|---|---|
|1|US#1, US#2, ...|mm/dd/23|mm/dd/23|US#1|...|

Use the observations column to report problems encountered during a sprint and/or to reflect on how the team has continuously improved its work. If you prefer, you can use the same format used in the project 2 (sprint markdown files). 

|Sprint# 1 |---|4/23|4/26|---|---|
|#1 : Goals| We wanted to plan the prodject make sure to come up with all the user stories as well as delgate the work up. Also started with the basic hmtls and the basic python modules / forms set ups

|Sprint# 2|---|4/26|4/29|---|---|
|#2 : Goals| Wanted to get the work started with the login, signup, as well as the animal table started.

|Sprint# 3|---|4/30|5/3|---|---|
|#3 : Goals| Wanted to get the added and subtracting animals working. Also wanted to get the pie chart up and runing. 

|Sprint# 4|---|5/4|5/7|---|---|
|#4 : Goals| Needed to tie in the member ships and make them connect to the pie chart, as well as figure out the issues uploading pictures into the animal tables. also docker stuff

|Sprint# 5|---|5/7|5/10|---|---|
|#5 :Goals | need to finsh the 2 testing types clean code alrdy ran the pep8 so after that we are done. 




# Testing 

Share in this section the results of the tests performed to attest to the quality of the developed product, including the coverage of the tests in relation to the written code. There is no minimum code coverage expectation for your tests, other than expecting "some" coverage through at least one white-box and one black-box test.

# Deployment 

The final product must demonstrate the integrity of at least 5 of the 6 planned user stories. The final product must be packaged in the form of a docker image. The project should be able to be deployed using: 

```
docker compose up
```
