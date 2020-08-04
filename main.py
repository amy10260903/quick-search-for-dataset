### Packages for UI ###
from PyQt5.QtWidgets import QApplication
from layouts.main import main as main
from layouts.label import main as label

### Packages for Main ###
import sys
import argparse

def process_command():
	parser = argparse.ArgumentParser()
	parser.add_argument('--mode', '-m', required=True, help='mode')
	return parser.parse_args()

if __name__ ==  '__main__':
	args = process_command()
	app = QApplication(sys.argv)

	if args.mode == "label":
		wid = label.MainWindow()
	elif args.mode == "init" or args.mode == "load":
		wid = main.MainWindow(args.mode)
	else:
		print('ArgumentError Raised: invalid mode')
		sys.exit()
	
	wid.show()
	sys.exit(app.exec_())