#!/usr/bin/python
#-*-coding:utf-8-*-
###############################################################################
#       imbatcher - Programa para separar lotes de fotos similares
#               Compara imágenes de a dos
#       Copyright (C) 2011  Joaquín Bogado <joaquinbogado en gmail.com>
#       Thenkiu ale santos :)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

import pygame
import pygame.camera
import sys

def startcam(res, device, vervose):
    (w,h)=res.split('x')
    w=int(w)
    h=int(h)
    res=(w,h)
    c = pygame.camera.Camera(device, res)
    c.start()
    frame = c.get_image()
    c.stop()
    if c.get_size() != res:
        print "Resolución no soportada. Se cambia a " + str(c.get_size())
        res = c.get_size()
    (w, h) = res
    screen = pygame.display.set_mode((w, h))
    s =  pygame.Surface((w, h), depth=24)
    crossair_orig = pygame.image.load("crossair.png")
    crossair = crossair_orig
    angle=0
    crossrect = crossair.get_rect()
    crossrect = crossrect.move((w/2)-150,(h/2)-150 )
    c.start()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.stop()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'left':
                    angle+=5
                    crossair = pygame.transform.rotate(crossair_orig,angle)
                if pygame.key.name(event.key) == 'right':
                    angle-=5
                    crossair = pygame.transform.rotate(crossair_orig, angle)
                crossrect = crossair.get_rect()
                crossrect.center=(w/2, h/2)
        s1 = c.get_image()
        screen.blit(s1, (0,0))
        screen.blit(crossair, crossrect)
        pygame.display.flip()

def __Main__():
    import argparse
    pygame.init()
    pygame.camera.init()
    parser = argparse.ArgumentParser(description='Software de soporte para la puesta en estación de monturas ecuatoriales y alineación polar por el método de deriva utilizando un dispositivo compatible con V4L2.')
    parser.add_argument('-r', '--resolution', dest='res', default='800x600', help='Resolusión de la cámara (ancho x alto). Default=800x600.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Salida útil para debug.')
    if pygame.camera.list_cameras().__len__() == 0:
        print "No hay dispositivos compatibles. Conecte un dispositivo V4L2 compatible."
        sys.exit(1)
    parser.add_argument('-d', '--device', dest='device', choices=pygame.camera.list_cameras(), default=pygame.camera.list_cameras()[0], help='Dispositivo de video')
    args = parser.parse_args()
    if args.verbose:
        print args.res
        print args.device
        print args.verbose
    startcam(args.res, args.device, args.verbose)

__Main__()
