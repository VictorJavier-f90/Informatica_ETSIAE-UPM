# -*- coding: utf-8 -*-
"""
segundos a  hora minuto y segundo
"""

segundos = 3725

horas = segundos // 3600
minutos = (segundos%3600)//60
segundo = (segundos%3600)%60

print(segundos, ' son: ',horas, 'horas, ', minutos, ' minutos, ',
      segundo, ' segundos')