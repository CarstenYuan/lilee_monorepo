## This is a Python web server demonstration using FastAPI ,MySQL, and Vue

### Prerequisites:
- Have Docker installed and running
- Port 3308 isn't occupied yet, otherwise, you'll need to change the port for 'mysqlDB' inside the docker-compose.yml file

---
### Getting Started

1. Clone this repository:
```
git clone https://github.com/CarstenYuan/lilee_monorepo.git
cd lilee_monorepo
```
2. run docker-compose.yml
```
docker-compose up -d
```
- When you run docker-compose, it will populate 20 groups and 90 users as mock data for easier testing.

---
### Test Funcitonalities
#### Using FastAPI's swagger
[Tests on FastAPI's swagger for Lilee project (Google Doc)](https://docs.google.com/document/d/1wrQXcUyLsucOAMaBRd_eFOyPEB4xaptl4ITwmUukbWw/edit?usp=sharing)

#### Using Vue website
[Tests on Vue web page for Lilee project (Google Doc)](https://docs.google.com/document/d/1a9OkUvqk4BWjV08H2m1gKLXe-Gu8pmVkTjMyInvnzhY/edit?usp=sharing)

---
### Unittest
[Steps on how to run pytest for my APIs (README.md in lilee_monorepo/lilee_fastapi folder)](https://github.com/CarstenYuan/lilee_monorepo/tree/main/lilee_fastapi)

---
### Functionalities
#### APIs
- User Management
    - Create User: Add a new user.
    - Delete User: Remove a user by id.
    - Read Single User: Get details of a specific user by id.
    - Read All Users: List all users with an optional name filter.

- Groups Management
    - Create Group: Add a new group.
    - Delete Group: Remove a group by id. Prevent deletion if the group has at least one user and provide an appropriate error message.
    - Read Single Group: Get details of a specific group by id.
    - Read All Groups: List all groups.

- **NOT** in project requirements, but implementing them for a better experience with Vue
    - Update User: To update a user's name, group_id, or is_activate status.
    - Get Active Groups: Get all the groups with True on is_activate status.
    - Update Group: To update a group's name or is_activate status.
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
