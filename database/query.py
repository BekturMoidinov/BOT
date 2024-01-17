CREATE_USER_TABLE = '''
CREATE TABLE IF NOT EXISTS telegram_users(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
username CHAR(20) ,
first_name CHAR(20),
last_name CHAR(20),
UNIQUE(telegram_user_id)
)
'''
SELECT_FROM_USER_TABLE = '''
SELECT telegram_user_id,first_name FROM telegram_users
'''


INSERT_USER_TABLE = '''
INSERT OR IGNORE INTO telegram_users  VALUES (?,?, ?, ?, ?)
'''

CREATE_ANSWER_TABLE = '''
CREATE TABLE IF NOT EXISTS answers(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
first_name CHAR(20),
transport_type CHAR(20) ,
model CHAR(20),
experience CHAR(20),
UNIQUE(telegram_user_id)
)
'''
INSERT_ANSWER_TABLE = '''
INSERT INTO answers  VALUES (?,?, ?, ?, ?,?)
'''
UPDATE_ANSWER_TABLE = '''
UPDATE answers SET transport_type = ?, model = ?, experience =? WHERE telegram_user_id = ?
'''
SELECT_ANSWER_TABLE = '''
SELECT first_name,transport_type,model,experience FROM answers
'''
SELECT_USER_FROM_ANSWER = '''
SELECT telegram_user_id FROM answers WHERE telegram_user_id=?
'''
SELECT_ALL_ID_ANSWER='''
SELECT telegram_user_id FROM answers
'''
CREATE_BAN_TABLE = '''
CREATE TABLE IF NOT EXISTS bans(
id INTEGER PRIMARY KEY,
tg_id INTEGER,
first_name CHAR(20),
countt INTEGER,
UNIQUE(tg_id)
)'''
INSERT_BAN_TABLE = '''
INSERT OR IGNORE INTO bans  VALUES (?,?,?,?)
'''

SELECT_BAN_TABLE_COUNT = '''
SELECT countt FROM bans WHERE tg_id=?
'''
UPDATE_BAN_TABLE_COUNT = '''
UPDATE bans SET countt=countt+1 WHERE tg_id=?
'''
DELETE_USER = '''
DELETE FROM bans WHERE tg_id=?
'''
SELECT_USER_FROM_BAN = '''
SELECT tg_id,first_name,countt FROM bans'''

CREATE_REGISTER_TABLE = '''
CREATE TABLE IF NOT EXISTS registers(
id INTEGER PRIMARY KEY,
tg_id INTEGER,
nickname CHAR(20),
biography TEXT,
age INTEGER,
zodiac CHAR(20),
gender CHAR(20),
best_color CHAR(20),
photo TEXT,
UNIQUE (tg_id)
'''
INSERT_REGISTER_TABLE = '''
INSERT OR IGNORE INTO registers VALUES (?,?,?,?,?,?,?,?,?)'''
