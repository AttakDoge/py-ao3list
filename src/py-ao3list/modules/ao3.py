from bs4 import BeautifulSoup
import requests as rq
from fake_useragent import UserAgent
from datetime import datetime
from typing import Tuple, List, Optional
from platformdirs import user_config_dir, user_data_dir
import os
import json
from pathlib import Path
from importlib import resources

CONFIG_DIR = user_config_dir("py-ao3list", "AttakDoge")

def sayhi():
    print("ao3")

def init() -> None:
    os.makedirs(CONFIG_DIR, exist_ok=True)
    config_file = Path(os.path.join(CONFIG_DIR, "config.json"))
    if not config_file.exists():
        try:
            default_config = resources.files("py-ao3list").joinpath("default-config.json")
            default_data = default_config.read_text(encoding="utf-8")
            config_file.write_text(default_data, encoding="utf-8")
        except ModuleNotFoundError:
            default_config = resources.files("py-ao3list").joinpath("default-config.json")
            default_data = default_config.read_text(encoding="utf-8")
            config_file.write_text(default_data, encoding="utf-8")
    print(CONFIG_DIR)
    #with open(config_file, "r", encoding="utf-8") as f:
    #    config = json.load()
    #    data_dir = config["data-directory"]
    

def get_ao3(work:str, to_get:Optional[List[int]] = None) -> Tuple[List, List[int]]:
    if to_get is None:
        to_get = [1,1,1,1,1]
    try: # see if input passed is just numbers
        work_id = int(work)
    except: # assume its a link
        try:
            work_id = int(work.split(sep="/")[4]) # get id from the link
        except Exception as e:
            print(f"The input \"{work}\" was not detected to be an acceptable link or work ID. Error:")
            raise
    link = f"https://archiveofourown.org/works/{work_id}"
    work_request = rq.get(link, headers={'User-Agent':str(UserAgent().chrome) + "(py-ao3listBot/1.0; +https://github.com/AttakDoge/py-ao3list)"})
    work_contents = BeautifulSoup(work_request.content, "html.parser")
    #print(work_contents)

    results = []
    errors = []
    
    if to_get[0] == 1:
        try: # get title
            title = str(work_contents.find("h2", {"class": "title heading"}).contents[0]).strip("\n").strip()
            results.append(title)
            errors.append(0)
        except Exception as e:
            title = f"N/A, likely failed to fetch {e}"
            errors.append(1)
    
    if to_get[1] == 1:
        try: # get author
            author = str(work_contents.find("h3", {"class": "byline heading"}).find("a").contents[0])
            results.append(author)
            errors.append(0)
        except Exception as e:
            author = f"N/A, likely failed to fetch {e}"
            errors.append(1)
    
    if to_get[2] == 1:
        try: # get number of chapters
            chapters = str(work_contents.find("dd", {"class": "chapters"}).contents[0]).split(sep="/")[0]
            results.append(chapters)
            errors.append(0)
        except Exception as e:
            chapters = f"N/A, likely failed to fetch {e}"
            errors.append(1)
    
    if to_get[3] == 1:
        try: # get last updated date
            last_updated = str(work_contents.find("dd", {"class": "status"}).contents[0])
            last_updated = datetime.strptime(last_updated, "%Y-%m-%d")
            results.append(last_updated)
            errors.append(0)
        except Exception as e:
            last_updated = f"N/A, likely failed to fetch {e}"
            errors.append(1)
    
    if to_get[4] == 1:
        try: # get first published date
            first_posted = str(work_contents.find("dd", {"class": "published"}).contents[0])
            first_posted = datetime.strptime(first_posted, "%Y-%m-%d")
            results.append(first_posted)
            errors.append(0)
        except Exception as e:
            first_posted = f"N/A, likely failed to fetch {e}"
            errors.append(1)
    
    results.append(work_id)
    results.append(link)
    return results, errors
    


#results, errors = get_ao3("https://archiveofourown.org/works/37004083/chapters/92324395")
#print(results)
#print(errors)