import sqlite3


class DbHandler:
    def __init__(self, path):
        self.path = path
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS Ciphers(given_text TEXT NOT NULL, output TEXT NOT NULL);"
        self.con.execute(query)

    def add_to_ciphers(self, given_text, output):
        query = "INSERT INTO Ciphers(given_text, output) VALUES(?, ?)"
        self.con.execute(query, (given_text, output))
        self.con.commit()

    def export_all_ciphers(self, table_name, output_file=None):
        try:
            query = f"SELECT * FROM {table_name}"
            results = self.con.execute(query).fetchall()
            if output_file:
                with open(output_file, "w") as file:
                    for row in results:
                        file.write(str(row) + "\n")
                print(f"Results saved to {output_file}")
            else:
                for row in results:
                    print(row)
        except Exception as e:
            print("Error occurred while fetching data:", e)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()
