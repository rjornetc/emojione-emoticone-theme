#! /usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir, path



emoji_path = path.join(path.curdir,'emojione','non-added')

print('<?xml version=\'1.0\'?>\n' +
      '<messaging-emoticon-map>')

for filename in listdir(emoji_path):
    if filename != 'non-added' and filename != 'emoticons.xml':
        code = filename.split('.')[0]
        codelist = code.split('-')
        print('    <emoticon file="' + code + '" >\n' +
              '        <string>' + unichr(int(codelist[0],16)) + unichr(int(codelist[1],16)) + '</string>\n' +
              '    </emoticon>')

print('</messaging-emoticon-map>')