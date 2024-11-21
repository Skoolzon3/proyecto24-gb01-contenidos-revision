from flask import render_template, request, jsonify, redirect, url_for
from database import get_next_sequence_value as get_next_sequence_value
from datetime import datetime
from pymongo.collection import Collection
from models.movie import Movie

class MovieCtrl:
    @staticmethod
    def render_template(db: Collection):
        moviesReceived = db.find()
        return render_template('Movie.html', movies=moviesReceived)

# ---------------------------------------------------------

    @staticmethod
    def addMovie(db: Collection):
        idMovie = get_next_sequence_value(db,"idMovie")
        movieTitle = request.form.get('title')
        duration = request.form.get('duration')
        urlVideo = request.form.get('urlVideo')
        urlTitlePage = request.form.get('urlTitlePage')
        releaseDate = request.form.get('releaseDate')
        synopsis = request.form.get('synopsis')
        description = request.form.get('description')
        language = request.form.getlist('language[]')
        category = request.form.getlist('category[]')
        character = request.form.getlist('character[]')
        participant = request.form.getlist('participant[]')
        trailer = request.form.get('trailer')
        isSuscription = request.form.get('isSuscription')

        if idMovie:
            movie = Movie(idMovie, movieTitle, urlVideo, urlTitlePage, releaseDate, synopsis, description,
                          isSuscription, duration, language, category, character, participant, trailer)
            db.insert_one(movie.toDBCollection())
            return redirect(url_for('movies'))
        else:
            return jsonify({'error': 'Película no añadida', 'status':'404 Not Found'}), 404

# ---------------------------------------------------------

    @staticmethod
    def getMovieById(db: Collection):
        idMovie = int(request.args.get('idMovie'))

        if idMovie:
            matchingMovie = db.find({'idMovie': idMovie})

            if matchingMovie:
                movieFound = [
                {
                    'idMovie' : movie.get('idMovie'),
                    'title' : movie.get('title'),
                    'urlVideo' : movie.get('urlVideo'),
                    'urlTitlePage' : movie.get('urlTitlePage'),
                    'releaseDate' : movie.get('releaseDate'),
                    'synopsis' : movie.get('synopsis'),
                    'description' : movie.get('description'),
                    'isSuscription' : movie.get('isSuscription'),
                    'duration' : movie.get('duration'),
                    'language' : movie.get('language'),
                    'category' : movie.get('category'),
                    'character' : movie.get('character'),
                    'participant' : movie.get('participant'),
                    'trailer' : movie.get('trailer'),
                }
                for movie in matchingMovie
                ]
                return jsonify(movieFound), 200

            else:
                return jsonify({'error': 'Película no encontrada', 'status': '404 Not Found'}), 404

        else:
            return jsonify({'error': 'Falta de datos o método incorrecto', 'status': '400 Bad Request'}), 400

# ---------------------------------------------------------

    @staticmethod
    def getMovieCharacters(movieCollection: Collection, characterCollection: Collection):
        idMovie = int(request.args.get('idMovie'))

        if idMovie:
            matchingMovie = movieCollection.find({'idMovie': idMovie})

            if matchingMovie:
                charactersList = []

                for movie in matchingMovie:
                    characterIds = movie.get('character', [])

                    for idCharacter in characterIds:

                        if idCharacter and idCharacter.strip().isdigit():
                            matchingCharacter = characterCollection.find({'idCharacter': int(idCharacter)})

                            for character in matchingCharacter:
                                charactersList.append({
                                    'idCharacter': character.get('idCharacter'),
                                    'name': character.get('name'),
                                    'participant': character.get('participant'),
                                    'age': character.get('age')
                                })

                        else:
                            print(f"idCharacter inválido encontrado: {idCharacter}")
                return jsonify(charactersList), 200

            else:
                return jsonify({'error': 'Película no encontrada', 'status': '404 Not Found'}), 404

        else:
            return jsonify({'error': 'Falta de datos o método incorrecto', 'status': '400 Bad Request'}), 400

