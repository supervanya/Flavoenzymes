# from modules.scrapers import scrape_kegg
# from modules.scrapers import scrape_brenda
# from modules.bruce_sorter import BruceSorter_485


# print(dir(scrape_brenda))
# scrape_brenda.printThis('khskd')
# import modules.scrapers
# print(scrape_brenda)

from GLOBALS import KEYWORDS

from modules.scrapers.scrape_driver import create_missing_list
from modules.scrapers.scrape_driver import scrape_all
from modules.scrapers.scrape_driver import write_out


def main():
    # takes into account the whitelist and blacklist
    missing_list = create_missing_list(kegg_keywords=KEYWORDS, brenda_keywords=KEYWORDS)

    # scrapes brenda and kegg
    # {'ec:1.14.13.2', 'ec:1.18.1.3', 'ec:1.97.1.4', 'ec:2.3.1.115', 'ec:2.3.1.116'}
    # {'ec:1.5.8.1', 'ec:1.14.14.87', 'ec:1.17.3.2', 'ec:1.14.14.47', 'ec:1.14.12.17', 'ec:2.4.1.159', 'ec:2.4.1.81', 'ec:1.14.19.45', 'ec:2.7.11.23', 'ec:1.14.13.8', 'ec:2.8.1.8', 'ec:4.2.1.167', 'ec:2.1.1.82', 'ec:1.3.8.4', 'ec:2.4.1.17', 'ec:1.14.14.88', 'ec:1.7.2.5', 'ec:1.3.8.11', 'ec:3.4.24.B17', 'ec:1.14.14.46', 'ec:1.14.13.53', 'ec:5.6.2.1', 'ec:6.3.2.2', 'ec:2.7.10.2', 'ec:1.14.14.90', 'ec:3.2.1.35', 'ec:3.4.11.2', 'ec:2.7.11.18', 'ec:1.1.1.145', 'ec:1.14.15.8', 'ec:1.13.11.31', 'ec:3.2.1.161', 'ec:1.3.1.9', 'ec:2.3.1.115', 'ec:2.4.2.25', 'ec:3.5.1.5', 'ec:1.14.12.18', 'ec:2.1.1.231', 'ec:2.4.1.240', 'ec:2.7.9.1', 'ec:1.14.11.23', 'ec:1.12.7.2', 'ec:1.5.99.15', 'ec:1.5.8.4', 'ec:1.1.1.195', 'ec:1.14.14.1', 'ec:1.11.2.1', 'ec:4.4.1.5', 'ec:1.1.1.62', 'ec:1.14.18.1', 'ec:1.10.5.1', 'ec:2.1.1.B75', 'ec:1.14.15.15', 'ec:1.5.8.3', 'ec:1.5.5.2', 'ec:3.2.2.4', 'ec:2.1.1.83', 'ec:3.2.1.167', 'ec:1.14.19.76', 'ec:3.4.22.1', 'ec:1.16.1.9', 'ec:1.14.13.29', 'ec:3.3.2.10', 'ec:3.1.3.9', 'ec:1.4.3.3', 'ec:1.1.1.219', 'ec:5.4.99.9', 'ec:5.4.3.2', 'ec:1.14.13.231', 'ec:2.1.1.46', 'ec:1.2.7.4', 'ec:1.3.1.56', 'ec:1.14.99.34', 'ec:2.4.2.30', 'ec:3.2.1.B31', 'ec:2.1.1.42', 'ec:1.14.14.94', 'ec:1.14.14.81', 'ec:1.6.5.5', 'ec:2.4.2.35', 'ec:1.6.5.9', 'ec:3.1.1.8', 'ec:3.1.4.35', 'ec:1.1.2.3', 'ec:2.3.1.41', 'ec:1.1.99.31', 'ec:1.19.1.1', 'ec:2.7.1.26', 'ec:1.13.11.24', 'ec:1.19.6.1', 'ec:3.1.3.53', 'ec:2.1.1.B76', 'ec:1.7.7.2', 'ec:1.3.8.14', 'ec:1.3.8.1', 'ec:2.4.1.234', 'ec:3.4.24.B20', 'ec:1.14.13.21', 'ec:1.3.8.12', 'ec:3.4.21.91', 'ec:2.3.1.116', 'ec:1.8.2.3', 'ec:2.8.2.4', 'ec:1.3.8.13', 'ec:2.4.1.218', 'ec:2.1.1.76', 'ec:3.2.1.B44', 'ec:2.1.1.84', 'ec:1.14.14.133', 'ec:1.14.13.52', 'ec:3.1.4.11', 'ec:3.2.1.20', 'ec:7.1.1.2', 'ec:2.7.7.49', 'ec:1.14.20.5', 'ec:3.4.23.46', 'ec:1.3.99.12', 'ec:4.1.1.36', 'ec:2.4.2.56', 'ec:1.17.7.3', 'ec:1.14.11.9', 'ec:2.4.1.239', 'ec:2.4.1.1', 'ec:1.14.14.82', 'ec:2.1.1.342', 'ec:2.3.1.20', 'ec:3.1.1.7', 'ec:1.14.14.89', 'ec:2.7.1.48', 'ec:1.14.11.22', 'ec:2.3.1.85', 'ec:3.2.1.18', 'ec:3.4.21.5', 'ec:2.7.11.22', 'ec:1.1.1.239', 'ec:2.1.1.267', 'ec:2.8.2.25', 'ec:1.97.1.4', 'ec:1.3.8.6', 'ec:3.4.24.74', 'ec:1.14.99.22', 'ec:3.2.1.40', 'ec:2.5.1.17', 'ec:2.1.1.169', 'ec:2.4.2.12', 'ec:1.18.6.1', 'ec:1.14.13.89', 'ec:1.14.14.55', 'ec:1.14.13.39', 'ec:1.14.19.19', 'ec:2.1.1.88', 'ec:1.3.1.109', 'ec:1.97.1.12', 'ec:2.4.1.253', 'ec:2.1.1.155', 'ec:1.18.1.3', 'ec:2.3.1.180', 'ec:1.5.5.1', 'ec:3.5.1.88', 'ec:1.1.1.213', 'ec:2.4.1.35', 'ec:2.4.1.B71', 'ec:5.6.1.6', 'ec:1.1.1.146', 'ec:3.4.22.61', 'ec:3.4.17.23', 'ec:2.1.1.350', 'ec:2.7.10.1', 'ec:1.2.1.12', 'ec:2.4.1.358', 'ec:2.1.1.75', 'ec:2.1.1.6', 'ec:2.4.1.170', 'ec:2.7.1.127', 'ec:1.1.1.64', 'ec:2.5.1.18', 'ec:1.18.1.4', 'ec:1.6.2.4', 'ec:2.1.1.232', 'ec:1.7.1.B1', 'ec:1.5.8.2', 'ec:1.3.1.45', 'ec:2.1.1.150', 'ec:1.3.8.9', 'ec:1.3.8.7', 'ec:2.8.2.27', 'ec:2.8.2.1', 'ec:1.6.5.10', 'ec:5.5.1.6', 'ec:1.13.11.33', 'ec:1.1.1.184', 'ec:7.6.2.2', 'ec:1.3.8.3', 'ec:1.3.1.77', 'ec:1.3.1.6', 'ec:1.14.14.14', 'ec:3.2.1.21', 'ec:1.3.8.10', 'ec:2.7.7.7', 'ec:7.2.1.2', 'ec:1.13.11.34', 'ec:3.1.1.1', 'ec:1.1.1.21', 'ec:2.4.1.B53', 'ec:1.6.5.2', 'ec:2.4.1.91', 'ec:4.1.1.22', 'ec:4.2.99.18', 'ec:3.3.2.9', 'ec:1.3.8.5', 'ec:1.6.5.11', 'ec:2.8.2.28', 'ec:2.4.1.115', 'ec:1.3.8.8', 'ec:1.1.5.3', 'ec:1.1.1.252', 'ec:1.3.5.1', 'ec:5.6.2.2', 'ec:3.4.15.1', 'ec:1.16.1.8', 'ec:3.4.24.35', 'ec:1.14.20.6', 'ec:1.1.1.51', 'ec:2.1.1.B74', 'ec:3.4.24.59', 'ec:2.8.1.6', 'ec:2.4.1.237', 'ec:2.8.2.26', 'ec:1.3.1.46', 'ec:2.3.1.54', 'ec:1.18.1.2', 'ec:1.18.1.1', 'ec:3.1.1.4', 'ec:2.3.1.173', 'ec:2.1.1.104'}
    scraped_results = scrape_all(missing_list)

    # write it out to a file
    if len(scraped_results) > 0:
        write_out(scraped_results)


if __name__ == "__main__":
    main()
