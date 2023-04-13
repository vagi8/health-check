import time
import yaml
import requests
import json
from urllib.parse import urlparse
import logging
import sys
import traceback
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def main():
    # initializing loggers
    log = logging.getLogger('main')
    debugHandler = setup_logger('main.debug','debug.log',level=logging.DEBUG)
    log.info("Loggers Initialized Successfully")

    endpointsFilepath = input("Please Input the full local file path for the HTTP endpoint yaml file - ")
    # Read the YAML file with the list of endpoints
    try:
        with open(endpointsFilepath) as f:
            endpoints = yaml.safe_load(f)
    except Exception:
        log.error("Invalid YAML file/format")
        debugHandler.debug(traceback.format_exc())
        sys.exit()
    availabiltyCountMap = {}

    while True:
        for endpoint in endpoints:
            parsed_url = urlparse(endpoint['url'])
            domain = parsed_url.netloc
            availabiltyCount = availabiltyCountMap.get(domain,[0,0])
            try:
                method = endpoint.get('method', 'GET')
                headers = endpoint.get('headers', {})
                body = endpoint.get('body', None)
                response = requests.request(
                    method, endpoint['url'], headers=headers, json=json.loads(body) if body else None, timeout=0.5)
                availabiltyCount[1] += 1
                if response.status_code >= 200 and response.status_code < 300 and response.elapsed.total_seconds() < 0.5:
                    availabiltyCount[0] += 1
                availabiltyCountMap[domain] = availabiltyCount
                debugHandler.debug("domain - {}, status - {}, latency - {}".format(domain,response.status_code,response.elapsed.total_seconds()))
            except Exception:
                log.error("Unknow error in processing endpoint - {}".format(str(endpoint)))
                debugHandler.debug(traceback.format_exc())


        # Log availability to console
        for domain, availabiltyCount in availabiltyCountMap.items():
            availability_percentage = (availabiltyCount[0]/availabiltyCount[1])*100
            debugHandler.debug("Domain - {}, Success - {}, Total - {}, Availability - {}".format(domain,availabiltyCount[0],availabiltyCount[1],availability_percentage))
            print("{} has {}% availability percentage".format(domain,availability_percentage))

        # Countinuesly loop over every 15 seconds    
        time.sleep(15)

if __name__== "__main__":
    main()