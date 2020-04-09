all: covid19certificate/ui_main.py covid19certificate/ui_peopleEdit.py

pkg_clean: clean
	*.egg-info

clean:
	rm -rf covid19certificate/ui_main.py covid19certificate/ui_peopleEdit.py __pycache__

covid19certificate/ui_main.py: main.ui
	pyuic5 main.ui > covid19certificate/ui_main.py

covid19certificate/ui_peopleEdit.py: peopleEdit.ui
	pyuic5 peopleEdit.ui > covid19certificate/ui_peopleEdit.py
