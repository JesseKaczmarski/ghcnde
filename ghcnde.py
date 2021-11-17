import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Enter the file location and name here with the .csv at the end (e.g. 2016.csv, if in the same directory, or an entire path can be entered)")
parser.add_argument("station_id", help="Enter a single station ID (e.g. Fort Collins' is USC00053005)")
#parser.add_argument("--elements", help="Enter a list of elements you would like to look at")
args = parser.parse_args()
print("You have selected Station ID Number: ", args.station_id, " to be extracted from ", args.filename)
conf1 = input("Is the above information correct? [y/n]\n")
if conf1 in ['Yes','YES','yes','y','yEs','yeS']:
    print("Thank you. Writing the data to memory...")
    df = pd.read_csv(args.filename,names=['id','date','element','dvalue','mflag','qflag','sflag','obstime'])
    df = df[df['id']==args.station_id]
    df['date'] = pd.to_datetime(df['date'],format='%Y%m%d')

    conf2 = input("The data has successfully loaded to memeory. Would you like to see a sample of the data? [y/n]\n")
    if conf2 in ['Yes','YES','yes','y','yEs','yeS']:
        print("---------------------------------------------------------------")
        print(df.head())
    print(" ")
    print(" ")
    print(" ")
    print("There are several element options for this station: ",df['element'].unique())

    elementTargets = input("List the 4-letter elements you would like to extract with a space to seperate them: ").split(' ')

    print("You have selected: ", elementTargets)
    conf3 = input("The program will now convert the data from long format to wide format. Are the elements you selected correct? [y/n]\n")
    if conf3 in ['Yes','YES','yes','y','yEs','yeS']:
        dfPivot = df.pivot('date','element','dvalue')
        dfFinal = dfPivot[dfPivot.columns.intersection(elementTargets)]
        newFileName = input('What would you like your new csv file to be called (include .csv at the end)?')
        dfFinal.to_csv(newFileName)

    else:
        print("Please try again. There is a tutorial on the Github page if you need additional help.")

else:
    print("Please try again. There is a tutorial on the Github page if you need additional help.")
