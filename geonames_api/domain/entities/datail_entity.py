from pydantic import BaseModel


class Detail(BaseModel):
    id: int
    city: str
    zip_code = int

    def __repr__(self):
        return f"id:{self.id},city:{self.city}, zip code: {self.zip_code}"
