import transaction
from .. import models


def register_data(request, data_info):
    data = models.Data(
        name=data_info.name,
        phone=data_info.phone_number,
        email=data_info.email
    )
    request.dbsession.add(data)
    transaction.commit()