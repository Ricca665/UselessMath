import UselessMath

def test():
    SqrtRange.Calculate(testfirstnumber, testsecondnumber, logFile, clearLog, True)
    SqrtRange.CalculateWOLogging(testfirstnumber, testsecondnumber, True)
    SqrtRange.CalculateWithThreads(testfirstnumber, testsecondnumber, logFile, clearLog, True, 2)
    SqrtRange.CalculateWOLoggingWithThreads(testfirstnumber, testsecondnumber, True, 2)