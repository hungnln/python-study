from app import db


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(120), unique=True, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # def __str__(self):
    #     return str(self.__class__) + '\n' + '\n'.join(
    #         ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def to_dict(self):
        data = self.__dict__.copy()  # Copy the instance's dictionary
        data.pop('_sa_instance_state', None)  # Remove the _sa_instance_state attribute
        return data