"""
This is an Employee class. this is a base class from which ProjectTeamLead, Manager classes are derived.
"""


class Employee:
    """
    This is a constructor for the Employee class.
    """
    __mapOfUserStory = dict()

    def __init__(self, empId: int = 0, name: str = "", age: int = 0, gender: str = "", designation: str = ""):
        self.__empId = empId
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__designation = designation
        self.__listOfUserStories = list[UserStory]

    def getEmpId(self):
        return self.__empId;

    def createUserStory(self, featureId, userStoryId, numberOfStoryPoints, storyStatus):
        userStory = UserStory([], numberOfStoryPoints, storyStatus, self)
        self.__listOfUserStories.append(userStory)
        self.__mapOfUserStory[userStoryId] = userStory
        ProjectTeamLead.getMapOfFeatureIdAndListOfUserStories()[featureId].append(userStory)

    def createTask(self, taskName="", expectedHoursToFinishTheTask=0,
                   taskStatus="NotStarted", userStoryId: int = 0):
        userStory = UserStory(self.__mapOfUserStory[userStoryId])
        userStory.getListOfTasks().append(Task(taskName, expectedHoursToFinishTheTask, self, taskStatus))
        self.__mapOfUserStory[userStoryId] = userStory

    def getUserStoryMap(self):
        return self.__mapOfUserStory

    """
    This is a method that  defines to view the object details in python in the format defined by us in this method.
    """

    def __str__(self):
        return "name : " + self.name + " age : " + str(
            self.age) + " gender : " + self.gender + " designation : " + self.designation + "listOfUserStories : " \
               + self.__listOfUserStories


"""
This is a ProjectTeamLead Class derived from Employee class. in this class,
 i have maintained the List of employees under the Project Team Lead.
"""


class ProjectTeamLead(Employee):
    __mapOfFeatureIdAndListOfUserStoriesUnderIt = dict()
    """
    This is a ProjectTeamLead class that is derived from the Employee base class.
    In this class i maintain the list of employees under a Project Team Lead

    """

    def __init__(self, empId: int = 0, name: str = "", age: int = 0, gender: str = "", designation: str = "",
                 listOfEmployeesUnderProjectTeamLead: list[Employee] = []):
        super().__init__(empId, name, age, gender, designation)
        self.__listOfEmployeesUnderProjectTeamLead = listOfEmployeesUnderProjectTeamLead
        self.__projectAssigned = Project()

    """
    In this method to print the Project TL (Team Lead)
    """

    def __str__(self):
        return super.__str__() + "List Of EmployeesUnderProject TeamLead : " + str(
            list[self.listOfEmployeesUnderProjectTeamLead])

    def createEmployee(self, empId: int = 0, name: str = "", age: int = 0, gender: str = "", designation: str = ""):
        self.__listOfEmployeesUnderProjectTeamLead.append(Employee(empId, name, age, gender, designation));

    def assignProject(self, project):
        self.__projectAssigned = project

    def getProjectTeamLeadId(self):
        return self.getEmpId()

    def createFeature(self, featureId: int = 0, featureSize: str = "XXL"):
        self.__projectAssigned.getListOfFeatures().append(Feature(featureId, [], self, featureSize))

    def getMapOfFeatureIdAndListOfUserStories(self):
        return self.__mapOfFeatureIdAndListOfUserStoriesUnderIt;


