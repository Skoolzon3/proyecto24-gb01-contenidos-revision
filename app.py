from flask import Flask, render_template
from flask_cors import CORS

import database as dbase
from controllers.category_ctrl import CategoryCtrl
from controllers.chapter_ctrl import ChapterCtrl
from controllers.character_ctrl import CharacterCtrl
from controllers.movie_ctrl import MovieCtrl
from controllers.participant_ctrl import ParticipantCtrl
from controllers.season_ctrl import SeasonCtrl
from controllers.series_ctrl import SeriesCtrl
from controllers.trailer_ctrl import TrailerCtrl

db = dbase.conexion_mongodb()

app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # CORS restringido al origen React

# -------------------------------------------------------------------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------------------------------------------------------------------------------

@app.route('/movies')
def movies():
    return MovieCtrl.render_template(db['movies'])


@app.route('/movies', methods=['POST'])
def addMovie():
    return MovieCtrl.add_movie(db['movies'])


@app.route('/movies', methods=['DELETE'])
def deleteMovieForm():
    return MovieCtrl.delete_movie_form(db['movies'])


@app.route('/movies/<idMovie>', methods=['DELETE'])
def deleteMovie(idMovie):
    return MovieCtrl.delete_movie(db['movies'], idMovie)


@app.route('/movies', methods=['PUT'])
def putMovieForm():
    return MovieCtrl.put_movie_form(db['movies'])


@app.route('/movies/<idMovie>', methods=['PUT'])
def putMovie(idMovie):
    return MovieCtrl.put_movie(db['movies'], idMovie)


@app.route('/movies/<idMovie>', methods=['GET'])
def getMovieById(idMovie):
    return MovieCtrl.get_movie_by_id(db['movies'], idMovie)


@app.route('/movies/title', methods=['GET'])
def getMovieByTitle():
    return MovieCtrl.get_movie_by_title(db['movies'])


@app.route('/movies/release', methods=['GET'])
def getMovieByReleaseDate():
    return MovieCtrl.get_movie_by_release_date(db['movies'])


@app.route('/movies/all', methods=['GET'])
def getAllMovies():
    return MovieCtrl.get_all_movies(db['movies'])


@app.route('/movies/characters', methods=['GET'])
def getMovieCharacters():
    return MovieCtrl.get_movie_characters(db['movies'], db['characters'])


@app.route('/movies/participants', methods=['GET'])
def getMovieParticipants():
    return MovieCtrl.get_movie_participants(db['movies'], db['participants'])


@app.route('/movies/<idMovie>/trailer', methods=['PUT'])
def putTrailerIntoMovie(idMovie):
    return MovieCtrl.put_trailer_into_movie(db['movies'], db['trailers'], idMovie)


@app.route('/movies/<idMovie>/trailer', methods=['DELETE'])
def deleteTrailerFromMovie(idMovie):
    return MovieCtrl.delete_trailer_from_movie(db['movies'], idMovie)


@app.route('/movies/<idMovie>/categories', methods=['PUT'])
def putCategoryIntoMovie(idMovie):
    return MovieCtrl.put_category_into_movie(db['movies'], db['categories'], idMovie)


@app.route('/movies/<idMovie>/categories', methods=['DELETE'])
def deleteCategoryFromMovie(idMovie):
    return MovieCtrl.delete_category_from_movie(db['movies'], idMovie)

# -------------------------------------------------------------------------------------------------------

@app.route('/trailers')
def trailers():
    return TrailerCtrl.render_template(db['trailers'])


@app.route('/trailers', methods=['POST'])
def addTrailer():
    return TrailerCtrl.add_trailer(db['trailers'])


@app.route('/trailers', methods=['DELETE'])
def deleteTrailerForm():
    return TrailerCtrl.delete_trailer_form(db['trailers'])


@app.route('/trailers', methods=['PUT'])
def putTrailerForm():
    return TrailerCtrl.put_trailer_form(db['trailers'])


@app.route('/trailers/<idTrailer>', methods=['DELETE'])
def deleteTrailer(idTrailer):
    return TrailerCtrl.delete_trailer(db['trailers'], idTrailer)


