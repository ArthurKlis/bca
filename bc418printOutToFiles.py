# This software helps transform information from Tanita BC-418 bca printout to digital files.

import csv


def saveBcaResultsToTxtFile(fileName, linesToAppend):
    readerRawTxtFile = open(fileName, 'w')
    try:
        for line in linesToAppend:
            readerRawTxtFile.write(line+"\n")

    finally:
        readerRawTxtFile.close()


# defining variables and setting values
bcaResults = {"bodyCompositionAnalyzerModel":"",
              "bodyCompositionAnalyzerProducent":"",
              "dataFromAnalyzer":"",
              "timeFromAnalyzer":"",
              "actualData":"",
              "actualTime":"",
              "personBodyType":"",
              "personGender":"",
              "personAge":"",
              "personHeight":"",
              "personWeight":"",
              "personBmi":"",
              "personBmrKj":"",
              "personBmrKcal":"",
              "bodyFatPercent":"",
              "bodyFatMass":"",
              "bodyFFM":"",
              "bodyTBW":"",
              "bodyVisceralFatRating":"",
              "desirableBodyFatPercent":"",
              "desirableBodyFatMass":"",
              "wholeBodyImpedance":"",
              "rightLegImpedance":"",
              "leftLegImpedance":"",
              "rightArmImpedance":"",
              "leftArmImpedance":"",
              "segAnaFatPercentRightLeg":"",
              "segAnaFatMassRightLeg":"",
              "segAnaFFMrightLeg":"",
              "segAnaPMMrightLeg":"",
              "segAnaFatPercentLeftLeg":"",
              "segAnaFatMassLeftLeg":"",
              "segAnaFFMleftLeg":"",
              "segAnaPMMleftLeg":"",
              "segAnaFatPercentRightArm":"",
              "segAnaFatMassRightArm":"",
              "segAnaFFMrightArm":"",
              "segAnaPMMrightArm":"",
              "segAnaFatPercentLeftArm":"",
              "segAnaFatMassLeftArm":"",
              "segAnaFFMleftArm":"",
              "segAnaPMMleftArm":"",
              "segAnaFatPercentTrunk":"",
              "segAnaFatMassTrunk":"",
              "segAnaFFMtrunk":"",
              "segAnaPMMtrunk":""}
