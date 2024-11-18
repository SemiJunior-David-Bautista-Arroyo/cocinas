from app.models.installerModel import InstallerModel
from app.schemas.installer import InstallerSchema
from app.factories.factories import Factory, MODEL_MAPPING


class InstallerService:

    def __init__(self, db) -> None:
        self.db = db

    
    def createinstaller(self, data : InstallerSchema):

        ni = Factory.create_instance(data, MODEL_MAPPING)

        self.db.add(ni)
        self.db.commit()
        self.db.refresh(ni)

        return ni


    def getInstallers(self):
        
        instalers = self.db.query(InstallerModel).all()

        return instalers
    
    
    def getbyID(self, id : int):

        instaler = self.db.query(InstallerModel).filter(InstallerModel.id == id).first() 


        return instaler
