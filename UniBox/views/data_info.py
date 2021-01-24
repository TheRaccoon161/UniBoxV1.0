from pyramid.view import view_config
from pyramid.response import Response
from UniBox.infrastructure.data_manager import register_data
from UniBox.infrastructure.info_parse import *
from UniBox.infrastructure.validate_data import *
from sqlalchemy.exc import DBAPIError


@view_config(route_name='home_info', renderer='../templates/test.jinja2')
def make_data(request):
    from UniBox import models
    query = request.dbsession.query(models.QA)
    QAndAs = query.filter(models.QA.count >= 25)

    data_info = parse_data_info(request.params)
    data_info.info_id = ''

    if not validate(data_info):
        data_info = get_valid_personal_data(data_info)
        data_info.order_id = 'Ошибка'
    else:
        order_id = register_data(request, data_info)
        data_info.order_id = 'Заявка отправлена!'

    return {'data_info': data_info, 'Q_As': QAndAs}
