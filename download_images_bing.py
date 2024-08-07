from icrawler.builtin import BingImageCrawler

bing_crawler = BingImageCrawler(storage={'root_dir': './images/puppies'})
bing_crawler.crawl(keyword='puppies', max_num=5)
