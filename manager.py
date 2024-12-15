import sys
import random
import io
import string
import webbrowser
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QDialog,
    QFileDialog,
    QTableWidgetItem,
)
from PyQt6.QtGui import QCursor, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6 import uic
import sqlite3 as sl
import re
from fernet_file import encrypt, decrypt


format_register = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>572</width>
    <height>597</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>572</width>
    <height>597</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>572</width>
    <height>597</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">
background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>40</y>
      <width>381</width>
      <height>481</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius: 15px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>70</y>
      <width>191</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 18pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Регистрация</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login_reg">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>150</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
color: rgb(0, 0, 0);
font: 12pt &quot;Nirmala UI&quot;;
border: 1px solid black;
border-radius: 10px;
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>10</number>
    </property>
   </widget>
   <widget class="QLineEdit" name="pass_reg">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>200</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid black;
border-radius: 10px;
color: rgb(0, 0, 0);
font: 12pt &quot;Nirmala UI&quot;;

</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>20</number>
    </property>
   </widget>
   <widget class="QPushButton" name="registrationButton">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>300</y>
      <width>241</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 15px;
font: 87 12pt &quot;Segoe UI Black&quot;;
color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Зарегестрироваться</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="repeatpass_reg">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>250</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid black;
border-radius: 10px;
color: rgb(0, 0, 0);
font: 12pt &quot;Nirmala UI&quot;;
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>20</number>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>370</y>
      <width>281</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="haveacc_button">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>390</y>
      <width>381</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-color: rgb(255, 255, 255);
border: 0px;
font: 75 10pt &quot;Rubik&quot;;
color: rgb(34, 158, 217);</string>
    </property>
    <property name="text">
     <string>Уже есть аккаунт</string>
    </property>
   </widget>
   <widget class="QLabel" name="errorlabel">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>120</y>
      <width>251</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 7pt &quot;Segoe UI&quot;;
color: rgb(193, 31, 55);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
format_enter = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>572</width>
    <height>597</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>572</width>
    <height>597</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>572</width>
    <height>597</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="back_labl">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>40</y>
      <width>381</width>
      <height>481</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius: 15px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="pass_ent">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>200</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid black;
border-radius: 10px;
color: rgb(0, 0, 0);
font: 12pt &quot;Nirmala UI&quot;;

</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="enterButton">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>280</y>
      <width>251</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-radius: 15px;
font: 87 12pt &quot;Segoe UI Black&quot;;
color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login_ent">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>150</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
color: rgb(0, 0, 0);
font: 12pt &quot;Nirmala UI&quot;;
border: 1px solid black;
border-radius: 10px;
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>15</number>
    </property>
   </widget>
   <widget class="QPushButton" name="noacc_lab">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>380</y>
      <width>381</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-color: rgb(255, 255, 255);
border: 0px;
font: 75 10pt &quot;Rubik&quot;;
color: rgb(34, 158, 217);</string>
    </property>
    <property name="text">
     <string>У меня нет аккаунта</string>
    </property>
   </widget>
   <widget class="QLabel" name="enter_lab">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>70</y>
      <width>51</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 18pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Вход</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>370</y>
      <width>301</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="errorlabel_ent">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>120</y>
      <width>201</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 7pt &quot;Segoe UI&quot;;
color: rgb(193, 31, 55);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
format_main = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1165</width>
    <height>646</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1165</width>
    <height>646</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1165</width>
    <height>646</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>-10</y>
      <width>201</width>
      <height>681</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="generator_button">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>201</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 10pt &quot;Rubik&quot;;
border: 0px;
color: rgb(34, 170, 255);</string>
    </property>
    <property name="text">
     <string>Генерирование паролей</string>
    </property>
   </widget>
   <widget class="QPushButton" name="anthrman_button">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>590</y>
      <width>201</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 10pt &quot;Rubik&quot;;
