all: ui_main.py ui_peopleEdit.py

clean:
	rm -rf ui_main.py ui_peopleEdit.py __pycache__ *.egg_info

ui_main.py: main.ui
	pyuic5 main.ui > ui_main.py

ui_peopleEdit.py: peopleEdit.ui
	pyuic5 peopleEdit.ui > ui_peopleEdit.py
