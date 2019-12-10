import datetime
import TimeTracker
import pathlib

class trackerControl():

    def __init__(s):
        ## This line references the TimeTracker modules relative location, and finds
        ## the data file located within
        s.dataLocation = pathlib.PurePath(TimeTracker.locRef).parent.joinpath('data')

    def createStartPoint(s):
        ## the current time
        rightNow = datetime.datetime.now()
        dataFile = open(s.dataLocation,mode = 'w')
        dataFile.write(repr(rightNow))
        dataFile.close()

    def getStartPoint(s):
        dataFile = open(s.dataLocation,mode = 'r')
        print(dataFile.read())
        dataFile.close()
    
    def forceStartPoint(s, Year = datetime.datetime.now().year,
                           Month = datetime.datetime.now().month,
                           Day = datetime.datetime.now().day,
                           Hour = datetime.datetime.now().hour,
                           Minute = datetime.datetime.now().minute):
        timeToForce = datetime.datetime(
            year=Year,
            month=Month,
            day=Day,
            hour=Hour,
            minute=Minute
        )

        dataFile = open(s.dataLocation,mode = 'w')
        dataFile.write(repr(timeToForce))
        dataFile.close()


    def timeDeltaCurrent(s):
        dataFile = open(s.dataLocation,mode = 'r')
        contents = dataFile.read()
        dataFile.close()

        startPoint = eval(contents)

        rightNow = datetime.datetime.now()
        timeDelta = rightNow - startPoint

        return(timeDelta)