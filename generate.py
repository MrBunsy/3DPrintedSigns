'''
Copyright Luke Wallin 2020

This file is part of Luke Wallin's 3DPrintedTrains project.

The 3DPrintedTrains project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The 3DPrintedTrains project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with The 3DPrintedTrains project.  If not, see <https:www.gnu.org/licenses/>.
'''

import os
from multiprocessing import Pool
import multiprocessing
from pathlib import Path
import argparse

Path("out").mkdir(parents=True, exist_ok=True)

class Sign():

    def __init__(self, name, base, details, colours, base_colour, mmu=True, height=4, layer_height=0.2):
        self.name = name
        self.base = base
        self.details = details
        self.colours = colours
        self.base_colour = base_colour
        self.mmu = mmu
        self.height = height
        self.layer_height = layer_height

    def getBaseJob(self, colour):
        baseJob = JobDescription("generate_sign.scad", "{}_{}".format(self.name, colour))
        baseJob.addVariable("BASE_FILE", self.base)
        baseJob.addVariable("DETAIL_FILES", self.details)
        baseJob.addVariable("COLOURS", self.colours)
        baseJob.addVariable("BASE_COLOUR", self.base_colour)
        baseJob.addVariable("LAYER_HEIGHT", self.layer_height)
        baseJob.addVariable("MMU", self.mmu)
        return baseJob

    def getJobs(self):
        jobs = []
        if self.mmu:

            baseJob = self.getBaseJob(self.colours[0])
            baseJob.addVariable("GEN_ITEM", 0)
            jobs.append(baseJob)

            for i in range(1,len(self.details)+1):
                colourJob = self.getBaseJob(self.colours[i])
                colourJob.addVariable("GEN_ITEM",i)
                jobs.append(colourJob)
        return jobs



class JobDescription():
    def __init__(self, scad, filename):
        self.variables = {}
        self.scad = scad
        self.filename = filename

    def addVariable(self, name, value):
        if isinstance(value, str):
            self.variables[name] = "\\\"{}\\\"".format(value)
        elif type(value)==bool:
            self.variables[name] = "true" if value else "false"
        elif isinstance(value, list):
            #just hope it's a list of strings, otherwise I cba to refactor this
            self.variables[name] = "[\\\"" + ("\\\",\\\"".join(value)) + "\\\"]"
        else:
            self.variables[name] = value

    def addVariables(self, dict):
        '''
        given dict of ["variable name"] = value, add them all
        :param dict:
        :return:
        '''
        for key in dict:
            self.addVariable(key, dict[key])

    def getVariableString(self):
        return " ".join(["-D {varname}={varvalue}".format(varname=key,varvalue=self.variables[key]) for key in self.variables])

    def do(self):
        cmd =  "openscad -o out/{filename}.stl {variablestring} {scad}".format(filename = self.filename, variablestring = self.getVariableString(), scad=self.scad)
        print(cmd)
        os.system(cmd)
        print("finished {}".format(self.filename))

def executeJob(job):
    job.do()


if __name__ == '__main__':
    #
    # parser = argparse.ArgumentParser(description="Generate all variants of a parametric object")
    # parser.add_argument("--class66", action='store_true')
    # parser.add_argument("--couplings", action='store_true')
    # parser.add_argument("--wagons", action='store_true')
    # parser.add_argument("--mwa", action='store_true')
    # args = parser.parse_args()
    # TODO fetch height and layer height

    height = 4
    layer_height = 0.2

    signs = [
        # Sign("ExampleName", "ShapeOfSign.svg", ["BlackBits.svg", "RedBits.svg"], ["backgroundColour", "Black", "Red"], "ColourOfBackOfSign", MultiMaterial?, height, layer_height),
        # Sign("TrainWarning","771_background.svg",["771_inner.svg","771_outline.svg"],["white","black","red"], "white", True,height,layer_height),
        # Sign("EndOfBicycleLane","965.svg",["965_inner.svg"],["blue","white"], "white", True, height, layer_height),
        # Sign("BicycleWarning","950_base.svg",["950_inner.svg","950_outer.svg"],["white","black","red"], "white", True,height,layer_height),
        # Sign("MiniRoundabout","611.1_base.svg",["611.1_inner.svg"],["blue","white"], "white", True,height,layer_height*2),
        # Sign("BicyleLane", "956_base.svg", ["956_white.svg"], ["blue", "white"], "white", True, height,layer_height * 2),
        # Sign("NoUTurns", "614_base.svg", ["614_red.svg", "614_black.svg"], ["white", "red", "black"], "white", True, height, layer_height * 2),
        # Sign("TramsOnly", "953.1_base.svg", ["953.1_white.svg"], ["blue", "white"], "white", True, height, layer_height * 2),
        # Sign("Derestricted", "671_base.svg", ["671_black.svg"], ["white", "black"], "white", True, height, layer_height * 2),
        # Sign("NoStopping", "642_base.svg", ["642_red.svg"], ["blue", "red"], "red", True, height, layer_height * 2),
#        Sign("NoEntry", "616_base.svg", ["616_red.svg"], ["white", "red"], "white", True, height, layer_height * 2),
#         Sign("EndOfHGVRestriction", "622.2_base.svg", ["622.2_grey.svg", "622.2_black.svg"], ["white", "grey", "black"], "white", True, height, layer_height * 2),
#         Sign("BlueArrow", "610_base.svg", ["610_blue.svg"], ["white", "blue"], "white", True, height, layer_height * 2),
#         Sign("LeftArrow", "609_base.svg", ["609_blue.svg"], ["white", "blue"], "white", True, height, layer_height * 2),
       # Sign("Priority", "615_base.svg", ["615_red.svg", "615_black.svg"], ["white", "red", "black"], "white", True, height, layer_height * 2),
        #Sign("NoMotorVehicles", "619_base.svg", ["619_red.svg", "619_black.svg"], ["white", "red", "black"], "white", True, height, layer_height * 2),
        Sign("Limit30", "670V30_base.svg", ["670V30_red.svg", "670V30_black.svg"], ["white", "red", "black"], "white",True, height, layer_height * 2),
    ]
    jobs = []

    for sign in signs:
        jobs.extend(sign.getJobs())

    p = Pool(multiprocessing.cpu_count()-1)
    p.map(executeJob, jobs)