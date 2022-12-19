from settings import app
from views import AdvView

app.add_url_rule('/advs/', view_func=AdvView.as_view('post'), methods=['POST', ])
app.add_url_rule('/advs/<int:adv_id>', view_func=AdvView.as_view('get'), methods=['GET', ])
app.add_url_rule('/advs/<int:adv_id>', view_func=AdvView.as_view('delete'), methods=['DELETE'], )
