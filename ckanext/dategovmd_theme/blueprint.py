from flask import Blueprint
import ckanext.dategovmd_theme.utils as utils

dategovmd = Blueprint('dategovmd', __name__)


def faq():
    return utils.show('faq')


dategovmd.add_url_rule("/faq", view_func=faq)
