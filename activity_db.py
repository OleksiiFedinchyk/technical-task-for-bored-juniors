import sqlite3

class Activity_table:
    conn = sqlite3.connect('activity.db')
    c = conn.cursor()

    def __init__(self):
        try:
            Activity_table.c.execute("CREATE TABLE activities (ID INTEGER PRIMARY KEY, Activity text)")
        except:
            pass

    @classmethod
    def insert_activity(cls, act):
        with Activity_table.conn:
            Activity_table.c.execute("INSERT INTO activities (Activity) VALUES (:activity)", {'activity': act})

    @classmethod
    def latest_activities(cls, n):
        Activity_table.c.execute("SELECT * FROM activities ORDER BY ID DESC")
        return Activity_table.c.fetchmany(n)




