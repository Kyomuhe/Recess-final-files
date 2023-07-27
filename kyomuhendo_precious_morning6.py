#Assignment 7
#1a show a context manager for file handling that automatically opens and closes a file
class FileHandler:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mode)
        except FileNotFoundError:
            raise Exception("File not found!")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# Usage:
try:
    with FileHandler("example.txt", "r") as file:
        # Perform operations on the file
        contents = file.read()
        print(contents)
except Exception as e:
    print(e)


#b, Show a context manager for managing a database connection
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# Usage:
try:
    with DatabaseConnection("example.db") as conn:
        # Perform database operations
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_name")
        results = cursor.fetchall()
        for row in results:
            print(row)
except sqlite3.OperationalError as e:
    print("Table not found:", e)


#c, show multithreading and multiprocessing that allows us to run the function for different amounts of time
import multiprocessing
import time

def run_function(seconds):
    print(f"Function started. Running for {seconds} seconds...")
    time.sleep(seconds)
    print("Function completed.")

if __name__ == '__main__':
    # Multiprocessing example
    processes = []
    for duration in [4, 5, 6]:
        process = multiprocessing.Process(target=run_function, args=(duration,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
