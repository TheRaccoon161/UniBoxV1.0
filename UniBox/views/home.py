from pyramid.view import view_config
from pyramid.response import Response
from UniBox.infrastructure.data_manager import register_data
from UniBox.infrastructure.info_parse import *
from UniBox.infrastructure.validate_data import *
from sqlalchemy.exc import DBAPIError


@view_config(route_name='home', renderer='../templates/index.jinja2')
def home_page(request):
    from UniBox import models
    query = request.dbsession.query(models.QA)
    QAndAs = query.filter(models.QA.count >= 25)
    return {'Q_As': QAndAs}



