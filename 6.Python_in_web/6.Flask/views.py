from flask import jsonify, request
from flask.views import MethodView
from models import AdvModel
from settings import Session
from sqlalchemy.exc import IntegrityError
from errors import Error


class AdvView(MethodView):
    def get(self, adv_id):
        with Session() as session:
            instance = session.query(AdvModel).get(adv_id)
            if instance:
                session.commit()
                return jsonify(instance.to_dict())
            else:
                raise Error(404, 'Not Found!')

    def post(self):
        data = request.json
        with Session() as session:
            new_adv = AdvModel(owner=data['owner'], header=data['header'], description=data['description'])
            session.add(new_adv)
            try:
                session.commit()
                return jsonify(new_adv.to_dict())
            except IntegrityError:
                raise Error(400, 'Bad Request!')

    def delete(self, adv_id):
        with Session() as session:
            instance = session.query(AdvModel).get(adv_id)
            if instance:
                session.delete(instance)
                session.commit()
                return jsonify({'status': 'Deleted'})
            else:
                raise Error(404, 'Not Found!')


