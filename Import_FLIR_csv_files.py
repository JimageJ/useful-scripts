from ij 			import IJ, ImagePlus
from array 			import array
from ij.process 	import  FloatProcessor
import os
import csv

def flatten(xss):
    return [x for xs in xss for x in xs]
    
path = IJ.getDirectory("Choose Source Directory ");

files = os.listdir(path)
# Filtering only the files.
files = [f for f in files if os.path.isfile(path+'/'+f)]

for j in files:

	if j[-3:]=="csv":
		with open(path+'/'+j, 'rb') as csvfile:
			data = list(csv.reader(csvfile))
		a=0
		
		tempList=[]
		for i in range(2,len(data)-1):
			#print data[i][1:]
			tempList.append(data[i][1:])
				
		flatList=flatten(tempList)
		flatList=flatList[:-1]
		flatList=[float(i) for i in flatList]
		imageArray= array( "f", flatList)

		fp= FloatProcessor(len(data[3][1:]), len(data)-3, imageArray, None)
		Imp= ImagePlus(j, fp)
		Imp.show()
		IJ.run("mpl-inferno")
		IJ.log(j+" loaded")