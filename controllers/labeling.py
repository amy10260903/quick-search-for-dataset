import json, os
from ruamel import yaml
from layouts.label.form import StandardItem
from PyQt5.QtGui import QColor
from datetime import datetime

def load_from_yaml(path):
	with open(path, 'r') as stream:
		loc_dict = yaml.load(stream, Loader=yaml.RoundTripLoader)
	stream.close()
	return loc_dict

def save_into_yaml(path, data):
	# Load the original data
	with open(path, 'r') as stream:
		loc_dict = yaml.load(stream, Loader=yaml.RoundTripLoader)
	
	for key in data.keys():
		if not len(data[key]) == 0:
			loc_dict[key] = data[key]

	# dump updated data and re-store
	dump = yaml.dump(
		loc_dict, default_flow_style=False, Dumper=yaml.RoundTripDumper)
	
	name, ext = os.path.splitext(path)
	timestamp = datetime.today().strftime("%Y%m%d")

	with open("{name}_{time}{ext}".format(name=name, ext=ext, time=timestamp), 'w') as stream:
		stream.write(dump)

def load_from_json(path, root_node):
	with open(path , 'r') as reader:
		abstract = []
		parent = {}
		children = {}
		count = {}
		count['total'] = 0
		count['onlist'] = 0
		count['blacklist'] = 0
		
		jlist = json.loads(reader.read())

		for node in jlist:
			count['total'] += 1

			if "abstract" in node["restrictions"] and "blacklist" not in node["restrictions"]:
				count['onlist'] += 1

				item = StandardItem(node["name"], 14, set_bold=True)
				parent[node["name"]] = node["child_ids"]
				children[node["name"]] = item
				abstract.append(node["name"])

				root_node.appendRow(item)

			elif "blacklist" in node["restrictions"]:
				count['blacklist'] += 1

			else: 
				for key, child_ids in parent.items():
					if node["id"] in child_ids:
						count['onlist'] += 1

						if key in abstract:
							item = StandardItem(node["name"], 13)
						else:
							item = StandardItem(node["name"], 12, color=QColor(155, 155, 155))
						
						children[key].appendRow(item)
						
						if len(node["child_ids"]) != 0:
							parent[node["name"]] = node["child_ids"]
							children[node["name"]] = item

						break
	reader.close()
	print("=== Count ===")              
	for key, value in count.items():
		print(key+":", value)
