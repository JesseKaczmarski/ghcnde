## GHCN-DE
# Global Historical Climate Network - Daily Data Extractor

This python program extracts daily summary data from the [NOAA Global Historical Climate Network](https://www.ncdc.noaa.gov/cdo-web/datasets) (GHCN-Daily) for a specific weather station of your choosing ([FTP Link for downloading data by year](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/)).
***
## Setup and Tutorial
1. Download the `ghcnde.py` program from this github repository, and place it wherever you like - preferrably in the directory that includes your downloaded data. For example, the following image shows the program in a directory along with the 2016 data downloaded from the [FTP website](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/). Note that the data must be extracted from the zip file.
2. Run the program from your terminal or command prompt. This command can be different depending on how you installed Python on your system. For myself, the program can be run with `python3 ghcnde.py -h` which returns the following:

    ![Help File](/assets/helpDialog.png)

3. You can see that there are two required arguments to run the program: `filename` and `station_id`. The help file gives and example of this for each. In this tutorial, I will be be using the recommendations in the help file to create and run the command `python3 ghcnde.py 2016.csv USC00053005`. It takes some time to write the data to memory given the size of the datafiles, but the program will restrict the dataframe to just the station ID you provided. A series of questions will arise and you can look at your data to make sure it is accurate:

    ![Prompt Examples](/assets/prompt1.png)
  
4. The program then shows you the data (an option which can be skipped by entering anything else but yes), and askes you to pick which elements you would like to extract (of which a list is provided). I want to pick the minimum temperature, the maximum temperature, and the percipitation: `TMIN TMAX PRCP`. The readme for this data can be found [here](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/readme-by_year.txt). After answering the remaining prompts, the data will be exported as a csv with the name of your choosing:

    ![Prompt Examples](/assets/finalPrompt.png)
    
    The following is an example of the csv that is exported:
    
    ![Prompt Examples](/assets/sheet.png)

## Help and Support

You can ask me questions about this directly by emailing: `jikaczmarski@unm.edu`, but I will assume you have read this tutorial and the information in `-h`. If you get an empty csv, it is because that weather station is not available in the data of that year.
