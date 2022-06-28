from flask import Blueprint,render_template,url_for
import testdb
from pybo.models import Question
bp = Blueprint('main',__name__,url_prefix='/')
from werkzeug.utils import redirect

@bp.route('/')
def index():
    return redirect(url_for('question.questionlist'))

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)

@bp.route('/hello')
def hello_pybo():
    return 'hello,pybo'

@bp.route('/dbtest')
def dbtest():
    testdb.getall_question()
    return '성공'
