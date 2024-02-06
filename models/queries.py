from models.connection import db


def select_name():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM your_table")
        result = cursor.fetchall()
        cursor.close()
        """
            Info_select is used to separate names into lists of 25 items,
            because discord only accepts 25 items per select menu
        """
        infos_select = [result[i:i + 25] for i in range(0, len(result), 25)]
        return {"status": True, "data": infos_select}

    except Exception as e:
        print(e)
        return {"status": False, "data": "so bad"}