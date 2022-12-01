# SpaceX_to_postgres

This is a quick solution to parse SpaceX GraphQL API and load data into relational model

## Task
- Design some base layer of datamarts for analysts
- Write scripts to fill your datamarts with data
- Create datamart, that calculates number of publications for missions, rockets and launches
- Describe Dockerfile and write docker-compose.yml file, that will allow us to run your code and query your RDBMS (`docker-compose build и up`)
- Share your work in project on GitHub and send us link


## SpaceX DB

In this solution I: 
 - parse spaceX graphql api
 - get entities
 - build statements
 - create tables
 - load data into tables
 - runs datamarts building

 MVP:
  - took only Missions, Launches, Histories, Links and Rockets
  - made 3 datamarts (named DM_...) for publications count for relational objects
  - loader only creates tables and push data into it - no updates, increments, deletes, drops
  - some problems with docker-compose
  
  Problems:
  - Data model not so consistent as expexted
  - Database isn't reachable inside constainer - kinda infra problem
  
  Next steps:
  - Solve techical problems
  - Refactor code
  - Make it smarter 
      support model changing
      support incremental load
      support updates/deletes
  - Make universal model parser to catch and flatten all objects in any GraphQL API
  

## Usage

1. Run ```docker-compose up```
2. Run ```cd py```
2. Run ```python3 -m venv env | source env/bin/activate | pip install -r /requirements.txt```
3. Run ```python3 run_me.py```
3. Observe DB!
    ```jdbc:postgresql://localhost:8001/spacex-db```
