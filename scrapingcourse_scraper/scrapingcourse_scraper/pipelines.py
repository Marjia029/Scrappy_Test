import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    name = Column(String)
    price = Column(String)
    image_path = Column(String)


class ProductPipeline:
    def __init__(self):
        # Connect to PostgreSQL
        self.engine = create_engine("postgresql://Marjia:Marjia029@db/ecommerce")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.Session()
        # Get the image path if images were downloaded
        image_path = item["images"][0]["path"] if "images" in item and item["images"] else None
        product = Product(
            url=item["url"],
            name=item["name"],
            price=item["price"],
            image_path=image_path,
        )
        try:
            session.add(product)
            session.commit()
        except Exception as e:
            session.rollback()
            spider.logger.error(f"Error saving product: {e}")
        finally:
            session.close()
        return item
