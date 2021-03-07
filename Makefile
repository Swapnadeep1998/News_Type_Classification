update:
	sudo apt-get update && sudo apt-get upgrade

conda-env:
	conda env create -f environment.yml --force
	#python3 setup.py install

create-env:
	pip3 install -r requirements.txt
	python3 setup.py install