bcaResults["bodyCompositionAnalyzerModel"] = 'BC-418'
bcaResults["bodyCompositionAnalyzerProducent"] = 'Tanita'
# gathering informations
bcaResults["dataFromAnalyzer"] = input('DD MMM RRRR: ')
bcaResults["timeFromAnalyzer"] = input('GG:MM: ')
bcaResults["actualData"] = input('RRRR-MM-DD: ')
bcaResults["actualTime"] = input('GG:MM: ')
bcaResults["personBodyType"] = input('BODY TYPE: ').upper()
bcaResults["personGender"] = input('GENDER: ').upper()
bcaResults["personAge"] = input('AGE: ')
bcaResults["personHeight"] = input('HEIGHT: ')
bcaResults["personWeight"] = input('WEIGHT: ')
bcaResults["personBmi"] = input('BMI: ')
bcaResults["personBmrKj"] = input('BMR kJ: ')
bcaResults["personBmrKcal"] = input('BMR kcal: ')
bcaResults["bodyFatPercent"] = input('FAT%: ')
bcaResults["bodyFatMass"] = input('FAT MASS: ')
bcaResults["bodyFFM"] = input('FFM: ')
bcaResults["bodyTBW"] = input('TBW: ')
bcaResults["bodyVisceralFatRating"] = input('VISCERAL FAT RATING: ')
bcaResults["desirableBodyFatPercent"] = input('DESIRABLE RANGE FAT%: ')
bcaResults["desirableBodyFatMass"] = input('DESIRABLE FAT MASS: ')
print('IMPEDANCE')
bcaResults["wholeBodyImpedance"] = input('Whole Body: ')
bcaResults["rightLegImpedance"] = input('Right Leg: ')
bcaResults["leftLegImpedance"] = input('Left Leg: ')
bcaResults["rightArmImpedance"] = input('Right Arm: ')
bcaResults["leftArmImpedance"] = input('Left Arm: ')
print('SEGMENTAL ANALYSIS')
print('Right Leg')
bcaResults["segAnaFatPercentRightLeg"] = input('Fat%: ')
bcaResults["segAnaFatMassRightLeg"] = input('Fat Mass: ')
bcaResults["segAnaFFMrightLeg"] = input('FFM: ')
bcaResults["segAnaPMMrightLeg"] = input('Predicted Muscle Mass: ')
print('Left Leg')
bcaResults["segAnaFatPercentLeftLeg"] = input('Fat%: ')
bcaResults["segAnaFatMassLeftLeg"] = input('Fat Mass: ')
bcaResults["segAnaFFMleftLeg"] = input('FFM: ')
bcaResults["segAnaPMMleftLeg"] = input('Predicted Muscle Mass: ')
print('Right Arm')
bcaResults["segAnaFatPercentRightArm"] = input('Fat%: ')
bcaResults["segAnaFatMassRightArm"] = input('Fat Mass: ')
bcaResults["segAnaFFMrightArm"] = input('FFM: ')
bcaResults["segAnaPMMrightArm"] = input('Predicted Muscle Mass: ')
print('Left Arm')
bcaResults["segAnaFatPercentLeftArm"] = input('Fat%: ')
bcaResults["segAnaFatMassLeftArm"] = input('Fat Mass: ')
bcaResults["segAnaFFMleftArm"] = input('FFM: ')
bcaResults["segAnaPMMleftArm"] = input('Predicted Muscle Mass: ')
print('Trunk')
bcaResults["segAnaFatPercentTrunk"] = input('Fat%: ')
bcaResults["segAnaFatMassTrunk"] = input('Fat Mass: ')
bcaResults["segAnaFFMtrunk"] = input('FFM: ')
bcaResults["segAnaPMMtrunk"] = input('Predicted Muscle Mass: ')
# processing
# saving raw information to txt file
bcaRawResultsLines = [str(bcaResults["bodyCompositionAnalyzerModel"]),
                      str(bcaResults["bodyCompositionAnalyzerProducent"]),
                      str(bcaResults["dataFromAnalyzer"])+' '+str(bcaResults["timeFromAnalyzer"]),
                      '('+str(bcaResults["actualData"])+' '+str(bcaResults["actualTime"])+')',
                      'BODY TYPE: '+str(bcaResults["personBodyType"]),
                      'GENDER: '+str(bcaResults["personGender"]),
                      'HEIGHT: '+str(bcaResults["personHeight"])+'cm',
                      'WEIGHT: '+str(bcaResults["personWeight"])+'kg',
                      'BMI: '+str(bcaResults["personBmi"]),
                      'BMR: '+str(bcaResults["personBmrKj"])+' kJ'+
                      ', '+str(bcaResults["personBmrKcal"])+' kcal',
                      'FAT%: '+str(bcaResults["bodyFatPercent"]),
                      'FAT MASS: '+str(bcaResults["bodyFatMass"])+'kg',
                      'FFM: '+str(bcaResults["bodyFFM"]),
                      'TBW: '+str(bcaResults["bodyTBW"]),
                      'VISCERAL FAT RATING: '+str(bcaResults["bodyVisceralFatRating"]),
                      'DESIRABLE RANGE',
                      'FAT%: '+str(bcaResults["desirableBodyFatPercent"]),
                      'FAT MASS: '+str(bcaResults["desirableBodyFatMass"])+'kg',
                      '', '',
                      'IMPEDANCE',
                      'Whole Body: '+str(bcaResults["wholeBodyImpedance"])+'\u03A9',
                      'Right Leg: '+str(bcaResults["rightLegImpedance"])+'\u03A9',
                      'Left Leg: '+str(bcaResults["leftLegImpedance"])+'\u03A9',
                      'Right Arm: '+str(bcaResults["rightArmImpedance"])+'\u03A9',
                      'Left Arm: '+str(bcaResults["leftArmImpedance"])+'\u03A9',
                      '', '',
                      'SEGMENTAL ANALYSIS',
                      'Right Leg',
                      'Fat% '+str(bcaResults["segAnaFatPercentRightLeg"]),
                      'Fat Mass '+str(bcaResults["segAnaFatMassRightLeg"])+'kg',
                      'FFM '+str(bcaResults["segAnaFFMrightLeg"]),
                      'Predicted Muscle Mass '+str(bcaResults["segAnaPMMrightLeg"])+'kg',
                      '',
                      'Left Leg',
                      'Fat% '+str(bcaResults["segAnaFatPercentLeftLeg"]),
                      'Fat Mass '+str(bcaResults["segAnaFatMassLeftLeg"]),
                      'FFM '+str(bcaResults["segAnaFFMleftLeg"]),
                      'Predicted Muscle Mass '+str(bcaResults["segAnaPMMleftLeg"]),
                      '',
                      'Right Arm',
                      'Fat% '+str(bcaResults["segAnaFatPercentRightArm"]),
                      'Fat Mass '+str(bcaResults["segAnaFatMassRightArm"]),
                      'FFM '+str(bcaResults["segAnaFFMrightArm"]),
                      'Predicted Muscle Mass '+str(bcaResults["segAnaPMMrightArm"]),
                      '',
                      'Left Arm',
                      'Fat% '+str(bcaResults["segAnaFatPercentLeftArm"]),
                      'Fat Mass '+str(bcaResults["segAnaFatMassLeftArm"]),
                      'FFM '+str(bcaResults["segAnaFFMleftArm"]),
                      'Predicted Muscle Mass '+str(bcaResults["segAnaPMMleftArm"]),
                      '',
                      'Trunk',
                      'Fat% '+str(bcaResults["segAnaFatPercentTrunk"]),
                      'Fat Mass '+str(bcaResults["segAnaFatMassTrunk"]),
                      'FFM '+str(bcaResults["segAnaFFMtrunk"]),
                      'Predicted Muscle Mass '+str(bcaResults["segAnaPMMtrunk"])]
