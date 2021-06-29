from flask import Blueprint
import ckanext.dategovmd_theme.utils as utils

dategovmd = Blueprint('dategovmd', __name__)


def faq():
    return utils.faq_show()


def articles():
    return utils.articles_show()

def article(id):
    return utils.article_show(id)


dategovmd.add_url_rule("/faq", view_func=faq)
dategovmd.add_url_rule("/news", view_func=articles)
dategovmd.add_url_rule("/news/<id>", view_func=article)
