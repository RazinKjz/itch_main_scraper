import asyncio
from itch_main.database import create_details_table, get_game_links
from itch_main.scraper import scrape_all_games

async def main():
    """Main function to initialize database and start scraping."""
    create_details_table()
    links = get_game_links()
    await scrape_all_games(links)

if __name__ == "__main__":
    asyncio.run(main())

