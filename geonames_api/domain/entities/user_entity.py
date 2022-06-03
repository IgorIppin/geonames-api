from pydantic import BaseModel


class User(BaseModel):
    name: str

    def __repr__(self):
        return f"name:{self.name}"

    class Config:
        schema_extra: dict = {
            'examples': [
                {
                    'name': "Ingvar"
                }
            ]
        }
