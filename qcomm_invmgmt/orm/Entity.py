from sqlalchemy import (
    String,
    UUID,
    Boolean,
    ForeignKey,
    Column,
    DateTime,
    create_engine,
)
from sqlalchemy.orm import (
    relationship,
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
)
import uuid

# Base class
class Base(DeclarativeBase):
    pass


# Utility function to generate UUID
def generate_uuid():
    return str(uuid.uuid4())


# Category Table
class Category(Base):
    __tablename__ = "category"
    __table_args__ = {"schema": "inventory"}
    
    cat_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=generate_uuid)
    cat_name: Mapped[str] = mapped_column(String(40), nullable=False)
    cat_desc: Mapped[str] = mapped_column(String(100), nullable=True)

    # Relationship with SKU
    skus: Mapped["SKU"] = relationship("SKU", back_populates="category")


# Brand Table
class SKUBrand(Base):
    __tablename__ = "sku_brand"
    __table_args__ = {"schema": "inventory"}
    
    brand_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=generate_uuid)
    brand_name: Mapped[str] = mapped_column(String(40), nullable=False)
    brand_desc: Mapped[str] = mapped_column(String(100), nullable=True)

    # Relationship with SKU
    skus: Mapped["SKU"] = relationship("SKU", back_populates="brand")


# Seller Table
class Seller(Base):
    __tablename__ = "seller"
    __table_args__ = {"schema": "inventory"}
    
    seller_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=generate_uuid)
    fname: Mapped[str] = mapped_column(String(60), nullable=False)
    lname: Mapped[str] = mapped_column(String(60), nullable=False)
    mobile: Mapped[str] = mapped_column(String(15), nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)

    # Relationship with SKU
    skus: Mapped["SKU"] = relationship("SKU", back_populates="seller")


# SKU Table
class SKU(Base):
    __tablename__ = "sku"
    __table_args__ = {"schema": "inventory"}
    
    sku_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=generate_uuid)
    sku_name: Mapped[str] = mapped_column(String(100), nullable=False)
    sku_desc: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Foreign keys
    sku_category: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("inventory.category.cat_id"), nullable=False
    )
    sku_brand: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("inventory.sku_brand.brand_id"), nullable=False
    )
    seller_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("inventory.seller.seller_id"), nullable=False
    )

    # Relationships
    category: Mapped["Category"] = relationship("Category", back_populates="skus")
    brand: Mapped["SKUBrand"] = relationship("SKUBrand", back_populates="skus")
    seller: Mapped["Seller"] = relationship("Seller", back_populates="skus")