saveBcaResultsToTxtFile('ascWyniki.txt', bcaRawResultsLines)
# saving needed values to csv file
header = ['data',
          'masa ciała',
          'tłuszcz w %',
          'masa tłuszczu',
          'wskaźnik tkanki trzewnej',
          'FFM', 'TBW',
          'tłuszcz w % prawa noga', 'masa tłuszczu prawa noga', 'przewidywana masa mięśni prawa noga',
          'tłuszcz w % lewa noga', 'masa tłuszczu lewa noga', 'przewidywana masa mięśni lewa noga',
          'tłuszcz w % prawe ramię', 'masa tłuszczu prawe ramię', 'przewidywana masa mięśni prawe ramię',
          'tłuszcz w % lewe ramię', 'masa tłuszczu lewe ramię', 'przewidywana masa mięśni lewe ramię',
          'tłuszcz w % tłów', 'masa tłuszczu tłów', 'przewidywana masa mięśni tłów']
data = [str(bcaResults["actualData"]), str(bcaResults["personWeight"]), str(bcaResults["bodyFatPercent"]),
        str(bcaResults["bodyFatMass"]), str(bcaResults["bodyVisceralFatRating"]), str(bcaResults["bodyFFM"]),
        str(bcaResults["bodyTBW"]), str(bcaResults["segAnaFatPercentRightLeg"]),
        str(bcaResults["segAnaFatMassRightLeg"]), str(bcaResults["segAnaPMMrightLeg"]),
        str(bcaResults["segAnaFatPercentLeftLeg"]), str(bcaResults["segAnaFatMassLeftLeg"]),
        str(bcaResults["segAnaPMMleftLeg"]), str(bcaResults["segAnaFatPercentRightArm"]),
        str(bcaResults["segAnaFatMassRightArm"]), str(bcaResults["segAnaPMMrightArm"]),
        str(bcaResults["segAnaFatPercentLeftArm"]), str(bcaResults["segAnaFatMassLeftArm"]),
        str(bcaResults["segAnaPMMleftArm"]), str(bcaResults["segAnaFatPercentTrunk"]),
        str(bcaResults["segAnaFatMassTrunk"]), str(bcaResults["segAnaPMMtrunk"])]
with open('ascWyniki.csv', 'w', encoding='UTF8', newline='') as f:
     writer = csv.writer(f)
     writer.writerow(header)
     writer.writerow(data)