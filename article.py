from newspaper import Article
import json, traceback

def summarize_article_at_url(link):
    try:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()

        return { 
            "status": True,
            "title": article.title,
            "authors" : article.authors,
            "publish_date" : article.publish_date,
            "keywords" : article.keywords,
            "summary" : article.summary,
            "url": link
        }
    except:
        return { "status": False, "error": traceback.format_exc() }
