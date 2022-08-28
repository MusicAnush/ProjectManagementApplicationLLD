# ProjectManagementApplicationLLD
KYRO Offline assessment

I have Designed the classes as Follows:
1. Organization
2. Manager (derived from Employee)
3. ProjectTeamLead (derived from Employee)
4. Project
5. Sprint
6. Employee
7. Feature
8. UserStory
9. Task

I have desinged these classes in this way:

1. An Organization can create Managers, Employees, And projects.
2. A Manager is responsible of Managing multiple projects, and Each Manager can have multiple Project Team Leads,
Where each TL is exactly assigned one TL. Under Each TL there are multiple Teammates(Employee) who will be working to finish the respective Project.
3. The Project TLs will create the features, and the employees will create thier user stories and tasks.
4. There is another helper class like Sprint class where it says how many sprints does a project needs to be finished and also through the sprint class the list of features and theier user stories and tasks can be viewed.
