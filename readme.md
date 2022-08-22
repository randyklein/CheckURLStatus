# App will check the status code for any URL provided (and subsequent redirects) and report the status code of the first and last page in the output.txt

## To Run:
* Populate list of URLs in urls.txt, each URL on it's own line.
* Run checkLinks.py
* Import output.txt into excel as CSV

## Notes
* To run in background and ignore closed terminal: `nohup python3 checkLinks.py &`
* To see status while running, check number of lines in output file using: `wc -l output.txt`
* Check file sizes while running: `ls -l --block-size=M`