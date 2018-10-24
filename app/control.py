# -*- coding: utf-8 -*-

import time
import datetime

# https://gpiozero.readthedocs.io/en/stable/
from gpiozero import LED

# https://github.com/adafruit/Adafruit_Python_DHT
import Adafruit_DHT


# # Радиатор отопления
# RADIATOR = LED(16)

# # Основное освещение
# MAIN_LAMP = LED(20)

# # Инфракрасная лампа
# HEAT_LAMP = LED(21)

# Датчик температуры и влажности
TEMP_SENSOR_PIN = 2

# Минимальная температура в курятнике,
# при достижении которой должен ВКЛЮЧИТЬСЯ радиатор
MIN_ALLOWED_TEMP = 10.0

# Минимальная температура в курятнике,
# при достижении которой должен ОТКЛЮЧИТЬСЯ радиатор
MAX_ALLOWED_TEMP = 13.0

# Час включения освещения (утро)
WAKE_UP_HOUR = 6

# Час отключения освещения (утро)
# DISABLE_LIGHT_MORNING_HOUR = 11

# Час включения освещения (вечер)
# ENABLE_LIGHT_EVENING_HOUR = 16

# Час отключения освещения (ночь)
SLEEP_HOUR = 20

# Задержка перед включением основного света
DELAY_MAIN_LAMP_WAKEUP = 50

# Задержка перед отключением дежурного света
DELAY_HEAT_LAMP_SLEEP = 30


def writeLog(msg):
    now = datetime.datetime.now()

    f = open('log.txt', 'a')
    f.write("{} - {}".format(now, msg))
    f.close()


def getCurrentTempHum():
    return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, TEMP_SENSOR_PIN, retries=15, delay_seconds=0.5)
    # return 10, 20

# while True:

#     time.sleep(60)

#     now = datetime.datetime.now()

#     # Получаем текущую температуру и влажность
#     humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, TEMP_SENSOR_PIN)

#     #
#     # Работа с обогревателем
#     #
#     if temp < MIN_ALLOWED_TEMP:
#         RADIATOR.on()
#         writeLog("{}°C {}% - Включение радиатора".format(temp, humidity))

#     if temp > MAX_ALLOWED_TEMP:
#         RADIATOR.off()
#         writeLog("{}°C {}% - Отключение радиатора".format(temp, humidity))

#     # чтобы одновременно не срабатывали сразу несколько реле
#     time.sleep(5)

#     #
#     # Утром включаем сначала дежурное освещение
#     #
#     if now.hour == WAKE_UP_HOUR:
#         HEAT_LAMP.on()

#         writeLog("{}°C {}% - Включение инфракрасной лампы".format(temp, humidity))

#         # Через 50 минут включаем основное
#         if (now.minute > DELAY_MAIN_LAMP_WAKEUP):
#             MAIN_LAMP.on()

#             # чтобы одновременно не срабатывали сразу несколько реле
#             time.sleep(5)

#             # Отключаем дежурное (инфракрасная лампа)
#             HEAT_LAMP.off()

#             writeLog("{}°C {}% - Отключение инфракрасной лампы, включение основного".format(temp, humidity))


#     #
#     # Если было отключение электричества включаем все что нужно
#     #
#     if now.hour > WAKE_UP_HOUR and now.hour < SLEEP_HOUR:
#         MAIN_LAMP.on()

#     #
#     # Отключение света вечером
#     #
#     if now.hour == SLEEP_HOUR:

#         # Включаем дежурное освещение на DELAY_HEAT_LAMP_SLEEP минут
#         if now.minute < DELAY_HEAT_LAMP_SLEEP:
#            HEAT_LAMP.on()

#            writeLog("{}°C {}% - Включение инфракрасной лампы".format(temp, humidity))

#         # Через DELAY_HEAT_LAMP_SLEEP минут - отключаем дежурное
#         else:
#             HEAT_LAMP.off()

#             writeLog("{}°C {}% - Отключение инфракрасной лампы".format(temp, humidity))

#         # чтобы одновременно не срабатывали сразу несколько реле
#         time.sleep(5)

#         # отключаем основное освещение
#         MAIN_LAMP.off()

#         writeLog("{}°C {}% - Отключение основного".format(temp, humidity))
