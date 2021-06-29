import ckan.plugins as p
import ckan.plugins.toolkit as tk
import requests
import datetime
from ckan.lib.plugins import DefaultTranslation
from ckanext.dategovmd_theme.blueprint import dategovmd as dategovmd_blueprint
import ckan.lib.helpers as helpers

total_pages = 0


def faq_items():
    response = requests.get(tk.config.get('infoportal.faq_url'))
    response_data = response.json()
    faq_items = response_data['items']
    return faq_items


def articles_items():
    articles_url = tk.config.get(
        'infoportal.articles_url') + "&Page=" + str(get_current_articles_page())
    response = requests.get(articles_url)
    response_data = response.json()
    articles_items = response_data['items']
    total_pages = response_data['totalPages']
    return articles_items


def get_article_data_by_id(full_url):
    id = full_url[slice(full_url.rindex("/") + 1, len(full_url), 1)]
    article_url = tk.config.get('infoportal.article_url') + id
    response = requests.get(article_url)
    response_data = response.json()
    return response_data


def datetime_to_human_headable_format(datetime_str):
    format = '%Y-%m-%dT%H:%M:%S'  # The format
    datetime_str_converted = datetime.datetime.strptime(datetime_str, format)
    UTC_datetime_timestamp = float(datetime_str_converted.strftime("%s"))
    local_date_converted = datetime.date.fromtimestamp(UTC_datetime_timestamp)
    local_time_converted = datetime.datetime.fromtimestamp(
        UTC_datetime_timestamp).time()
    return {"date": local_date_converted, "time": local_time_converted}


def get_current_articles_page():
    full_url = helpers.current_url()
    try:
        page = full_url[slice(full_url.rindex("?page=") + 6, len(full_url), 1)]
        return int(page)
    except:
        helpers.redirect_to("/news?page=1")
        return 1


def get_total_pages():
    return int(total_pages)

def get_translation(data, lang):
    if len(data[lang]):
        return data[lang]
    elif not len(data['ro']) and len(data["en"]):
        return data['en']
    elif not len(data['en']) and len(data["ro"]):
        return data['ro']
    elif not len(data['en']) and not len(data["ro"]):
        return data['ru']


class Dategovmd_ThemePlugin(p.SingletonPlugin, DefaultTranslation):
    p.implements(p.ITranslation)
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')

    # IBlueprint
    def get_blueprint(self):
        return [dategovmd_blueprint]

    # ITemplateHelpers
    def get_helpers(self):
        return {'faq_list': faq_items,
                'articles_items': articles_items,
                'datetime_to_readable':  datetime_to_human_headable_format,
                'get_article_data_by_id': get_article_data_by_id,
                'get_translation': get_translation,
                'get_current_articles_page': get_current_articles_page,
                'get_total_pages': get_total_pages
                }