@app.route('/trailers/<idTrailer>', methods=['PUT'])
def putTrailer(idTrailer):
    return TrailerCtrl.put_trailer(db['trailers'], idTrailer)


@app.route('/trailers/<idTrailer>', methods=['GET'])
def getTrailerById(idTrailer):
    return TrailerCtrl.get_trailer_by_id(db['trailers'], idTrailer)


@app.route('/trailers/<idTrailer>/categories', methods=['PUT'])
def putCategoryIntoTrailer(idTrailer):
    return TrailerCtrl.put_category_into_trailer(db['trailers'], db['categories'], idTrailer)


@app.route('/trailers/<idTrailer>/categories', methods=['DELETE'])
def deleteCategoryFromTrailer(idTrailer):
    return TrailerCtrl.delete_category_from_trailer(db['trailers'], idTrailer)

# -------------------------------------------------------------------------------------------------------

@app.route('/chapters')
def chapters():
    return ChapterCtrl.render_template(db['chapters'])


@app.route('/chapters', methods=['POST'])
def addChapter():
    return ChapterCtrl.add_chapter(db['chapters'])


@app.route('/chapters', methods=['DELETE'])
def deleteChapterForm():
    return ChapterCtrl.delete_chapter_form(db['chapters'])


@app.route('/chapters', methods=['PUT'])
def putChapterForm():
    return ChapterCtrl.put_chapter_form(db['chapters'])


@app.route('/chapters/<idChapter>', methods=['DELETE'])
def deleteChapter(idChapter):
    return ChapterCtrl.delete_chapter(db['chapters'], idChapter)


@app.route('/chapters/<idChapter>', methods=['PUT'])
def putChapter(idChapter):
    return ChapterCtrl.put_chapter(db['chapters'], idChapter)


@app.route('/chapters/<idChapter>', methods=['GET'])
def getChapterById(idChapter):
    return ChapterCtrl.get_chapter_by_id(db['chapters'], idChapter)

# -------------------------------------------------------------------------------------------------------

@app.route('/seasons')
def seasons():
    return SeasonCtrl.render_template(db['seasons'])


@app.route('/seasons', methods=['POST'])
def addSeason():
    return SeasonCtrl.add_season(db['seasons'])


@app.route('/seasons', methods=['PUT'])
def putSeasonForm():
    return SeasonCtrl.put_season_form(db['seasons'])


@app.route('/seasons', methods=['DELETE'])
def deleteSeasonForm():
    return SeasonCtrl.delete_season_form(db['seasons'])


@app.route('/seasons/<idSeason>', methods=['PUT'])
def putSeason(idSeason):
    return SeasonCtrl.put_season(db['seasons'], idSeason)


@app.route('/seasons/<idSeason>', methods=['DELETE'])
def deleteSeason(idSeason):
    return SeasonCtrl.delete_season(db['seasons'], idSeason)


@app.route('/seasons/<idSeason>', methods=['GET'])
def getSeasonById(idSeason):
    return SeasonCtrl.get_season_by_id(db['seasons'], idSeason)


@app.route('/seasons/chapters', methods=['GET'])
def getSeasonChapters():
    return SeasonCtrl.get_season_chapters(db['seasons'], db['chapters'])


@app.route('/seasons/characters', methods=['GET'])
def getSeasonCharacters():
    return SeasonCtrl.get_season_characters(db['seasons'], db['characters'])


@app.route('/seasons/participants', methods=['GET'])
def getSeasonParticipants():
    return SeasonCtrl.get_season_participants(db['seasons'], db['participants'])


@app.route('/seasons/<idSeason>/trailer', methods=['PUT'])
def putTrailerIntoSeasons(idSeason):
    return SeasonCtrl.put_trailer_into_season(db['seasons'], db['trailers'], idSeason)


@app.route('/seasons/<idSeason>/trailer', methods=['DELETE'])
def deleteTrailerFromSeason(idSeason):
    return SeasonCtrl.delete_trailer_from_season(db['seasons'], idSeason)


