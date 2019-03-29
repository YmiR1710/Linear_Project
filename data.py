from twitter_analysis import get_tweets
import datetime
import mysql.connector


def get_info(user_names):
    now = datetime.datetime.today()
    users = []
    for u in user_names:
        users.append([u, 0, 0])
    for user in users:
        try:
            for tweet in get_tweets(user[0], tweets=450):
                if tweet.get('time').split()[0] == str(now - datetime.timedelta(1)).split()[0]:
                    user[2] += 1
                    user[1] += tweet.get('likes')
        except:
            users.remove(user)
    for user in users:
        if user[2] != 0:
            user[1] = user[1]/user[2]
        else:
            user[1] = 0
    return users


def database_insert(table_name, users):
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="wital1999",
        database="twitter"
    )
    my_cursor = my_db.cursor()
    command = "CREATE TABLE IF NOT EXISTS {} ( `id` int NOT NULL AUTO_INCREMENT".format(table_name)
    insert_1 = "("
    insert_2 = ""
    count = 1
    for user in users:
        command += ", `name_{}` VARCHAR(255), `likes_{}` FLOAT".format(count, count)
        insert_1 += "name_{}, likes_{}, ".format(count, count)
        insert_2 += "'" + user[0] + "', " + str(user[1]) + ", "
        count += 1
    insert_1 = insert_1[:-2]
    insert_1 += ")"
    insert_2 = insert_2[:-2]
    insert_2 += ");"
    insert = "INSERT INTO {} ".format(table_name) + insert_1 + " VALUES(" + insert_2
    command += ", PRIMARY KEY (id));"
    try:
        my_cursor.execute(command)
        my_cursor = my_db.cursor()
        my_cursor.execute(insert)
    except:
        pass
    my_db.commit()
    
