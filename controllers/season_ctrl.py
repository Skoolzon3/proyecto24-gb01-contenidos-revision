from flask import render_template, request, jsonify, redirect, url_for
from database import get_next_sequence_value as get_next_sequence_value
from pymongo.collection import Collection
from models.season import Season

class SeasonCtrl:
    @staticmethod
    def render_template(db: Collection):
        seasonsReceived = db.find()
        return render_template('Season.html', seasons=seasonsReceived)

# ---------------------------------------------------------

    @staticmethod
    def addSeason(db: Collection):
        idSeason = get_next_sequence_value(db,"idSeason")
        idSeries = request.form.get('idSeries')
        season_title = request.form.get('title')
        seasonNumber = request.form.get('seasonNumber')
        totalChapters = request.form.get('totalChapters')
        chapterList = request.form.getlist('chapterList[]')
        participants = request.form.getlist('participant[]')
        trailer = request.form.get('trailer')
        if idSeason:
            season = Season(idSeason, int(idSeries), season_title, int(seasonNumber),
                            int(totalChapters), chapterList, participants, trailer)
                            
            db.insert_one(season.toDBCollection())
            return redirect(url_for('seasons'))
        else:
            return jsonify({'error': 'Season not found or not added', 'status':'404 Not Found'}), 404

# ---------------------------------------------------------
    @staticmethod
    def delete_season(db: Collection):
        if request.form.get('_method') == 'DELETE':
            idSeason = int(request.form['idSeason'])
            if idSeason and db.delete_one({'idSeason': idSeason}):
                print("Delete ok")
                return redirect(url_for('seasons'))
            else:
                print("Delete failed")
                return redirect(url_for('seasons'))
        else:
            return redirect(url_for('seasons'))

# ---------------------------------------------------------

    @staticmethod
    def put_season(db: Collection):
        if request.form.get('_method') != 'PUT':
            return jsonify({'error': 'No se puede actualizar', 'status': '400 Bad Request'}), 400
        try:
            idSeason = int(request.form.get('idSeason'))
            idSeries = request.form.get('idSeries')
            season_title = request.form.get('title')
            seasonNumber = request.form.get('seasonNumber')
            totalChapters = request.form.get('totalChapters')
            chapterList = request.form.getlist('chapterList[]')
            participants = request.form.getlist('participant[]')
            trailer = request.form.get('trailer')

            if not idSeason:
                return jsonify({'error': 'ID de temporada requerido', 'status': '400 Bad Request'}), 400

            filter = {'idSeason': idSeason}

            update_fields = {}

            if idSeries:
                update_fields['idSeries'] = int(idSeries)
            if season_title:
                update_fields['title'] = season_title
            if seasonNumber:
                update_fields['seasonNumber'] = int(seasonNumber)
            if totalChapters:
                update_fields['totalChapters'] = int(totalChapters)
            if chapterList:
                update_fields['chapterList'] = chapterList
            if participants:
                update_fields['participants'] = participants
            if trailer:
                update_fields['trailer'] = trailer

            change = {'$set': update_fields}

            result = db.update_one(filter, change)
            if result.matched_count == 0:
                return jsonify({'error': 'Temporada no encontrada', 'status': '404 Not Found'}), 404
            elif result.modified_count == 0:
                return jsonify({'message': 'La temporada ya está actualizada', 'status': '200 OK'}), 200

            # Redirigir a la lista de temporadas
            return redirect(url_for('seasons'))

        except ValueError:
            return jsonify({'error': 'Datos inválidos', 'status': '400 Bad Request'}), 400

        except Exception as e:
            return jsonify(
                {'error': f'Error interno del servidor: {str(e)}', 'status': '500 Internal Server Error'}
            ), 500

# --------------------------------

    @staticmethod
    def getSeasonById(db: Collection):
        idSeason = int(request.args.get('idSeason'))
        if idSeason:
            matching_season = db.find({'idSeason': idSeason})
            if matching_season:
                seasonFound = [
                {
                    'idSeason' : season.get('idSeason'),
                    'idSeason' : season.get('idSeries'),
                    'title' : season.get('title'),
                    'seasonNumber' : season.get('seasonNumber'),
                    'totalChapters' : season.get('totalChapters'),
                    'chapterList' : season.get('chapterList'),
                    'participants' : season.get('participants'),
                    'trailer' : season.get('trailer')
                }
                for season in matching_season
                ]
                return jsonify(seasonFound), 200
            else:
                return jsonify({'error': 'Season not found', 'status': '404 Not Found'}), 404
        else:
            return jsonify({'error': 'Missing data or incorrect method', 'status': '400 Bad Request'}), 400