@app.route('/seasons/<idSeason>/categories', methods=['PUT'])
def putCategoryIntoSeason(idSeason):
    return SeasonCtrl.put_category_into_season(db['seasons'], db['categories'], idSeason)


@app.route('/seasons/<idSeason>/categories', methods=['DELETE'])
def deleteCategoryFromSeason(idSeason):
    return SeasonCtrl.delete_category_from_season(db['seasons'], idSeason)


@app.route('/seasons/<idSeason>/chapters', methods=['PUT'])
def putChapterIntoSeason(idSeason):
    return SeasonCtrl.put_chapter_into_season(db['seasons'], db['chapters'], idSeason)


@app.route('/seasons/<idSeason>/chapters', methods=['DELETE'])
def deleteChapterFromSeason(idSeason):
    return SeasonCtrl.delete_chapter_from_season(db['seasons'], idSeason)

# -------------------------------------------------------------------------------------------------------

@app.route('/categories')
def categories():
    return CategoryCtrl.render_template(db['categories'])


@app.route('/categories', methods=['POST'])
def addCategory():
    return CategoryCtrl.add_category(db['categories'])


@app.route('/categories/all', methods=['GET'])
def getAllCategories():
    return CategoryCtrl.get_all_categories(db['categories'])


@app.route('/categories/<idCategory>', methods=['GET'])
def getCategoryById(idCategory):
    return CategoryCtrl.get_category_by_id(db['categories'], idCategory)

# No se borran ni se modifican categorías.

@app.route('/categories/content', methods=['GET'])
def getContentByCategory():
    return CategoryCtrl.get_content_by_category(db['categories'], db['movies'], db['series'])


# -------------------------------------------------------------------------------------------------------

@app.route('/participants')
def participants():
    return ParticipantCtrl.render_template(db['participants'])


@app.route('/participants', methods=['POST'])
def addParticipant():
    return ParticipantCtrl.add_participant(db['participants'])


@app.route('/participants', methods=['PUT'])
def putParticipantForm():
    return ParticipantCtrl.put_participant_form(db['participants'])


@app.route('/participants', methods=['DELETE'])
def deleteParticipantForm():
    return ParticipantCtrl.delete_participant_form(db['participants'])


@app.route('/participants/<idParticipant>', methods=['PUT'])
def putParticipant(idParticipant):
    return ParticipantCtrl.put_participant(db['participants'], idParticipant)


@app.route('/participants/<idParticipant>', methods=['DELETE'])
def deleteParticipant(idParticipant):
    return ParticipantCtrl.delete_participant(db['participants'], idParticipant)


@app.route('/participants/<idParticipant>', methods=['GET'])
def getParticipantById(idParticipant):
    return ParticipantCtrl.get_participant_by_id(db['participants'], idParticipant)


@app.route('/participants/name', methods=['GET'])
def getParticipantByName():
    return ParticipantCtrl.get_participant_by_name(db['participants'])


@app.route('/participants/surname', methods=['GET'])
def getParticipantBySurname():
    return ParticipantCtrl.get_participant_by_surname(db['participants'])


@app.route('/participants/age', methods=['GET'])
def getParticipantByAge():
    return ParticipantCtrl.get_participant_by_age(db['participants'])


@app.route('/participants/content', methods=['GET'])
def getContentByParticipant():
    return ParticipantCtrl.get_content_by_participant(db['participants'], db['movies'], db['series'])

@app.route('/participants/all', methods=['GET'])
def getAllParticipants():
    return ParticipantCtrl.get_all_participants(db['participants'])

# -------------------------------------------------------------------------------------------------------

@app.route('/characters')
def characters():
    return CharacterCtrl.render_template(db['characters'])


@app.route('/characters', methods=['POST'])
def addCharacter():
    return CharacterCtrl.add_character(db['characters'])


@app.route('/characters', methods=['PUT'])
def putCharacterForm():
    return CharacterCtrl.put_character_form(db['characters'])


@app.route('/characters', methods=['DELETE'])
def deleteCharacterForm():
    return CharacterCtrl.delete_character_form(db['characters'])


@app.route('/characters/<idCharacter>', methods=['PUT'])
def putCharacter(idCharacter):
    return CharacterCtrl.put_character(db['characters'], idCharacter)


