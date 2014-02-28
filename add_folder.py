import sys
import os
project_name = None;
source_dir=sys.argv[1]
req_file=sys.argv[2]
for word in os.listdir(source_dir):
        if word.endswith(".xcodeproj"):
			project_name = word
			print ("ProjectName:"+project_name)
pbx_proj=sys.argv[1]+"/"+project_name+"/project.pbxproj"
print ("Pbxproject:"+pbx_proj)
from mod_pbxproj import XcodeProject
project = XcodeProject.Load(pbx_proj)

project_name_new = project_name[:-10]
new_group = project.get_or_create_group(project_name_new)
project.add_folder(req_file, parent=new_group)

targets = project.get_targets()

main_target = project.get_obj(targets[0])
main_source = project.get_obj(main_target['buildPhases'][0])
main_files = main_source['files']

i = 1

result = None

while i < len(targets):
	target = project.get_obj(targets[i])
	source = project.get_obj(target['buildPhases'][0])
	files = source['files']
	files_to_remove = []

	for f in files:
		current_file = project.get_obj(f)
		current_fileRef = current_file['fileRef']

		for m in main_files:
			main_file = project.get_obj(m)
			if 'fileRef' in main_file:
				if current_fileRef == main_file['fileRef']:
					files_to_remove.append(f)

	for r in files_to_remove:
		files.remove(r)

	project.modify_files(targets[i], files)
	i = i + 1

if project.modified:
  project.backup()
  project.saveFormat3_2()
print "successfully added"  