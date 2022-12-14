from flask import current_app, Blueprint, jsonify, render_template, request

from .apis.imdb_api import get_movie_summary
from .authentication import token_required

movies_summary = Blueprint('movies_summary', __name__, template_folder='templates/movies', static_folder='static')

@movies_summary.route('/get_movie_data', methods=['GET'])
@token_required
def get_movie_data():
    if not request.args.get('q'):
        current_app.logger.error("No query provided")
        return "No query provided", 400
    
    query = {
        'q': request.args.get('q')
    }

    movies_json = get_movie_summary(querystring=query)
    # movies_json = ""

    return movies_json, 200
