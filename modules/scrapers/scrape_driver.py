import pandas as pd
from pathlib import Path

from modules.helpers.logger import log
from modules.scrapers.kegg.search import kegg_search
from modules.scrapers.brenda.search import brenda_search

from modules.scrapers.kegg.scrape import kegg_scrape
from modules.scrapers.brenda.scrape import brenda_scrape


def create_missing_list(kegg_keywords, brenda_keywords):
    """kegg_keywords and brenda_keywords must be a list | returns a set()"""
    whitelist_path = Path("modules/scrapers/whitelist.csv")
    blacklist_path = Path("modules/scrapers/blacklist.csv")

    # makeing the sets of ECs
    white_list = set(pd.read_csv(whitelist_path)["ec"])
    black_list = set(pd.read_csv(blacklist_path)["ec"])
    brenda_list = brenda_search(brenda_keywords)
    kegg_list = kegg_search(kegg_keywords)
    # TODO: this must be implemented
    # prev_list = helpers.get_scraped_list()
    prev_list = set()
    # this are all the results that came back from kegg and brenda
    new_list = brenda_list | kegg_list

    # combining the lists
    # note: the parentecies are crucial here for order of operations
    master_list = (new_list | white_list) - (prev_list | black_list)

    # Logging the lists for debugging purposes
    log(f"white_list len: {len(white_list)}", "debug")
    log(f"black_list len: {len(black_list)}", "debug")
    log(f"brenda_list len: {len(brenda_list)}", "debug")
    log(f"kegg_list len: {len(kegg_list)}", "debug")
    log(f"new_list len: {len(new_list)} will be used", "debug")
    return master_list


def scrape_all(list_of_ecs):
    kegg_data = kegg_scrape(list_of_ecs)
    brenda_data = brenda_scrape(list_of_ecs)

    print(f"kegg_data: {len(kegg_data)}, brenda_data: {len(brenda_data)}")
    return None
