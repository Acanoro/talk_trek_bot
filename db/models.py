import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    id_tg = sq.Column(sq.Integer, unique=True)

    def __str__(self):
        return f'Users: {self.id_tg}'


class Words(Base):
    __tablename__ = 'words'

    id = sq.Column(sq.Integer, primary_key=True)
    word = sq.Column(sq.String(length=50), unique=True)
    translate = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return f'Words: {self.word}'


class LearnedWordsUser(Base):
    __tablename__ = 'learned_words_user'

    id = sq.Column(sq.Integer, primary_key=True)

    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"))
    learned_user = relationship("Users", backref="learned_words")

    word = sq.Column(sq.String(length=50), unique=True)
    translate = sq.Column(sq.String(length=50), unique=True)


class WordsInLearningUser(Base):
    __tablename__ = 'words_in_learning_user'

    id = sq.Column(sq.Integer, primary_key=True)

    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"))
    learning_user = relationship("Users", backref="words_in_learning")

    word = sq.Column(sq.String(length=50), unique=True)
    translate = sq.Column(sq.String(length=50), unique=True)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
