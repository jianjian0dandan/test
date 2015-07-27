
import csv
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
path = r'D:\re_list.csv'
csvfile = open(path,'wb')
writer = csv.writer(csvfile)
writer.writerow(["attitudes_count","mid","uid","verified"])

with open ("re_list_result.jl") as f:
	for line in f:
   		line = json.loads(line)
   		if line.has_key("user"):
			csvfile.write(str(line["attitudes_count"]) + ",")
			csvfile.write(str(line["mid"]) + ",")
			csvfile.write(str(line["user"]["id"]) + ',')
			csvfile.write(str(line["user"]["verified"]) + '\n')
csvfile.close()
		
