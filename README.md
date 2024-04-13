## This is a Python web server demonstration using FastAPI ,MySQL, and Vue
### Functionalities
#### APIs
- User Management
    - Create User: add a new user
    - Delete User: Remove a user by id
    - Read Single User: Retrieve details of a specific user by id.
    - Read All Users: List all users with optional filtering by partial name match.
    - Update User: To update a user's name, group_id, or is_activate
- Groups Management
    - Create Group: Add a new group.
    - Delete Group: Remove a group by id. Prevent deletion if the group has at least one user and provide an appropriate error message.
    - Read Single Group: Retrieve details of a specific group by id.
    - Read All Groups: List all groups.
    - Update Group: To update a group's name or is_activate
---
### Database Design
#### Users Table
| id     | name               | group_id| is_activate| creator | createdTime        | modifier| modifiedTime       |
|--------|--------------------|---------|------------|---------|--------------------|---------|--------------------|
| 1      | Olive Smith        | Null    | 1          | Alice   | 2024-04-11 12:00:00| Bob     | 2024-04-12 12:30:00|
| 2      | Noah Johnson       | 17      | 1          | Bob     | 2024-04-11 12:00:00| Cathy   | 2024-04-12 12:30:00|
| 3      | Emma Williams      | 9       | 0          | Devin   | 2024-04-11 12:00:00| Yao     | 2024-04-12 12:30:00|

#### Groups Table
| id     | name               | is_activate| creator | createdTime        | modifier| modifiedTime       |
|--------|--------------------|------------|---------|--------------------|---------|--------------------|
| 1      | Olive Smith        | 1          | Alice   | 2024-04-11 12:00:00| Bob     | 2024-04-12 12:30:00|
| 2      | Noah Johnson       | 1          | Bob     | 2024-04-11 12:00:00| Cathy   | 2024-04-12 12:30:00|
| 3      | Emma Williams      | 0          | Devin   | 2024-04-11 12:00:00| Yao     | 2024-04-12 12:30:00|

- Relationship: A user can belong to zero or one group; a group can have zero or many users.
---
### Launch services
#### Prerequisites:
- Have Docker installed and running
- Port 3308 isn't occupied yet, otherwise, you'll need to change the port for 'mysqlDB' inside the docker-compose.yml file
```
# git clone this repository
> git clone [https://github.com/CarstenYuan/lilee_fastapi.git](https://github.com/CarstenYuan/lilee_monorepo.git)
> cd lilee_fastapi

# run docker-compose.yml
> docker-compose up -d
```
- When you run docker-compose, it will populate 20 groups and 90 users.
---
### Testing
#### Using FastAPI's swagger
[Test steps on FastAPI's swagger for Lilee project](https://docs.google.com/document/d/1wrQXcUyLsucOAMaBRd_eFOyPEB4xaptl4ITwmUukbWw/edit?usp=sharing)

#### Using Vue website
```
Pending link to a file
```
