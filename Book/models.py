from Book import db

class BookName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)


class Buy(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Integer, nullable=True)

class webhook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intentid = db.Column(db.String(200), nullable=False)
    querytext = db.Column(db.String(400), nullable=True)
    senddata = db.Column(db.String(2000), nullable=True)
    create_date = db.Column(db.DateTime(),nullable=False)


class moviehook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intentid = db.Column(db.String(200), nullable=False)
    querytext = db.Column(db.String(400), nullable=True)
    senddata = db.Column(db.String(2000), nullable=True)
    create_date = db.Column(db.DateTime(),nullable=False)

class Vote(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    count = db.Column(db.Integer, nullable=False)
