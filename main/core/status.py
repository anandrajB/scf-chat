from enum import Enum

# BASE ENUM VALUES FOR STATUS CODE AND MESSAGES 

class Base_Values(Enum):
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"
    SWR = "something went wrong"
    UTGD = "unable to find matching data , please try again"
    SCC = "Successfully created configuration"