border: 0px;
color: rgb(34, 170, 255);</string>
    </property>
    <property name="text">
     <string>Сменить пользователя</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="passwordTable">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>50</y>
      <width>611</width>
      <height>671</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>611</width>
      <height>671</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>611</width>
      <height>671</height>
     </size>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(255, 255, 255, 180);</string>
    </property>
    <property name="editTriggers">
     <set>QAbstractItemView::NoEditTriggers</set>
    </property>
    <property name="sortingEnabled">
     <bool>false</bool>
    </property>
    <attribute name="horizontalHeaderCascadingSectionResizes">
     <bool>true</bool>
    </attribute>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>206</number>
    </attribute>
    <attribute name="horizontalHeaderShowSortIndicator" stdset="0">
     <bool>false</bool>
    </attribute>
    <attribute name="horizontalHeaderStretchLastSection">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderCascadingSectionResizes">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderShowSortIndicator" stdset="0">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderStretchLastSection">
     <bool>false</bool>
    </attribute>
    <column>
     <property name="text">
      <string>Название сервиса</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Логин</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>URL</string>
     </property>
    </column>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>810</x>
      <y>0</y>
      <width>361</width>
      <height>681</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>890</x>
      <y>10</y>
      <width>211</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font: 13pt &quot;Sitka Text&quot;;</string>
    </property>
    <property name="text">
     <string>Подробная информация</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>60</y>
      <width>41</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>100</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>140</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Надежность</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>180</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Ссылка</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>220</y>
      <width>81</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>840</x>
      <y>90</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>840</x>
      <y>130</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>840</x>
      <y>170</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>840</x>
      <y>210</y>
      <width>291</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
border-top: 1px solid gray;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="login_settext">
    <property name="geometry">
     <rect>
      <x>940</x>
      <y>60</y>
      <width>191</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="password_settext">
    <property name="geometry">
     <rect>
      <x>940</x>
      <y>100</y>
      <width>191</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="url_label">
    <property name="geometry">
     <rect>
      <x>940</x>
      <y>180</y>
      <width>191</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="name_label">
    <property name="geometry">
     <rect>
      <x>940</x>
      <y>220</y>
      <width>191</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
font:10pt &quot;Segoe UI&quot;;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QProgressBar" name="qualitebar">
    <property name="geometry">
     <rect>
      <x>950</x>
      <y>140</y>
      <width>151</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border: 1px solid gray;
background-color: rgb(226, 226, 226);</string>
    </property>
    <property name="value">
     <number>0</number>
    </property>
    <property name="textVisible">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="check_button">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>70</y>
      <width>201</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 9pt &quot;Rubik&quot;;
border: 0px;
color: rgb(34, 170, 255);</string>
    </property>
    <property name="text">
     <string>Проверка надежности пароля</string>
    </property>
   </widget>
   <widget class="QPushButton" name="change_button">
    <property name="geometry">
     <rect>
      <x>880</x>
      <y>280</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(180, 180, 180);
font: 10pt &quot;Sitka Text&quot;;
border: 0px;
border-radius: 5px;
</string>
    </property>
    <property name="text">
     <string>Изменить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="delete_button">
    <property name="geometry">
     <rect>
      <x>990</x>
      <y>280</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(180, 180, 180);
font: 10pt &quot;Sitka Text&quot;;
border: 0px;
border-radius: 5px;
</string>
    </property>
    <property name="text">
     <string>Удалить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_13">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>0</y>
      <width>611</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="search_line">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>10</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border: 1px solid gray;
border-radius: 10px;
background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add_button">
    <property name="geometry">
     <rect>
      <x>590</x>
      <y>10</y>
      <width>211</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(180, 180, 180);
font: 10pt &quot;Sitka Text&quot;;
border: 0px;
border-radius: 10px;
</string>
    </property>
    <property name="text">
     <string>Добавить данные</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_14">
    <property name="geometry">
     <rect>
      <x>850</x>
      <y>250</y>
      <width>271</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(226, 226, 226);
color: rgb(255, 0, 0);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <zorder>passwordTable</zorder>
   <zorder>label_2</zorder>
   <zorder>label_9</zorder>
   <zorder>label</zorder>
   <zorder>generator_button</zorder>
   <zorder>anthrman_button</zorder>
   <zorder>label_3</zorder>
   <zorder>label_4</zorder>
   <zorder>label_5</zorder>
   <zorder>label_10</zorder>
   <zorder>label_11</zorder>
   <zorder>label_12</zorder>
   <zorder>label_6</zorder>
   <zorder>label_7</zorder>
   <zorder>label_8</zorder>
   <zorder>login_settext</zorder>
   <zorder>password_settext</zorder>
   <zorder>url_label</zorder>
   <zorder>name_label</zorder>
   <zorder>qualitebar</zorder>
   <zorder>check_button</zorder>
   <zorder>change_button</zorder>
   <zorder>delete_button</zorder>
   <zorder>label_13</zorder>
   <zorder>search_line</zorder>
   <zorder>add_button</zorder>
   <zorder>label_14</zorder>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
