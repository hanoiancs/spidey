from karyakarsa import NovelCrawler


if __name__ == '__main__':
    crawler = NovelCrawler()
    # Get list of chapters by series slug
    # chapters = crawler.get_chapters('bumijanna-prolog')
    # print(chapters)

    # Get chapter detail
    chapter = crawler.get_chapter('bumijanna-34')
    print(chapter["content_text"])
    