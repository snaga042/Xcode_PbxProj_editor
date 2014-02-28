import sys
import os

project_name = None
family = None
source_dir=sys.argv[1]
target_family = sys.argv[2]

for word in os.listdir(source_dir):
        if word.endswith(".xcodeproj"):
			project_name = word
			print ("ProjectName:"+project_name)

pbx_proj=sys.argv[1]+"/"+project_name+"/project.pbxproj"
print ("Pbxproject:"+pbx_proj)

from mod_pbxproj import XcodeProject
project = XcodeProject.Load(pbx_proj)

if(target_family == "iPhone"):
	family = "1"
elif(target_family == "iPad"):
	family = "2"
else:
	family = "1,2"

project.remove_targeted_device_family()
project.add_targeted_device_family(family)

if project.modified:
  project.saveFormat3_2()

print "successfully modified"