# ---------------------------------------------------------

    @staticmethod
    def getMovieParticipants(movieCollection, participantsCollection):
        idMovie = int(request.args.get('idMovie'))

        if idMovie:
            matchingMovie = movieCollection.find({'idMovie': idMovie})

            if matchingMovie:
                participantsList = []

                for movie in matchingMovie:
                    participantsIds = movie.get('participant', [])

                    for idParticipant in participantsIds:

                        if idParticipant and idParticipant.strip().isdigit():
                            matchingParticipant = participantsCollection.find({'idParticipant': int(idParticipant)})

                            for participant in matchingParticipant:
                                participantsList.append({
                                    'name': participant.get('name'),
                                    'surname': participant.get('surname'),
                                    'age': participant.get('age'),
                                    'nationality': participant.get('nationality')
                                })

                        else:
                            print(f"idParticipant inválido encontrado: {idParticipant}")
                return jsonify(participantsList), 200
            else:
                return jsonify({'error': 'Película no encontrada', 'status': '404 Not Found'}), 404
        else:
            return jsonify({'error': 'Falta de datos o método incorrecto', 'status': '400 Bad Request'}), 400

# ---------------------------------------------------------

    @staticmethod
    def getMovieByTitle(db: Collection):
        title = request.args.get('title')

        if title:
            matching_movie = db.find({'title': {'$regex': title, '$options': 'i'}})

            if db.count_documents({'title': {'$regex': title, '$options': 'i'}}) > 0:
                movieFound = [
                {
                    'idMovie' : movie.get('idMovie'),
                    'title' : movie.get('title'),
                    'urlVideo' : movie.get('urlVideo'),
                    'urlTitlePage' : movie.get('urlTitlePage'),
                    'releaseDate' : movie.get('releaseDate'),
                    'synopsis' : movie.get('synopsis'),
                    'description' : movie.get('description'),
                    'isSuscription' : movie.get('isSuscription'),
                    'duration' : movie.get('duration'),
                    'language' : movie.get('language'),
                    'category' : movie.get('category'),
                    'character' : movie.get('character'),
                    'participant' : movie.get('participant'),
                    'trailer' : movie.get('trailer'),
                }
                for movie in matching_movie
                ]
                return jsonify(movieFound), 200

            else:
                return jsonify({'error': 'No se han encontrado películas', 'status': '404 Not Found'}), 404

        else:
            return jsonify({'error': 'Falta de datos o método incorrecto', 'status': '400 Bad Request'}), 400

# ---------------------------------------------------------

    @staticmethod
    def getMovieByReleaseDate(db: Collection):
        releaseDate_str = request.args.get('releaseDate')

        if releaseDate_str:
            releaseDate = datetime.strptime(releaseDate_str, '%Y-%m-%d').date()
            matching_movies = db.find({'releaseDate': str(releaseDate)})

            if db.count_documents({'releaseDate': str(releaseDate)}) > 0:
                movieFound = [
                {
                    'idMovie' : movie.get('idMovie'),
                    'title' : movie.get('title'),
                    'urlVideo' : movie.get('urlVideo'),
                    'urlTitlePage' : movie.get('urlTitlePage'),
                    'releaseDate' : movie.get('releaseDate'),
                    'synopsis' : movie.get('synopsis'),
                    'description' : movie.get('description'),
                    'isSuscription' : movie.get('isSuscription'),
                    'duration' : movie.get('duration'),
                    'language' : movie.get('language'),
                    'category' : movie.get('category'),
                    'character' : movie.get('character'),
                    'participant' : movie.get('participant'),
                    'trailer' : movie.get('trailer'),
                }
                for movie in matching_movies
                ]
                return jsonify(movieFound), 200

            else:
                return jsonify({'error': 'Película no encontrada', 'status': '404 Not Found'}), 404

        else:
            return jsonify({'error': 'Falta de datos o método incorrecto', 'status': '400 Bad Request'}), 400