@app.route('/characters/<idCharacter>', methods=['DELETE'])
def deleteCharacter(idCharacter):
    return CharacterCtrl.delete_character(db['characters'], idCharacter)


@app.route('/characters/<idCharacter>', methods=['GET'])
def getCharacterById(idCharacter):
    return CharacterCtrl.get_character_by_id(db['characters'], idCharacter)


@app.route('/characters/name', methods=['GET'])
def getCharacterByName():
    return CharacterCtrl.get_character_by_name(db['characters'])


@app.route('/characters/age', methods=['GET'])
def getCharacterByAge():
    return CharacterCtrl.get_character_by_age(db['characters'])


@app.route('/characters/all', methods=['GET'])
def getAllCharacters():
    return CharacterCtrl.get_all_characters(db['characters'])


@app.route('/characters/content', methods=['GET'])
def getContentByCharacter():
    return CharacterCtrl.get_content_by_character(db['characters'], db['movies'], db['series'])

# -------------------------------------------------------------------------------------------------------

@app.route('/series')
def series():
    return SeriesCtrl.render_template(db['series'])


@app.route('/series', methods=['POST'])
def addSeries():
    return SeriesCtrl.add_series(db['series'])


@app.route('/series/all', methods=['GET'])
def getAllSeries():
    return SeriesCtrl.get_all_series(db['series'])


@app.route('/series/title', methods=['GET'])
def getSeriesByTitle():
    return SeriesCtrl.get_series_by_title(db['series'])


@app.route('/series/<idSeries>', methods=['GET'])
def getSeriesById(idSeries):
    return SeriesCtrl.get_series_by_id(db['series'], idSeries)


@app.route('/series', methods=['DELETE'])
def deleteSeriesForm():
    return SeriesCtrl.delete_series_form(db['series'])


@app.route('/series', methods=['PUT'])
def putSeriesForm():
    return SeriesCtrl.put_series_form(db['series'])


@app.route('/series/<idSeries>', methods=['DELETE'])
def deleteSeries(idSeries):
    return SeriesCtrl.delete_series(db['series'], idSeries)


@app.route('/series/<idSeries>', methods=['PUT'])
def putSeries(idSeries):
    return SeriesCtrl.put_series(db['series'], idSeries)


@app.route('/series/chapters', methods=['GET'])
def getSeriesChapters():
    return SeriesCtrl.get_series_chapters(db['series'], db['seasons'])


@app.route('/series/characters', methods=['GET'])
def getSeriesCharacters():
    return SeriesCtrl.get_series_characters(db['series'], db['characters'])


@app.route('/series/participants', methods=['GET'])
def getSeriesParticipants():
    return SeriesCtrl.get_series_participants(db['series'], db['participants'])


@app.route('/series/<idSeries>/trailer', methods=['PUT'])
def putTrailerIntoSeries(idSeries):
    return SeriesCtrl.put_trailer_into_series(db['series'], db['trailers'], idSeries)

@app.route('/series/<idSeries>/trailer', methods=['DELETE'])
def deleteTrailerFromSeries(idSeries):
    return SeriesCtrl.delete_trailer_from_series(db['series'], idSeries)


@app.route('/series/<idSeries>/categories', methods=['PUT'])
def putCategoryIntoSeries(idSeries):
    return SeriesCtrl.put_category_into_series(db['series'], db['categories'], idSeries)

@app.route('/series/<idSeries>/categories', methods=['DELETE'])
def deleteCategoryFromSeries(idSeries):
    return SeriesCtrl.delete_category_from_series(db['series'], idSeries)


@app.route('/series/<idSeries>/seasons', methods=['PUT'])
def putSeasonIntoSeries(idSeries):
    return SeriesCtrl.put_season_into_series(db['series'], db['seasons'], idSeries)


@app.route('/series/<idSeries>/seasons', methods=['DELETE'])
def deleteSeasonFromSeries(idSeries):
    return SeriesCtrl.delete_season_from_series(db['series'], idSeries)


if __name__ == '__main__':
    app.run(debug=True, port=8082)
