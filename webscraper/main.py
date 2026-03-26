from scrapers.traits_scraper import TraitsScraper
base_url = "https://2e.aonprd.com"


def main():
    traits = TraitsScraper()
    traits.scrape('https://2e.aonprd.com/Traits.aspx')


if __name__ == "__main__":
    main()