# ---------------------------------------------------------

    @staticmethod
    def getAllMovies(db: Collection):
        allMovies = db.find()

        if db.count_documents({}) > 0:
            movies_list = [
                {
                    'idMovie' : movie.get('idMovie'),
                    'title' : movie.get('title'),
                    'urlVideo' : movie.get('urlVideo'),
                    'urlTitlePage' : movie.get('urlTitlePage'),
                    'releaseDate' : movie.get('releaseDate'),
                    'synopsis' : movie.get('synopsis'),
                    'description' : movie.get('description'),
                    'isSuscription' : movie.get('isSuscription'),
                    'duration' : movie.get('duration'),
                    'language' : movie.get('language'),
                    'category' : movie.get('category'),
                    'character' : movie.get('character'),
                    'participant' : movie.get('participant'),
                    'trailer' : movie.get('trailer'),
                }
                for movie in allMovies
            ]
            return jsonify(movies_list), 200

        else:
            return jsonify({'error': 'No existen películas insertadas', 'status': '404 Not Found'}), 404

# ---------------------------------------------------------

    @staticmethod
    def delete_movie(db: Collection):
        if request.form.get('_method') == 'DELETE':
            idMovie = int(request.form['idMovie'])
            if idMovie and db.delete_one({'idMovie': idMovie}):
                print("Delete ok")
                return redirect(url_for('movies'))
            else:
                print("Delete failed")
                return redirect(url_for('movies'))
        else:
            return redirect(url_for('movies'))

# ---------------------------------------------------------

    @staticmethod
    def put_movie(db: Collection):
        if request.form.get('_method') != 'PUT':
            return jsonify({'error': 'No se puede actualizar', 'status': '400 Bad Request'}), 400
        try:
            idMovie = int(request.form.get('idMovie'))
            movieTitle = request.form.get('title')
            duration = request.form.get('duration')
            urlVideo = request.form.get('urlVideo')
            urlTitlePage = request.form.get('urlTitlePage')
            releaseDate = request.form.get('releaseDate')
            synopsis = request.form.get('synopsis')
            description = request.form.get('description')
            language = request.form.getlist('language[]')
            category = request.form.getlist('category[]')
            character = request.form.getlist('character[]')
            participant = request.form.getlist('participant[]')
            trailer = request.form.get('trailer')
            isSuscription = request.form.get('isSuscription')

            if not idMovie:
                return jsonify({'error': 'Identificador de película requerido', 'status': '400 Bad Request'}), 400

            filter = {'idMovie': idMovie}

            updateFields = {}

            if movieTitle:
                updateFields['title'] = movieTitle
            if duration:
                updateFields['duration'] = int(duration)
            if urlVideo:
                updateFields['urlVideo'] = urlVideo
            if urlTitlePage:
                updateFields['urlTitlePage'] = urlTitlePage
            if releaseDate:
                updateFields['releaseDate'] = releaseDate
            if synopsis:
                updateFields['synopsis'] = synopsis
            if description:
                updateFields['description'] = description
            if language:
                updateFields['language'] = language
            if category:
                updateFields['category'] = category
            if character:
                updateFields['character'] = character
            if participant:
                updateFields['participant'] = participant
            if trailer:
                updateFields['trailer'] = trailer
            if isSuscription:
                updateFields['isSuscription'] = isSuscription

            change = {'$set': updateFields}
            result = db.update_one(filter, change)

            if result.matched_count == 0:
                return jsonify({'error': 'Película no encontrada', 'status': '404 Not Found'}), 404

            elif result.modified_count == 0:
                return jsonify({'message': 'La película ya está actualizada', 'status': '200 OK'}), 200

            return redirect(url_for('movies'))

        except ValueError:
            return jsonify({'error': 'Datos inválidos', 'status': '400 Bad Request'}), 400

        except Exception as e:
            return jsonify(
                {'error': f'Error interno del servidor: {str(e)}', 'status': '500 Internal Server Error'}
            ), 500

# --------------------------------
