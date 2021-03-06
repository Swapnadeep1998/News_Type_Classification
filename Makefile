update:
	sudo apt-get update && sudo apt-get upgrade

conda-env:
	conda env create -f environment.yml --force

create-env:
	pip3 install -r requirements.txt

