all: attestation/ui_main.py attestation/ui_peopleEdit.py

clean:
	rm -rf attestation/ui_main.py attestation/ui_peopleEdit.py __pycache__ *.egg-info

attestation/ui_main.py: main.ui
	pyuic5 main.ui > attestation/ui_main.py

attestation/ui_peopleEdit.py: peopleEdit.ui
	pyuic5 peopleEdit.ui > attestation/ui_peopleEdit.py
