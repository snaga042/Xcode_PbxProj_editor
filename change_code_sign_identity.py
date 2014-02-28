import sys
import os

project_name = None;
source_dir=sys.argv[1]
new_code_sign_identity=sys.argv[2]

for word in os.listdir(source_dir):
        if word.endswith(".xcodeproj"):
			project_name = word
			print ("ProjectName:"+project_name)

pbx_proj=sys.argv[1]+"/"+project_name+"/project.pbxproj"
print ("Pbxproject:"+pbx_proj)

from mod_pbxproj import XcodeProject

project = XcodeProject.Load(pbx_proj)

project.change_code_sign_identity(new_code_sign_identity)

if project.modified:
	project.saveFormat3_2()

print "Successfully changed Code Signing Identity to :", new_code_sign_identity