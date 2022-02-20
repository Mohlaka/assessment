# -------------------------------------------------------------------------------------
# Open PayslipItemCodeTypes.csv, read and to PayslipItemCodeTypes list
def getPayslipItemCodeTypes():
    # List placeholder for PayslipItemCodeTypes.csv
    PayslipItemCodeTypes = []
    with open('PayslipItemCodeTypes.csv', 'r') as file:
        next(file)
        for line in file.readlines():
            line = line.rstrip()
            PayslipItemCodeTypes.append(line)

    # Remove any duplicates
    PayslipItemCodeTypes = sorted(set(PayslipItemCodeTypes))

    return PayslipItemCodeTypes
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# Open Python Developer Assessment v1.csv, read and to PythonDeveloperAssessmentv1 list
def getPythonDeveloperAssessmentv1():
    # List placeholder for PayslipItemCodeTypes.csv
    PythonDeveloperAssessmentv1 = []
    with open('Python Developer Assessment v1.csv', 'r') as file:
        next(file)
        for line in file.readlines():
            line = line.rstrip()
            PythonDeveloperAssessmentv1.append(line)

    # Remove any duplicates
    PythonDeveloperAssessmentv1 = sorted(set(PythonDeveloperAssessmentv1))
    
    return PythonDeveloperAssessmentv1



print(getPayslipItemCodeTypes()['W512'])
