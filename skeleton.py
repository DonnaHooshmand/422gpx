#!/usr/bin/env python3


import pandas  # for, like, everything!
from geopy import distance  # for distance calculation
from GpxParser import GpxParse
from generate_directions import generate_directions
from addressLookup import *
from googleLookup import *
import sys
import datetime
import time
import gpxpy
import requests
import math  # for bearings calculation
import numpy as np  # for bearings calculation

def runner(path, api_key):
    # start with a gpx we want to generate directions from
    # extract lat and long
    # return a pandas DataFrame
    dataFrame = GpxParse(path)  # some other files available
    # add an empty street name column
    dataFrame["Street"] = ""
    # scope with 300 data points
    dataFrame = dataFrame.iloc[0:300]
    # re-set the dataFrame's index
    # binary search highly rely on correct index
    dataFrame = dataFrame.reset_index(drop=True)
    # lookup street name for each data point
    binarySearch(dataFrame, dataFrame, api_key)
    # for a contiguous series of data points with the same street, eliminate all but the first and last
    # return the revised pandas DataFrame
    filtered = df_cleanup(dataFrame)
    # figure cumulative distance from turn to turn
    # determine direction of turn (left or right)
    # compose string like "make a right turn onto Franklin Blvd."
    # write instructions to CSV
    cue_sheet = generate_directions(filtered)
    
    # cue_sheet.to_html(buf="result.html")

    return cue_sheet    # dataframe


def runner2(path, api_key):
    # Same thing as runner, but uses GoogleAPI for the second module.
    dataFrame = GpxParse(path)  # some other files available
    # add an empty street name column
    dataFrame["Street"] = ""
    # scope with 300 data points
    dataFrame = dataFrame.iloc[0:300]
    # re-set the dataFrame's index
    # binary search highly rely on correct index
    dataFrame = dataFrame.reset_index(drop=True)
    # lookup street name for each data point
    binarySearch2(dataFrame, dataFrame, api_key)
    # for a contiguous series of data points with the same street, eliminate all but the first and last
    # return the revised pandas DataFrame
    filtered = df_cleanup2(dataFrame)
    # figure cumulative distance from turn to turn
    # determine direction of turn (left or right)
    # compose string like "make a right turn onto Franklin Blvd."
    # write instructions to CSV
    cue_sheet = generate_directions(filtered)
    
    # cue_sheet.to_html(buf="result.html")

    return cue_sheet    # dataframe



# def main(path, api_key):
#     runner(path, api_key)


# if __name__ == '__main__':
#     # api_key = sys.argv[1]
#     path = "Morning_Ride.gpx"
#     api_key = "0d62ea71819844649ad97eb811da7413"
#     main(path, api_key)



