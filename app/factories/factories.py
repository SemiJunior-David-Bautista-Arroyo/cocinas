from app.models.materialModel import MaterialModel
from app.schemas.material import MaterialSchema
from app.models.designModel import DesignModel
from app.schemas.design import DesignSchema 
from app.models.kitchenModel import KitchenModel
from app.schemas.kitchen import KitchenSchema
from app.models.installerModel import InstallerModel
from app.schemas.installer import InstallerSchema 


# fabrica generica para la creación de modelos
class Factory:
    @staticmethod
    def create(data, model):
        # Método genérico para crear instancias de modelos desde schemas.
        return model(**data.__dict__)


    @staticmethod
    def create_instance(schema, model_mapping):
        # Crea una instancia automaticamente en base al schema y mapeo de modelos
        model = model_mapping.get(type(schema))

        if not model:
            raise ValueError(f'Not Model associated with the shema:{type(schema)}')
        
        return Factory.create(schema, model)
        
# mapeo de schema a modelos
MODEL_MAPPING = {
    MaterialSchema : MaterialModel,
    DesignSchema : DesignModel,
    KitchenSchema : KitchenModel,
    InstallerSchema : InstallerModel,
}

