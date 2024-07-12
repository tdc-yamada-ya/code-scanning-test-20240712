import sqlite3

def f(name: str):
  con = sqlite3.connect("tutorial.db")
  cur = con.cursor()
  cur.execute("INSERT INTO foo(name) VALUES (" + name + ")")

if __name__ == "__main__":
  print("main")