format_change = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>334</width>
    <height>195</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>334</width>
    <height>195</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>334</width>
    <height>195</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(226, 226, 226);</string>
  </property>
  <widget class="QLineEdit" name="login_edit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="password_edit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="url_edit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>90</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="name_edit">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>120</y>
     <width>311</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ready_button">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>160</y>
     <width>121</width>
     <height>23</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(180, 180, 180);
font: 10pt &quot;Sitka Text&quot;;
border: 0px;
border-radius: 5px;
</string>
   </property>
   <property name="text">
    <string>Готово</string>
   </property>
  </widget>
  <widget class="QPushButton" name="back_button">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>160</y>
     <width>121</width>
     <height>23</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(180, 180, 180);
font: 10pt &quot;Sitka Text&quot;;
border: 0px;
border-radius: 5px;
</string>
   </property>
   <property name="text">
    <string>Назад</string>
   </property>
  </widget>
  <widget class="QLabel" name="error_label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>291</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 8pt &quot;Noto Sans&quot;;
color: rgb(255, 0, 0);</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
format_add = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>249</width>
    <height>300</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>249</width>
    <height>300</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>249</width>
    <height>300</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QPushButton" name="adddan">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>180</y>
     <width>111</width>
     <height>23</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
font: 75 9pt &quot;Rubik&quot;;
border: 0px;
color: rgb(34, 170, 255);
border-radius: 10px;</string>
   </property>
   <property name="text">
    <string>Добавить данные</string>
   </property>
  </widget>
  <widget class="QPushButton" name="back_button">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>180</y>
     <width>111</width>
     <height>23</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
font: 75 9pt &quot;Rubik&quot;;
border: 0px;
color: rgb(34, 170, 255);
border-radius: 10px;</string>
   </property>
   <property name="text">
    <string>Назад</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="login">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>231</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="password">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>90</y>
     <width>231</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="url">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>120</y>
     <width>231</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>150</y>
     <width>111</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(0, 255, 42);
font: 8pt &quot;Noto Sans&quot;;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="error_label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>151</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(255, 0, 0);</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLineEdit" name="name">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>231</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
format_generator = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>481</width>
    <height>185</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>481</width>
    <height>185</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>481</width>
    <height>185</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QPushButton" name="go_button">
   <property name="geometry">
    <rect>
     <x>100</x>
     <y>20</y>
     <width>101</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
   <property name="text">
    <string>Создать Пароли</string>
   </property>
  </widget>
  <widget class="QPlainTextEdit" name="paroli">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>30</y>
     <width>261</width>
     <height>151</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="save_button">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>70</y>
     <width>81</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>81</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(255, 255, 255);
font: 75 8pt &quot;Rubik&quot;;</string>
   </property>
   <property name="text">
    <string>Длина пароля</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>111</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(255, 255, 255);
font: 75 8pt &quot;Rubik&quot;;</string>
   </property>
   <property name="text">
    <string>Количество паролей</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>10</y>
     <width>191</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(255, 255, 255);
font: 75 8pt &quot;Rubik&quot;;</string>
   </property>
   <property name="text">
    <string>Сгенерированные пароли:</string>
   </property>
  </widget>
  <widget class="QPushButton" name="go_away_button">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>130</y>
     <width>191</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
   <property name="text">
    <string>Выйти</string>
   </property>
  </widget>
  <widget class="QSpinBox" name="kolvo_spin">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>42</width>
     <height>22</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
   <property name="minimum">
    <number>1</number>
   </property>
  </widget>
  <widget class="QSpinBox" name="length_spin">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>61</width>
     <height>22</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 75 8pt &quot;Rubik&quot;;
background-color: rgb(255, 255, 255);
border: 1px solid gray;</string>
   </property>
   <property name="minimum">
    <number>1</number>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
