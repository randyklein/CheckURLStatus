import requests
from ratelimit import limits, RateLimitException, sleep_and_retry

#rate limit to one call every 3 seconds
@sleep_and_retry
@limits(calls=1, period=3)
def get_status_code(url):
    try:
        r = requests.get(url)
        print ("Processing " + url)

        if len(r.history) > 0:
            chain = ""
            code = r.history[0].status_code
            final_url = r.url
            final_code = r.status_code
            for resp in r.history:
                chain += resp.url + " | "
            return str(code) + '\t' + str(len(r.history)) + '\t' + chain + '\t' + final_url + '\t' + str(final_code)
        else:
            return str(r.status_code) + '\t\t\t\t'
    except requests.ConnectionError:
        print("Error: failed to connect.")
        return '0\t\t\t\t'


input_file = 'urls-family.txt'
output_file = 'output-family.txt'

with open(output_file, 'w') as o_file:
    o_file.write('URL\tStatus\tNumber of redirects\tRedirect Chain\tFinal URL\tFinal Status Code\n')
    f = open(input_file, "r")
    lines = f.read().splitlines()
    for line in lines:
        code = get_status_code(line)
        o_file.write(line + "\t" + str(code) + "\n")
    f.close()