from app.models.userModel import UserModel
from app.models.rolModel import RolModel
from app.schemas.userSchema import UserSchema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")

class UserService:

    def __init__(self, db) -> None:
        self.db = db

    
    def exclude_values(self, user : UserSchema) ->UserSchema:
        userdict = user.__dict__.copy()

        userdict.pop('password_user', None)

        return userdict


    def addUser(self, data : UserSchema) -> UserSchema:

        user = data.__dict__

        user['password_user'] = pwd_context.hash(data.password_user)

        nu = UserModel(**user)

        self.db.add(nu)
        self.db.commit()
        self.db.refresh(nu)
        self.db.close()

        return self.exclude_values(nu)
    

    def verifyuser(self, username : str, pasword : str) -> UserSchema:

        result = (
        self.db.query(
            UserModel.id,
            UserModel.name,
            UserModel.lastname,
            UserModel.username,
            UserModel.cellphone,
            UserModel.address,
            UserModel.password_user,
            RolModel.rol.label("role")  # Alias para el rol
        )
        .join(RolModel, UserModel.rol_id == RolModel.id)  # JOIN explícito
        .filter(UserModel.username == username)  # Filtrar por username
        .first()
    )
        password_verifier = pwd_context.verify(pasword, result.password_user)
        
        if result.name and password_verifier:
            usuario = {
                "id" : result.id,
                "name" : result.name,
                "lastname" : result.lastname,
                "username" : result.username,
                "cellphone" : result.cellphone,
                "address" : result.address,
                "rol" : result.role,
            }
            return usuario
        
        return None
    
    
    def getall(self) :

        users = self.db.query(UserModel).all()

        return users
    
    
