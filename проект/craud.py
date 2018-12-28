#!/usr/bin/python3
# -*- coding: utf8 -*-
import sys, sqlite3
from config import *

con = sqlite3.connect(STATIC_DIR+DB_NAME)
c = con.cursor()
try:
  c.execute("CREATE TABLE IF NOT EXISTS user (id integer, user text, data text)")
  con.commit()
  con.close()
except:
  pass

class sql():
  def __init__(self, user="None", data="None", idstr="None"):
    self.user=user
    self.data=data
    self.idstr=idstr

  def ins(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    c.execute("SELECT id FROM user ORDER BY id DESC LIMIT 1")
    if c.fetchone() == None:
      ins = [('0', "Имя", "Дата"),]
      c.executemany("INSERT INTO user VALUES (?,?,?)", ins)
    c.execute("SELECT id FROM user ORDER BY id DESC LIMIT 1")
    idi = c.fetchone()
    idi = idi[0] + 1
    ins = [(idi, self.user, self.data),]
    c.executemany("INSERT INTO user VALUES (?,?,?)", ins)
    con.commit()
  def sel(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    if self.user == "all":
      c.execute("SELECT * FROM user")
      al = c.fetchall()
      return al
    else:
      c.execute("SELECT * FROM user WHERE user='%s'" % self.user)
      al = c.fetchall()
      return al
  def selid(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    c.execute("SELECT * FROM user WHERE id='%s'" % self.user)
    al = c.fetchall()
    return al
  def seldata(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    c.execute("SELECT * FROM user WHERE data='%s'" % self.user)
    al = c.fetchall()
    return al
  def delete(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    if self.user == 'id':
      c.execute("DELETE FROM user WHERE id='%s'" % self.data)
    elif self.user == 'user':
      c.execute("DELETE FROM user WHERE user='%s'" % self.data)
    elif self.user == 'data':
      c.execute("DELETE FROM user WHERE data='%s'" % self.data)
    con.commit()
  def update(self):
    con = sqlite3.connect(STATIC_DIR+DB_NAME)
    c = con.cursor()
    print(self.user, self.data, self.idstr)
    if self.data == 'user':
      c.execute("UPDATE user SET user=?  WHERE id=?", (self.idstr, self.user))
    if self.data == 'data':
      c.execute("UPDATE user SET data=?  WHERE id=?", (self.idstr, self.user))
    con.commit()
    con.close()
helper = """Краткая инструкция по использованию программы
-h                  Вызов данной справки
-i <имя> <дата>     Внесение данных в таблицу, дата в формате: dd-mm-yyyy Пример: ./craud.py -i Vanessa 21-01-2005
-s <имя>            Поиск данных по столбцу "Имя". Пример: ./craud.py -s Vasya  - Покажет все значение столбцов с именем "Vanessa"
-s all              Поиск по ключу -s, со значением "all", покажет все данные в таблице.
-id <id>            Поиск данных по столбцу "id". Пример: ./craud.py -id 2  - Покажет все значение столбцов с ID = "2"
-dt <дата>          Поиск данных по столбцу "дата". Пример: ./craud.py -dt 21-01-2010  - Покажет все значение столбцов с датой = "21-01-2010"
-d <столбец> <значение> Для удаления строки из бызы выберете столбец со значением = (id, user(Имя), data(Дата)) и само значение. 
                    Пример: ./craud.py -d user Melissa
-e <id> <столбец> <значение> Для редактирования строки, укажите её "id", столбец(user, или data) который вы хотите отредактировать и его новое значение
                    Пример: ./craud.py -e 2 user Rowan
"""
if len(sys.argv) == 1:
  print(helper)
if len(sys.argv) == 2:
  if sys.argv[1] == "-h":
    print("""Краткая инструкция по использованию программы
-h              Вызов данной справки
-i имя дата     Внесение данных в таблицу, дата в формате: dd-mm-yyyy Пример: ./craud.py -i Vanessa 21-01-2005
""")
if len(sys.argv) == 3:
  if sys.argv[1] == "-s":
    s = sql(sys.argv[2]).sel() 
    print("Список значений с именем:", sys.argv[2])
    for i in s:
      print(i[0],i[1],i[2])
#      print(i[0],i[1])
  elif sys.argv[1] == "-id":
    s = sql(sys.argv[2]).selid() 
    print("Список пользователей с ID:", sys.argv[2])
    for i in s:
      print(i[0],i[1],i[2])
  elif sys.argv[1] == "-dt":
    s = sql(sys.argv[2]).seldata() 
    print("Все значения таблицы с датой:", sys.argv[2])
    for i in s:
      print(i[0],i[1],i[2])
  else:
    print("Вы ввели не верные данные, попробуте ещё раз.")

if len(sys.argv) >= 4:
  if sys.argv[1] == "-i":
    s = sql(sys.argv[2], sys.argv[3]).ins()
  elif sys.argv[1] == "-d":
    s = sql(sys.argv[2], sys.argv[3]).delete()
    print("Удалены все значения таблицы:", sys.argv[2], sys.argv[3])
  elif sys.argv[1] == "-e":
    s = sql(sys.argv[2], sys.argv[3], sys.argv[4]).update()
    print("Значение изменено:", sys.argv[2], sys.argv[3], sys.argv[4])
  else:
    print("Вы ввели не верные данные, попробуте ещё раз.")






