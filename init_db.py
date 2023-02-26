import sqlite3

conn = sqlite3.connect('database.db')
create_table = '''
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    content TEXT NOT NULL
);'''
conn.executescript(create_table)
conn.execute("INSERT INTO posts (title, author, content) VALUES (?, ?, ?)",
            ('第一篇博客', '春木', '你好，我是春木\n春风绿地树先知，欢迎来到我的博客\n'))
conn.commit()
conn.close()
