class Employee:
  def __init__(self, name : string, age : int, gender : string,  designation : string):
    self.name = name;
    self.age = age;
    self.gender = gender;
    self.designation = designation;

class ProjectTeamLead(Employee):
  def __init__(self, listOfEmployeesUnderProjectTeamLead : List<Employee> = []):
    self.listOfEmployeesUnderProjectTeamLead = listOfEmployeesUnderProjectTeamLead;
    
class Manager(Employee):
  def__init__(self, listOfProjectTeamLeads : List<ProjectTeamLead>):
    self.listOfProjectTeamLeads = listOfProjectTeamLeads;

class Task:
  def __init__(self, taskName : string = "", expectedHoursToFinishTheTask : int = 0, taskOwner : Employee = None, taskStatus : string = "NotStarted"):
    self.taskName = taskName;
    self.expectedHoursToFinishTheTask = expectedHoursToFinishTheTask;
    self.taskOwner = taskOwner;
    self.taskStatus = taskStatus;

class UserStory:
  def __init__(self, listOfTasks : List<Task> = [], numberOfStoryPoints : int = 0, storyStatus : string = "", storyOwner : Employee = None):
    self.listOfTasks = listOfTasks;
    self.numberOfStoryPoints = numberOfStoryPoints;
    self.storyStatus = storyStatus;
    self.storyOwner = storyOwner;
    
class Feature:
  def __init__(self, listOfUserStories, featureOwner, featureSize)

class Project:
  def __init__(self, projectName : string, listOfFeatures : List<Feature> = [], projectManager : Manager  = None):
    self.projectName = projectName;
    self.listOfFeatures = listOfFeatures;
    self.projectManager = projectManager;
