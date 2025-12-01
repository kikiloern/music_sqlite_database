# %%
import sqlite3
import pandas as pd

# %%
conn = sqlite3.connect('songs.db')
cursor = conn.cursor()

# Tabelle anlegen, falls sie noch nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    date_listened TEXT,
    language TEXT,
    notes TEXT
)
""")
conn.commit()

# Add song
title = "Ali Pamtim Jos"
author = "Hanka Paldum"
date_listened = "2025-12-01"
language = "Yugoslavian"
notes = "Yugoslavian classic"

cursor.execute(
    'INSERT INTO songs (title, author, date_listened, language, notes) VALUES (?, ?, ?, ?, ?)',
    (title, author, date_listened, language, notes)
)
conn.commit()

print("Song added successfully!\n")

# List all songs
cursor.execute('SELECT id, title, author, date_listened, language, notes FROM songs')
songs = cursor.fetchall()
print("Music in the database:")
for music in songs:
    print(music)

df = pd.read_sql_query("SELECT * FROM songs", conn)
df.to_excel("music.xlsx", index=False)

conn.close()
print("Exported all songs to music.xlsx")

# %%


# %%

#%%

#%%
conn = sqlite3.connect('music.db')
cursor = conn.cursor()


# Delete a book by its id, for example id = 1
music_id_to_delete = 5
cursor.execute('DELETE FROM music WHERE id = ?', (music_id_to_delete,))
conn.commit()

print(f"Book with id {music_id_to_delete} deleted.")
conn.close()
# %%