class Manager(Employee):
    __mapOfProjectTLIdAndProjectAssignedId = dict();
    """
    this is the constructor of the Manager Method. A manager can have list of project team leads.
    It is derived from Employee class, since a Manager is an Employee with some extra privileges.
    I have assumed that a Manager is a one who can create projects and manage multiple projects,
    and can assign exactly one project to one project Team Lead.
    """

    def __init__(self, empId: int = 0, name: str = "", age: int = 0, gender: str = "", designation: str = "",
                 listOfProjectTeamLeads: list[ProjectTeamLead] = []):
        super().__init__(empId, name, age, gender, designation)
        self.__listOfProjects = []
        self.__listOfProjectTeamLeads = listOfProjectTeamLeads

    def createProjectLead(self, empId: int = 0, empName: str = "", age: int = 0, gender: str = "",
                          designation: str = ""):
        self.__listOfProjectTeamLeads.append(ProjectTeamLead(empId, empName, age, gender, designation))

    """
    I have assumed that a manager alone can create a project. and can have multiple projects under he/she. 
    So i have maintained a list of the projects that he / she manages. 
    """

    def createProject(self, projectId: int = 0, projectName="", projectExpectedDurationForCompletionInYears: int = 0):
        project = Project(projectId, projectName, [],
                          self, projectExpectedDurationForCompletionInYears)
        self.listOfProjects.append(project)

    """
    returns the list of projects under the manager.
    """

    def getListOfProjects(self):
        return self.listOfProjects

    def assignProjectUnderProjectTl(self, projectId, ProjectTLId):
        self.__mapOfProjectTLIdAndProjectAssignedId[ProjectTLId] = projectId
        ProjectTeamLead(filter(lambda projectTl:
                               projectTl.getEmpId() == ProjectTLId, self.__listOfProjectTeamLeads)[0]) \
            .assignProject(Project(filter(lambda project: project.getProjectId() == projectId,
                                          self.__listOfProjects)[0]))


class Task:
    def __init__(self, taskName="", expectedHoursToFinishTheTask=0, taskOwner: Employee = None,
                 taskStatus="NotStarted"):
        self.__taskName = taskName
        self.__expectedHoursToFinishTheTask = expectedHoursToFinishTheTask
        self.__taskOwner = taskOwner
        self.__taskStatus = taskStatus

    def __str__(self):
        return "[taskName : " + self.__taskName + " taskOwner : " + self.__taskOwner + \
               " expectedHoursToFinishTheTask : " + self.__expectedHoursToFinishTheTask + "]"


class UserStory:
    def __init__(self, userStoryId: int = 0, listOfTasks: list[Task] = [], numberOfStoryPoints: int = 0,
                 storyStatus="", storyOwner: Employee = None):
        self.__listOfTasks = listOfTasks
        self.__numberOfStoryPoints = numberOfStoryPoints
        self.__storyStatus = storyStatus
        self.__storyOwner = storyOwner
        self.__userStoryId = userStoryId

    def getListOfTasks(self):
        return self.__listOfTasks


class Feature:
    def __init__(self, featureId: int = 0, listOfUserStories: list[UserStory] = [], featureOwner: Employee = None,
                 featureSize='XXL'):
        self.__featureId = featureId
        self.__listOfUserStories = listOfUserStories
        self.__featureOwner = featureOwner
        self.__featureSize = featureSize

    def getListOfUserStories(self):
        return self.__listOfUserStories

    def getFeatureId(self):
        return self.__featureId

    def getFeatureOwner(self):
        return self.__featureOwner

    def getFeatureSize(self):
        return self.__featureSize


class Sprint:
    def __init__(self, sprintNum: int = 0, listOfFeatures: list[Feature] = []):
        self.__sprintNum = sprintNum
        self.__listOfFeatures = listOfFeatures


"""
This is a Project Class that cannot be created by the main application directly.
The Manager is responsible in creating the objects of the projects.
"""


class Project:
    def __init__(self, projectId: int = 0, projectName="", listOfFeatures: list[Feature] = [],
                 projectManager: Manager = None,
                 projectExpectedDurationForCompletionInYears: int = 0):
        self.__projectId = projectId
        self.__projectName = projectName
        self.__listOfFeatures = listOfFeatures
        self.__projectManager = projectManager
        self.__projectExpectedDurationForCompletionInYears = projectExpectedDurationForCompletionInYears
        self.__listOfSprints = []

    def appendSprintDetails(self, sprintDetail: Sprint):
        self.__listOfSprints.append(sprintDetail);

    def getProjectId(self):
        return self.__projectId

    def getListOfFeatures(self):
        return self.__listOfFeatures


class Organization:
    def __init__(self, orgName):
        self.orgName = orgName

    def createManager(self, managerName: str = ""):
        pass

    def createEmployee(self, empId, empName, age, gender, designation):
        pass

    def createProjectLead(self, empName, age, gender, designation):
        pass
