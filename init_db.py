from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URI = 'sqlite:///test.db'
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

def init_db():
    if not os.path.exists('test.db'):
        print("Creating database and tables...")
        with engine.connect() as connection:
            try:
                connection.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL
                );
                """))
                print("Created users table.")

                connection.execute(text("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    product TEXT NOT NULL,
                    amount INTEGER NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                );
                """))
                print("Created orders table.")

                connection.execute(text("""
                INSERT INTO users (name, age, email) VALUES
                ('Alice', 30, 'alice@example.com'),
                ('Bob', 25, 'bob@example.com'),
                ('Charlie', 35, 'charlie@example.com');
                """))
                print("Inserted sample data into users table.")

                connection.execute(text("""
                INSERT INTO orders (user_id, product, amount) VALUES
                (1, 'Laptop', 1),
                (1, 'Mouse', 2),
                (2, 'Keyboard', 1),
                (3, 'Monitor', 1);
                """))
                print("Inserted sample data into orders table.")

                # Explicitly commit transactions
                connection.commit()
                print("Transaction committed.")
            except Exception as e:
                print("An error occurred:", e)
                connection.rollback()
                print("Transaction rolled back.")
        print("Database initialized with sample data.")
    else:
        print("Database already exists.")

if __name__ == '__main__':
    init_db()
