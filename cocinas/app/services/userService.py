from app.models.userModel import UserModel
from app.schemas.user import UserSchema, AddressSchema

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class userService:

    def __init__(self, db) -> None:
        self.db = db


    def excludeValues(self, user : UserSchema) -> UserSchema:
        
        user_dict = user.__dict__.copy()

        user_dict.pop('password_user',None)

        return user_dict


    def verifyClient(self, email : str, password : str) -> UserSchema :
        client = self.db.query(UserModel).filter(UserModel.email == email).first()

        password_verifier = pwd_context.verify(password, client.password_user)

        if client and password_verifier:    
            cliente = self.excludeValues(client)
            return cliente
        
        return None
    

    def getclientbyId(self, id : int) -> UserSchema :
        
        client = self.db.query(UserModel).filter(UserModel.id == id).first()
        if client is None:
            raise Exception('Any user was found')
        
        return client


    def registerClient(self, data : UserSchema) -> UserSchema:

        hashed_password = pwd_context.hash(data.password_user)

        user = data.__dict__
        user['password_user'] = hashed_password

        new_client = UserModel(**user)

        self.db.add(new_client)
        self.db.commit()
        self.db.refresh(new_client)
        self.db.close()

        return self.excludeValues(new_client)

    
    def deleteClient(self, id : int) :

        client = self.db.query(UserModel).filter(UserModel.id == id).first()
       
        if client is None:
            return False
        
        self.db.delete(client)
        self.db.commit()

        return


    def updateClient(self, id : int, data : AddressSchema) -> UserSchema :
        
        client = self.getclientbyId(id)

        if client is None:
            return False

        client.address = data.__dict__


        self.db.commit()
        self.db.refresh(client)

        cliente = self.excludeValues(client)
        self.db.close()

        return cliente

