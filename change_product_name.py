import sys
import os

project_name = None;
source_dir=sys.argv[1]
new_product_name=sys.argv[2]

for word in os.listdir(source_dir):
        if word.endswith(".xcodeproj"):
			project_name = word
			print ("ProjectName:"+project_name)

pbx_proj=sys.argv[1]+"/"+project_name+"/project.pbxproj"
print ("Pbxproject:"+pbx_proj)

from mod_pbxproj import XcodeProject

project = XcodeProject.Load(pbx_proj)

project.change_product_name(new_product_name)

if project.modified:
	project.backup()
	project.saveFormat3_2()

print "Successfully changed Product Name to :", new_product_name