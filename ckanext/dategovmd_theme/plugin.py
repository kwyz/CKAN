import ckan.plugins as p
import ckan.plugins.toolkit as tk
import requests
from ckan.lib.plugins import DefaultTranslation
from ckanext.dategovmd_theme.blueprint import dategovmd as dategovmd_blueprint


def faq_items():
    response = requests.get(tk.config.get('infoportal.faq_url'))
    response_data = response.json()
    faq_items = response_data['items']
    return faq_items


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
        return {'faq_list': faq_items}
