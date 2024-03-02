from sqlalchemy.orm import mapped_column
from datetime import datetime

from app.extensions import db

class Ficha(db.Model):
    __tablename__ = 'tb_ctr_fichas'
    
    id = mapped_column(db.Integer, primary_key=True)
    var_raca_fic = mapped_column(db.String(45))
    var_etnia_fic = mapped_column(db.String(45))
    var_ser_fic = mapped_column(db.String(45))
    var_classesocial_fic = mapped_column(db.String(45))
    dat_created_fic = mapped_column(db.DateTime, default=datetime.now())
    
    def __init__(self, raca, etnia, ser, social):
        self.var_raca_fic = raca
        self.var_etnia_fic = etnia
        self.var_ser_fic = ser
        self.var_classesocial_fic = social
        self.dat_created_fic = datetime.now()
        
    def to_dict(self):
        return {
            "raca" : self.var_raca_fic,
            'etnia' : self.var_etnia_fic,
            'ser' : self.var_ser_fic,
            'classe_social' : self.var_classesocial_fic,
            "criacao" : self.dat_created_fic
        }
        
    def add(self):
        db.session.add(self)
        db.session.commit()