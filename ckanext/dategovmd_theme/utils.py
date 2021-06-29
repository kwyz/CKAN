
import ckantoolkit as tk


def faq_show():
    return tk.render('custom/faq.html')


def articles_show():
    return tk.render('custom/articles.html')


def article_show(id):
    return tk.render('custom/article.html')
