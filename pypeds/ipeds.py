import pandas as pd
import numpy as np
import os
import requests
import zipfile
import glob


# zip file factory
def zip_parser(url=None, survey=None):
    # setup the tmp path and file name
    path = "/tmp/"
    file = survey + ".zip"

    # get the data
    results = requests.get(url)
    with open(path + file, 'wb') as f:
        f.write(results.content)

    # extract the files to the path
    file = zipfile.ZipFile(path + file)
    file.extractall(path=path)

    # list the csv files for the surveys, most likely get one , but may get to with _rv for revised
    files = glob.glob(path + "*csv*")

    # return the files
    return(files)



# build a valid ipeds survey url - return a dict with a survey key and url for download
def get_hd(year):
    # assert that year is a int and length 1
    assert isinstance(year, int), "year is not an integer"
    assert year >= 2002 and year <= 2017, "year must be >=2002 and < 2017"
    # build the SURVEY id
    SURVEY = 'HD' + str(year)
    # build the url
    URL = "https://nces.ed.gov/ipeds/datacenter/data/{}.zip".format(SURVEY)
    # return the bits as a dictionary for use later
    return({'url': URL, 'survey': SURVEY})


def get_ic(year):
    # assert that year is a int and length 1
    assert isinstance(year, int), "year is not an integer"
    assert year >= 2002 and year <= 2017, "year must be >=2002 and < 2017"
    # build the SURVEY id
    SURVEY = 'IC' + str(year)
    # build the url
    URL = "https://nces.ed.gov/ipeds/datacenter/data/{}.zip".format(SURVEY)
    # return the bits as a dictionary for use later
    return({'url': URL, 'survey': SURVEY})
