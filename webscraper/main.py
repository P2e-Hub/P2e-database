from scrapers.traits_parser import TraitsParser
from sqlalchemy import create_engine
from orm.trait import Base
base_url = "https://2e.aonprd.com"

def main():
    traits = TraitsParser()
    # traits.parse(url="https://2e.aonprd.com/Traits.aspx")
    # engine = create_engine(
    #     "postgresql+psycopg://postgres:example@100.75.243.92:5432/pathfinder-2e"
    # )
    # with engine.connect() as conn:
    #     Base.metadata.create_all(engine)
    #     # conn.execute(text("CREATE TABLE TRAITS (x int, y int)"))
    #     conn.commit()
    # traits = TraitsScraper()
    # traits.scrape('https://2e.aonprd.com/Traits.aspx')


if __name__ == "__main__":
    main()
