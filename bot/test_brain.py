#!/usr/bin/env python

# Copyright (C) 2008 Sebastian Silva Fundacion FuenteLibre sebastian@fuentelibre.org
#
# HablarConSara.activity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HablarConSara.activity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HablarConSara.activity.  If not, see <http://www.gnu.org/licenses/>.

#coding=utf-8

import aiml
import os.path

k = aiml.Kernel()
k.loadBrain("sara.brn")

while True: print k.respond(raw_input("Pregunta > ")) 