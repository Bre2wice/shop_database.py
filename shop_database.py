from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Setup
engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Table definitions
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    status = Column(Boolean, default=False)  # Bonus: shipped or not

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity}, status={self.status})"


# Create tables
Base.metadata.create_all(engine)


# Insert data
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

product1 = Product(name="Laptop", price=1200)
product2 = Product(name="Phone", price=800)
product3 = Product(name="Headphones", price=150)

order1 = Order(user=user1, product=product1, quantity=1, status=False)
order2 = Order(user=user1, product=product2, quantity=2, status=True)
order3 = Order(user=user2, product=product3, quantity=3, status=False)
order4 = Order(user=user2, product=product1, quantity=1, status=True)

session.add_all([user1, user2, product1, product2, product3, order1, order2, order3, order4])
session.commit()


# Queries
print("\n--- All Users ---")
for user in session.query(User).all():
    print(user)

print("\n--- All Products ---")
for product in session.query(Product).all():
    print(product)

print("\n--- All Orders ---")
for order in session.query(Order).all():
    print(f"User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}, Shipped: {order.status}")

# Update product price
product_to_update = session.query(Product).filter_by(name="Phone").first()
if product_to_update:
    product_to_update.price = 850
    session.commit()
    print(f"\nUpdated {product_to_update.name}'s price to {product_to_update.price}")

# Delete user by ID
user_to_delete = session.query(User).filter_by(id=2).first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()
    print(f"\nDeleted user: {user_to_delete.name}")

# Bonus queries
print("\n--- Orders Not Shipped ---")
for order in session.query(Order).filter_by(status=False).all():
    print(f"Order ID: {order.id}, User: {order.user.name}, Product: {order.product.name}")

print("\n--- Total Orders per User ---")
for user in session.query(User).all():
    count = session.query(Order).filter_by(user_id=user.id).count()
    print(f"{user.name} has {count} order(s).")
