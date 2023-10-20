# About
App will check the status code for any URL provided (and subsequent redirects) and report the status code of the first and last page in the output.txt

## System Requirements
* Python 3
* Python PIP

## To Run:
* Download soure, extract to folder, navigate into the project folder
* Populate list of URLs in urls.txt, each URL on it's own line.
* Install required python packages using `pip install -r requirements.txt`
* Run checkLinks.py
* Import output.txt into excel as CSV

## Notes
* To run in background and ignore closed terminal: `nohup python3 checkLinks.py &`
* To see status while running, check number of lines in output file using: `wc -l output.txt`
* Check file sizes while running: `ls -l --block-size=M`
