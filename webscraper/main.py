from scrapers.traits_scraper import TraitsScraper
from sqlalchemy import create_engine, text
base_url = "https://2e.aonprd.com"


def main():
    engine = create_engine("postgresql+psycopg://postgres:example@100.75.243.92:5432/pathfinder-2e")
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE TRAITS (x int, y int)"))
        conn.commit()
    # traits = TraitsScraper()
    # traits.scrape('https://2e.aonprd.com/Traits.aspx')


if __name__ == "__main__":
    main()
