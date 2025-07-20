import psycopg2

class Database:
    def __init__(self):
        self.database = psycopg2.connect(
            dbname="translate",
            password="1111",
            host="localhost",
            user="postgres",
            port="5432"
        )

    def execute(self, sql, *args, commit=False, fetchall=False, fetchone=False):
        with self.database as db:
            with self.database.cursor() as cursor:
                cursor.execute(sql, args)

                if commit:
                    result = db.commit()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
        return result

    def create_tables(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS categories (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
            );
        """, commit=True)

        self.execute("""
            CREATE TABLE IF NOT EXISTS films (
                id SERIAL PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                description TEXT,
                category_id INTEGER REFERENCES categories(id)
            );
        """, commit=True)

    def insert_category(self, name):
        self.execute("INSERT INTO categories (name) VALUES (%s);", name, commit=True)

    def insert_film(self, title, description, category_id):
        self.execute(
            "INSERT INTO films (title, description, category_id) VALUES (%s, %s, %s);",
            title, description, category_id,
            commit=True
        )

    def get_categories(self):
        return self.execute("SELECT id, name FROM categories;", fetchall=True)

    def get_films_by_category(self, category_id):
        return self.execute(
            "SELECT title, description FROM films WHERE category_id = %s;",
            category_id,
            fetchall=True
        )