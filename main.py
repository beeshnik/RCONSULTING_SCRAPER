from utils.utils import Utils
from scrapers.scraper import Scraper
from scrapers.builders.func.yield_scraper import yield_scraper


def main():
    scraper: Scraper = yield_scraper()
    scraper.process()
    scraper.driver.quit()


if __name__ == "__main__":
    Utils.load_settings()
    main()
