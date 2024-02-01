import httpx
import asyncio
from parsel import Selector

class AsyncEnglishScrapper:
    URL = "https://test-english.com/level-b2/"
    HEADERS={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'identity'
    }
    LINKXPATH='//div[@class="pill hoverable"]/a/@href'

    async def get_page(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            response = await client.get(url=self.URL)
            links=await self.scrape_url(response=response)
            return links

    async def scrape_url(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINKXPATH).extract()
        # for link in links:
        #     print(link)
        return links
if __name__ == "__main__":
    scraper = AsyncEnglishScrapper()
    asyncio.run(scraper.get_page())