format_check = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>PasswordCheck</class>
 <widget class="QDialog" name="PasswordCheck">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>305</width>
    <height>253</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>305</width>
    <height>253</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>305</width>
    <height>253</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Dialog</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(34, 158, 217);</string>
  </property>
  <widget class="QLineEdit" name="password">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>10</y>
     <width>271</width>
     <height>20</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
  </widget>
  <widget class="QProgressBar" name="oneoffour">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>271</width>
     <height>16</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
   <property name="value">
    <number>0</number>
   </property>
   <property name="textVisible">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QTextBrowser" name="problems">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>80</y>
     <width>271</width>
     <height>171</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(255, 255, 255);</string>
   </property>
   <property name="html">
    <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Возможные проблемы пароля:&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QLabel" name="Qualitylabel">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>60</y>
     <width>101</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(format_register)
        uic.loadUi(f, self)
        self.setWindowTitle("Registration")
        self.haveacc_button.clicked.connect(self.go_to_login)
        self.haveacc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_reg.setPlaceholderText("Логин")
        self.pass_reg.setPlaceholderText("Пароль")
        self.repeatpass_reg.setPlaceholderText("Повтор пароля")
        self.registrationButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor)
        )  # Красивый курсор
        self.registrationButton.clicked.connect(self.saveinfo)
        rx = QRegularExpression(
            "^[a-zA-Z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$"
        )  # Ограничение вводимых символов
        validator = QRegularExpressionValidator(rx)
        self.login_reg.setValidator(validator)
        self.pass_reg.setValidator(validator)
        self.repeatpass_reg.setValidator(validator)

    def go_to_login(self):
        self.enterEv = Enter()
        self.enterEv.show()
        self.close()

    def go_to_main_window(self):
        self.mainEv = Main(self.login_reg.text())
        self.mainEv.show()
        self.close()

    def saveinfo(self):
        self.connection = sl.connect("../managerdatabase.db")
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS "USERS" (
                "ID"        INTEGER PRIMARY KEY AUTOINCREMENT,
                "LOGIN"     TEXT NOT NULL,
                "PASSWORD"  TEXT NOT NULL
            )
        """
        )
        if self.login_reg.text() != "" and self.pass_reg.text() != "":
            if self.check_is_not_in_db():
                if self.password_are_same():
                    self.connection.execute(
                        """INSERT INTO "USERS" (LOGIN, PASSWORD) VALUES (?, ?)""",
                        (self.login_reg.text(), encrypt(str(self.pass_reg.text()))),
                    )
                    self.connection.commit()
                    self.errorlabel.setText("")
                    self.go_to_main_window()
                else:
                    self.errorlabel.setText("Пароли неодинаковые")
            else:
                self.errorlabel.setText("Логин уже существует")
        else:
            self.errorlabel.setText("Вы не ввели логин или пароль")
        self.connection.close()

    def check_is_not_in_db(self):  # Проверка на новизну логина
        self.connection = sl.connect("../managerdatabase.db")
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM USERS WHERE LOGIN = ?", (self.login_reg.text(),)
        )
        result = cursor.fetchone()[0]
        return result == 0

    def password_are_same(self):  # Проверка на совпадение
        return self.pass_reg.text() == self.repeatpass_reg.text()


class Enter(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(format_enter)
        uic.loadUi(f, self)
        self.setWindowTitle("Enter")
        self.login_ent.setPlaceholderText("Логин")
        self.pass_ent.setPlaceholderText("Пароль")
        self.noacc_lab.clicked.connect(self.go_to_reg)
        self.noacc_lab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.enterButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.enterButton.clicked.connect(self.check_info)
        rx = QRegularExpression(
            "^[a-zA-Z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$"
        )  # Ограничение вводимых символов
        validator = QRegularExpressionValidator(rx)
        self.login_ent.setValidator(validator)
        self.pass_ent.setValidator(validator)

    def go_to_reg(self):
        self.regEv = Register()
        self.regEv.show()
        self.close()

    def check_is_in_db(self):
        self.connection = sl.connect("../managerdatabase.db")
        cursor = self.connection.cursor()
        self.connection.execute(
            """
                    CREATE TABLE IF NOT EXISTS "USERS" (
                        "ID"        INTEGER PRIMARY KEY AUTOINCREMENT,
                        "LOGIN"     TEXT NOT NULL,
                        "PASSWORD"  TEXT NOT NULL
                    )
                """
        )
        cursor.execute(
            "SELECT COUNT(*) FROM USERS WHERE LOGIN = ?", (self.login_ent.text(),)
        )
        result = cursor.fetchone()[0]
        return result != 0

    def check_is_password(self):
        self.connection = sl.connect("../managerdatabase.db")
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT PASSWORD FROM USERS WHERE LOGIN = ?",
            (self.login_ent.text(), )
        )

        result = cursor.fetchone()[0]
        return decrypt(result) == self.pass_ent.text()

    def check_info(self):
        self.connection = sl.connect("../managerdatabase.db")
        if self.login_ent.text() != "" and self.pass_ent.text() != "":
            if self.check_is_in_db() and self.check_is_password():
                self.connection.commit()
                self.errorlabel_ent.setText("")
                self.go_to_main_window()
            else:
                self.errorlabel_ent.setText("Неверный логин или пароль")
        else:
            self.errorlabel_ent.setText("Вы не ввели логин или пароль")

    def go_to_main_window(self):
        self.mainEv = Main(self.login_ent.text())
        self.mainEv.show()
        self.close()


class Main(QMainWindow):
    def __init__(self, user_login=None):
        super().__init__()
        f = io.StringIO(format_main)
        uic.loadUi(f, self)
        self.setWindowTitle("PasswordManager")
        self.login = user_login
        conn = sl.connect("../managerdatabase.db")
        c = conn.cursor()
        c.execute(
            """
                    CREATE TABLE IF NOT EXISTS "DATA" (
                        "USER_ID"   INTEGER NOT NULL,
                        "ID"        INTEGER PRIMARY KEY AUTOINCREMENT,
                        "LOGIN"     TEXT NOT NULL,
                        "PASSWORD"  TEXT NOT NULL,
                        "NAME"      TEXT NOT NULL,
                        "URL"       TEXT
                    )
                """
        )
        conn.commit()
        conn.close()
        self.generator_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.anthrman_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.set_button_styles()
        self.anthrman_button.clicked.connect(self.show_confirmation_dialog)
        self.generator_button.clicked.connect(self.generator_dialog)
        self.check_button.clicked.connect(self.go_check)
        self.search_line.setPlaceholderText("Поиск по названию")
        self.change_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.clicked.connect(self.go_to_add)
        self.update_table()
        self.passwordTable.itemClicked.connect(self.more_information)
        self.url_label.mousePressEvent = self.label_clicked
        self.url_label.setStyleSheet(
            "color: blue; background-color: rgb(226, 226, 226); text-decoration: underline;"
        )
        self.url_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.clicked.connect(self.remove_info)
        self.change_button.clicked.connect(self.go_to_change)
        self.search_line.textChanged.connect(self.search)

    def search(self):
        text = self.search_line.text().lower()
        for row in range(self.passwordTable.rowCount()):
            item = self.passwordTable.item(row, 0)
            if item and text in item.text().lower():
                self.passwordTable.showRow(row)
            else:
                self.passwordTable.hideRow(row)

    def go_to_change(self):
        p = [
            self.login_settext.text(),
            self.password_settext.text(),
            self.name_label.text(),
            self.url_label.text(),
        ]
        if len(p) >= 3 and p[0] != '' and p[1] != '' and p[2] != '':
            self.changeEv = ChangeDialog(p, self.login, self)
            self.changeEv.show()

    def remove_info(self):
        conn = sl.connect("../managerdatabase.db")
        cursor = conn.cursor()
        cursor.execute(
            """
                    DELETE FROM DATA 
                    WHERE USER_ID = (SELECT ID FROM USERS WHERE LOGIN = ?) 
                    AND NAME = ?
                """,
            (self.login, self.name_label.text()),
        )
        conn.commit()
        self.update_table()
        self.login_settext.setText("")
        self.password_settext.setText("")
        self.url_label.setText("")
        self.name_label.setText("")
        self.qualitebar.setValue(0)

    def label_clicked(self, event):
        webbrowser.open(self.url_label.text())

    def update_table(self):
        conn = sl.connect("../managerdatabase.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT NAME, LOGIN, URL FROM DATA WHERE USER_ID = (SELECT ID FROM USERS WHERE LOGIN = ?)",
            (self.login,),
        )
        rows = cursor.fetchall()
        self.passwordTable.setRowCount(0)
        for row_data in rows:
            row_position = self.passwordTable.rowCount()
            self.passwordTable.insertRow(row_position)
            self.passwordTable.setItem(row_position, 0, QTableWidgetItem(row_data[0]))
            self.passwordTable.setItem(row_position, 1, QTableWidgetItem(row_data[1]))
            self.passwordTable.setItem(
                row_position, 2, QTableWidgetItem(row_data[2] if row_data[2] else "")
            )
        conn.close()

    def set_button_styles(self):
        button_style = """
        QPushButton {
            font: 75 10pt "Rubik";
            border: 0px;
            color: rgb(34, 170, 255);
            background-color: rgb(255, 255, 255);
        }
        QPushButton:hover {
            background-color: rgb(236, 236, 236);
        }
        """
        self.generator_button.setStyleSheet(button_style)
        self.anthrman_button.setStyleSheet(button_style)
        self.check_button.setStyleSheet(button_style)

    def more_information(self, item):
        row = item.row()
        title = self.passwordTable.item(row, 0).text()
        conn = sl.connect("../managerdatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT LOGIN, PASSWORD, URL FROM DATA WHERE NAME = ?", (title,))
        result = cursor.fetchone()
        self.login_settext.setText(result[0])
        self.password_settext.setText(decrypt(result[1]))
        self.url_label.setText(result[2])
        self.name_label.setText(title)
        self.check(result[1])

    def check(self, password):
        self.qualitebar.setValue(0)
        min_length = 10
        cur_pass = decrypt(password)
        has_upper = re.search(r"[A-Z]", cur_pass) is not None
        has_lower = re.search(r"[a-z]", cur_pass) is not None
        has_digit = re.search(r"\d", cur_pass) is not None
        has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', cur_pass) is not None
        is_long_enough = len(cur_pass) >= min_length
        self.problems = 0
        if not has_upper:
            self.problems += 1
        if not has_lower:
            self.problems += 1
        if not has_digit:
            self.problems += 1
        if not has_special:
            self.problems += 1
        if not is_long_enough:
            self.problems += 1
        if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
            self.qualitelab(100)
        elif self.problems == 1:
            self.qualitelab(80)
        elif self.problems == 2:
            self.qualitelab(60)
        elif self.problems == 3:
            self.qualitelab(40)
        elif self.problems == 4:
            self.qualitelab(20)

    def qualitelab(self, percent):
        self.qualitebar.setValue(percent)
        if percent == 100:
            self.qualitebar.setStyleSheet(
                "QProgressBar::chunk { background-color: green; border-radius:15px;}"
            )
        elif percent == 80:
            self.qualitebar.setStyleSheet(
                "QProgressBar::chunk { background-color: lime; border-radius:15px;}"
            )
        elif percent == 60:
            self.qualitebar.setStyleSheet(
                "QProgressBar::chunk { background-color: orange; border-radius:15px;}"
            )
        else:
            self.qualitebar.setStyleSheet(
                "QProgressBar::chunk { background-color: red; border-radius:15px;}"
            )

    def show_confirmation_dialog(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Подтверждение")
        msg_box.setText("Вы уверены, что хотите сменить пользователя?")
        msg_box.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        reply = msg_box.exec()
        if reply == QMessageBox.StandardButton.Yes:
            self.go_to_enter()
        else:
            pass

    def generator_dialog(self):
        dialog = GeneratorDialog(self)
        dialog.exec()

    def go_to_enter(self):
        self.enterEv = Enter()
        self.enterEv.show()
        self.close()

    def go_check(self):
        dialog = CheckPassword(self)
        dialog.exec()

    def go_to_add(self):
        dialog = Adding(self.login, self)
        dialog.exec()


class ChangeDialog(QDialog):
    def __init__(self, p, log, parent=None):
        super(ChangeDialog, self).__init__(parent)
        f = io.StringIO(format_change)
        uic.loadUi(f, self)
        self.setWindowTitle("ChangeInformation")
        self.login_usera = log
        if len(p) == 4:
            self.url_edit.setText(f"{p[3]}")
        self.login_edit.setText(f"{p[0]}")
        self.name_edit.setText(f"{p[2]}")
        self.password_edit.setText(f"{p[1]}")
        self.ready_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_button.clicked.connect(self.go_back)
        self.ready_button.clicked.connect(self.go_edit)
        self.name_izn = self.name_edit.text()
        self.main = parent
        conn = sl.connect("../managerdatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM DATA WHERE NAME = ?", (p[2],))
        self.result = cursor.fetchone()
        conn.close()

    def check_is_not_in_db(self):
        self.connection = sl.connect("../managerdatabase.db")
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM DATA WHERE NAME = ? AND USER_ID = (SELECT ID FROM USERS WHERE LOGIN = ?)",
            (self.name_edit.text(), self.login_usera),
        )
        result = cursor.fetchone()[0]
        return result == 0

    def go_edit(self):
        self.error_label.setText("")
        login = self.login_edit.text()
        password = self.password_edit.text()
        name = self.name_edit.text()
        url = self.url_edit.text()
        record_id = self.result[0]
        try:
            if login != "" and password != "" and name != "":
                if name == self.name_izn or self.check_is_not_in_db():
                    conn = sl.connect("../managerdatabase.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        """
                            UPDATE DATA 
                            SET LOGIN = ?, PASSWORD = ?, NAME = ?, URL = ? 
                            WHERE ID = ? AND USER_ID = (SELECT ID FROM USERS WHERE LOGIN = ?)
                        """,
                        (login, password, name, url, record_id, self.login_usera),
                    )
                    conn.commit()
                    self.main.login_settext.setText(login)
                    self.main.password_settext.setText(password)
                    self.main.url_label.setText(url)
                    self.main.name_label.setText(name)
                    self.main.check(password)
                    conn.close()
                    self.main.update_table()
                    self.name_izn = name
                    QMessageBox.information(self, "Успех", "Данные успешно обновлены.")
                else:
                    self.error_label.setText("Такое имя уже есть")
            else:
                self.error_label.setText("Вы не вписали какие-то данные")
        except sl.Error as e:
            QMessageBox.critical(
                self, "Ошибка", f"Произошла ошибка при обновлении данных: {str(e)}"
            )

    def go_back(self):
        self.close()


class GeneratorDialog(QDialog):
    def __init__(self, parent=None):
        super(GeneratorDialog, self).__init__(parent)
        f = io.StringIO(format_generator)
        uic.loadUi(f, self)
        self.setWindowTitle("PasswordGenerator")
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!;%:?*()@#$^&"
        self.go_button.clicked.connect(self.generation)
        self.go_away_button.clicked.connect(self.go_away)
        self.save_button.clicked.connect(self.save_file)
        self.paroli.setReadOnly(True)
        self.par_g = []

    def generation(self):
        self.paroli.clear()
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = string.punctuation
        for i in range(int(self.kolvo_spin.value())):
            password = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(special_chars),
            ]
            all_characters = lowercase + uppercase + digits + special_chars
            password += random.choices(
                all_characters, k=int(self.length_spin.value()) - 4
            )
            random.shuffle(password)
            self.paroli.insertPlainText("".join(password) + "\n")
            self.par_g.append("".join(password))

    def save_file(self):
        if not self.par_g:
            QMessageBox.warning(self, "Ошибка", "Сначала сгенерируйте пароль!")
            return
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Сохранить пароль", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, "a") as file:
                    for i in self.par_g:
                        file.write(i + "\n")
                QMessageBox.information(
                    self, "Успех", f"Пароль сохранен в файл {file_name}"
                )
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")

    def go_away(self):
        self.close()


class CheckPassword(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        f = io.StringIO(format_check)
        uic.loadUi(f, self)
        self.setWindowTitle("CheckPassword")
        self.password.setPlaceholderText("Проверяемый пароль")
        self.password.textChanged.connect(self.check)
        rx = QRegularExpression(
            "^[a-zA-Z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$"
        )  # Ограничение вводимых символов
        validator = QRegularExpressionValidator(rx)
        self.password.setValidator(validator)

    def check(self):
        self.problems.clear()
        self.problems.insertPlainText("Возможные проблемы с паролем:" + "\n")
        self.oneoffour.setValue(0)
        self.Qualitylabel.setText("")
        min_length = 10
        cur_pass = self.password.text()
        has_upper = re.search(r"[A-Z]", cur_pass) is not None
        has_lower = re.search(r"[a-z]", cur_pass) is not None
        has_digit = re.search(r"\d", cur_pass) is not None
        has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', cur_pass) is not None
        is_long_enough = len(cur_pass) >= min_length
        self.problems_spi = []
        if not has_upper:
            self.problems_spi.append(
                "Пароль должен содержать хотя бы одну заглавную букву."
            )
        if not has_lower:
            self.problems_spi.append(
                "Пароль должен содержать хотя бы одну строчную букву."
            )
        if not has_digit:
            self.problems_spi.append("Пароль должен содержать хотя бы одну цифру.")
        if not has_special:
            self.problems_spi.append(
                "Пароль должен содержать хотя бы один специальный символ."
            )
        if not is_long_enough:
            self.problems_spi.append(
                f"Пароль должен содержать минимум {min_length} символов."
            )
        if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
            self.problems.insertPlainText("Проблем с паролем нет!")
            self.qualitelab(100)
        elif len(self.problems_spi) == 1:
            self.qualitelab(80)
        elif len(self.problems_spi) == 2:
            self.qualitelab(60)
        elif len(self.problems_spi) == 3:
            self.qualitelab(40)
        elif len(self.problems_spi) == 4:
            self.qualitelab(20)

    def qualitelab(self, percent):
        self.oneoffour.setValue(percent)
        if percent == 100:
            self.Qualitylabel.setText("Сильный пароль")
            self.Qualitylabel.setStyleSheet("color: green;")
            self.oneoffour.setStyleSheet(
                "QProgressBar::chunk { background-color: green; }"
            )
        elif percent == 80:
            self.Qualitylabel.setText("Хороший пароль")
            self.Qualitylabel.setStyleSheet("color: lime;")
            self.oneoffour.setStyleSheet(
                "QProgressBar::chunk { background-color: lime; }"
            )

        elif percent == 60:
            self.Qualitylabel.setText("Средний пароль")
            self.Qualitylabel.setStyleSheet("color: orange;")
            self.oneoffour.setStyleSheet(
                "QProgressBar::chunk { background-color: orange; }"
            )
        else:
            self.Qualitylabel.setText("Слабый пароль")
            self.Qualitylabel.setStyleSheet("color: red;")
            self.oneoffour.setStyleSheet(
                "QProgressBar::chunk { background-color: red; }"
            )
        if self.problems_spi:
            for i in self.problems_spi:
                self.problems.insertPlainText(i + "\n")


class Adding(QDialog):
    def __init__(self, login, parent=None):
        self.main = parent
        super(QDialog, self).__init__(parent)
        f = io.StringIO(format_add)
        uic.loadUi(f, self)
        self.setWindowTitle("AddInformation")
        self.login_info = login
        self.login.setPlaceholderText("Логин")
        self.password.setPlaceholderText("Пароль")
        self.url.setPlaceholderText("Ссылка в форманте https://сайт(Необязательно)")
        self.name.setPlaceholderText("Название сервиса")
        self.adddan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_button.clicked.connect(self.go_back)
        self.adddan.clicked.connect(self.add_information)
        rx1 = QRegularExpression(
            "^[a-zA-Z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$"
        )  # Ограничение вводимых символов
        validator1 = QRegularExpressionValidator(rx1)
        self.password.setValidator(validator1)
        rx2 = QRegularExpression(
            "^[a-zA-Z0-9 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~]*$"
        )  # Ограничение вводимых символов
        validator2 = QRegularExpressionValidator(rx2)
        self.login.setValidator(validator2)

    def go_back(self):
        self.close()

    def check_is_not_in_db(self):
        self.connection = sl.connect("../managerdatabase.db")
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM DATA WHERE NAME = ? AND USER_ID = (SELECT ID FROM USERS WHERE LOGIN = ?)",
            (self.name.text(), self.login_info),
        )
        result = cursor.fetchone()[0]
        return result == 0

    def add_information(self):
        self.error_label.setText("")
        if (
            self.login.text() != ""
            and self.password.text() != ""
            and self.name.text() != ""
        ):
            conn = sl.connect("../managerdatabase.db")
            c = conn.cursor()
            c.execute("SELECT id FROM USERS WHERE LOGIN=?", (self.login_info,))
            user_id = c.fetchone()[0]
            if self.url.text() == "":
                url = None
            else:
                url = self.url.text()
            if self.check_is_not_in_db():
                c.execute(
                    """
                                INSERT INTO "DATA" (USER_ID, LOGIN, PASSWORD, NAME, URL) VALUES (?, ?, ?, ?, ?)
                            """,
                    (
                        user_id,
                        self.login.text(),
                        encrypt(self.password.text()),
                        self.name.text(),
                        url,
                    ),
                )
                conn.commit()
                conn.close()
                self.login.setText("")
                self.password.setText("")
                self.url.setText("")
                self.name.setText("")
                self.label.setText("Данные добавлены")
                self.main.update_table()
            else:
                self.error_label.setText("Такое имя существует")
        else:
            self.error_label.setText("Вы не ввели данные")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Register()
    ex.show()
    sys.exit(app.exec())


"""
    сделано кровью и потом ;)
"""