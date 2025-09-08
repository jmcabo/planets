#!/usr/bin/env python3

#Created: 2025-09-03, por JMC, basado en el answer de Stack Exchange:
#    https://space.stackexchange.com/questions/41619/how-to-determine-the-distance-between-where-earth-and-mars-are-two-specific-date
#

#    export PYTHONPATH=$PYTHONPATH:~/admin/progs/Planets/AWP/src/python_tools
#
#    python3  -m pip install --break-system-packages   -r requirements.txt
#

#Old title:
#    Plot Earth-Mars relative distance for years 2040-2050

# AWP libraries
import spice_data  as sd
import spice_tools as st

import datetime
from datetime import date

# 3rd party libraries
import spiceypy as spice
import numpy as np
import matplotlib.pyplot as plt
plt.style.use( 'dark_background' )


import sys
#Remove ellipsis:
np.set_printoptions(threshold=sys.maxsize)


#Planet codes for the calc_ephemeris call
#
#    MERCURY BARYCENTER (1)  SATURN BARYCENTER (6)   MERCURY (199)
#    VENUS BARYCENTER (2)    URANUS BARYCENTER (7)   VENUS (299)
#    EARTH BARYCENTER (3)    NEPTUNE BARYCENTER (8)  MOON (301)
#    MARS BARYCENTER (4)     PLUTO BARYCENTER (9)    EARTH (399)
#    JUPITER BARYCENTER (5)  SUN (10)                TT-TDB (1000000001)


def printPlanetDatesPerYear(planet, startYear, endYear):
    auToKm = 149597870.691
    print("rs" + str(planet) + " = [")
    for year in range(startYear, endYear):
        _, _, et0, et1 = getDates(year, year+1)
        SAMPLES_PER_DAY = 1
        ets   = np.arange(et0, et1, 86400 / SAMPLES_PER_DAY)    #By day.
        rs    = st.calc_ephemeris(399, ets, 'J2000', planet)    #399 is Earth, 4 is Mars.
        rs = rs[:, :3]
        dists = np.linalg.norm(rs, axis = 1) / 149.6e6
        distsAU = [d / auToKm for d in dists]
        ts    = (ets - et0) / (3600 * 24 * 365.0) + year
        for i in range(0, len(rs)-1):
            print("    [" + str(ts[i]) + ", " + str(rs[i][0] / auToKm) + ", "
                  + str(rs[i][1] / auToKm) + ", " + str(rs[i][2] / auToKm) + "],")
    print("]")
    print("")


def getPlotData(planet, startYear, et0, et1):
    SAMPLES_PER_DAY = 1
    #debug: ets   = np.arange(et0, et1, 50000)
    ets   = np.arange(et0, et1, 86400 * SAMPLES_PER_DAY)    #By day.
    #print(ets) #debug
    #print(et0) #debug!
    rs    = st.calc_ephemeris(399, ets, 'J2000', planet)[:, :3]    #399 is Earth, 4 is Mars.
    #print(len(rs))   #debug
    dists = np.linalg.norm(rs, axis = 1) / 149.6e6
    #debug: print(ets)  #debug
    ts    = (ets - et0) / (3600 * 24 * 365.0) + startYear
    #debug:  return ts, dists
    return ts, dists, rs


def getPlotDataSubtract(planetLhs, planetRhs, startYear, et0, et1):
    ets = np.arange(et0, et1, 50000)
    #Planet 1:
    rsLhs = st.calc_ephemeris(399, ets, 'J2000', planetLhs)[ :, :3 ]    #399 is Earth, 4 is Mars.
    distsLhs = np.linalg.norm( rsLhs, axis = 1 ) / 149.6e6
    ts = ( ets - et0 ) / ( 3600 * 24 * 365.0 ) + startYear
    #Planet 2:
    rsRhs = st.calc_ephemeris(399, ets, 'J2000', planetRhs)[ :, :3 ]    #399 is Earth, 4 is Mars.
    distsRhs = np.linalg.norm(rsRhs, axis = 1) / 149.6e6
    #Subtract:
    subtractionResult = [x-y for x,y in zip(distsLhs, distsRhs)]
    return ts, subtractionResult


def getDates(startYear, endYear):
    et0   = spice.str2et( '' + str(startYear) + '-01-01' )
    et1   = spice.str2et( '' + str(endYear) + '-01-01' )
    return startYear, endYear, et0, et1


if __name__ == '__main__':
    spice.furnsh(sd.leapseconds_kernel)
    spice.furnsh(sd.de432s_kernel)
    spice.furnsh(sd.de442_kernel)

    #startYear, endYear, et0, et1 = getDates(2009, 2012)
    #startYear, endYear, et0, et1 = getDates(2020, 2022)
    #startYear, endYear, et0, et1 = getDates(2023, 2024)
    #startYear, endYear, et0, et1 = getDates(1600, 2650)
    startYear, endYear, et0, et1 = getDates(2024, 2027)

    ts1, marsDists, rsMars = getPlotData(4, startYear, et0, et1)
    ts2, venusDists, rsVenus = getPlotData(2, startYear, et0, et1)
    ts3, mercuryDists, rsMercury = getPlotData(1, startYear, et0, et1)
    #ts4, marsMinusVenus = getPlotDataSubtract(4, 2, startYear, et0, et1)
    #ts5, marsMinusMercury = getPlotDataSubtract(4, 1, startYear, et0, et1)
    #ts6, venusMinusMercury = getPlotDataSubtract(2, 1, startYear, et0, et1)
    printPlanetDatesPerYear(4, 1600, 2650)

    #print(rsMars)   #debug

    #print(len(rsMars)) #debug

    d = datetime.date.today()
    etNow = spice.str2et(str(d.isoformat()))
    tsNow = (etNow - et0) / (3600 * 24 * 365.0) + startYear

    nowTimestamps = []
    nowLine = []
    if etNow < et1 and etNow > et0:
        nowTimestamps = [tsNow - 0.0005, tsNow, tsNow + 0.0005]
        nowLine = [0, 2.2, 0]

    plt.figure(figsize = (12, 8))
    plt.plot(
             ts2, mercuryDists, 'r',
             ts1, marsDists,    'y',
             ts3, venusDists,   'b',
             nowTimestamps, nowLine, 'm',
             #ts4, marsMinusVenus, 'b',
             #ts5, marsMinusMercury, 'y',
             #ts6, venusMinusMercury, 'r'
             )
    plt.xlabel('Time (years)')
    plt.ylabel('Earth-Mars Relative Distance (AU)')
    plt.title('Earth-Mars Relative Distance ' + str(startYear) + ' to ' + str(endYear) +  ' ')
    plt.grid()
    #debug:
    #plt.show()






