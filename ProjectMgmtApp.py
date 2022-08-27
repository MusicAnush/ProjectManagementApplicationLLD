class Employee:
    def __init__(self, name: str = "", age: int = 0, gender: str = "", designation: str = ""):
        self.name = name;
        self.age = age;
        self.gender = gender;
        self.designation = designation;


class ProjectTeamLead(Employee):
    def __init__(self, listOfEmployeesUnderProjectTeamLead: list[Employee] = []):
        self.listOfEmployeesUnderProjectTeamLead = listOfEmployeesUnderProjectTeamLead;


class Manager(Employee):
    def __init__(self, listOfProjectTeamLeads: list[ProjectTeamLead] = []):
        self.listOfProjectTeamLeads = listOfProjectTeamLeads;


class Task:
    def __init__(self, taskName="", expectedHoursToFinishTheTask=0, taskOwner: Employee = None,
                 taskStatus="NotStarted"):
        self.taskName = taskName;
        self.expectedHoursToFinishTheTask = expectedHoursToFinishTheTask;
        self.taskOwner = taskOwner;
        self.taskStatus = taskStatus;


class UserStory:
    def __init__(self, listOfTasks: list[Task] = [], numberOfStoryPoints: int = 0,
                 storyStatus="", storyOwner: Employee = None):
        self.listOfTasks = listOfTasks;
        self.numberOfStoryPoints = numberOfStoryPoints;
        self.storyStatus = storyStatus;
        self.storyOwner = storyOwner;


class Feature:
    def __init__(self, listOfUserStories: list[UserStory] = [], featureOwner: Employee = None, featureSize='XXL'):
        self.listOfUserStories = listOfUserStories;
        self.featureOwner = featureOwner;
        self.featureSize = featureSize;


class Project:
    def __init__(self, projectName="", listOfFeatures: list[Feature] = [], projectManager: Manager = None):
        self.projectName = projectName;
        self.listOfFeatures = listOfFeatures;
        self.projectManager = projectManager;
