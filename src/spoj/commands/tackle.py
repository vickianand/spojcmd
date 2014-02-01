# -*- coding: utf-8 -*-
import sys, time, os
from . import Command
from . import settings
from ..settings import _url
from ..utils import unescape as _, display_in_browser


LANG_COMP = {
        'py':    {4: 'python 2.7'},
        'rb':    {17: 'ruby 1.9.3'},
        'php':   {29: 'php 5.2.6'},
        'java':  {10: 'java SE 6'},
        'jar':   {24: 'java SE 6'},
        'pas':   {22: 'fpc 2.2.4', 2: 'gpc 20070904'},
        'pl':    {3: 'perl 5.12.1'},
        'scala': {39: 'scala 2.8.0'},
        'sed':   {46: 'sed 4.2'},
        'c':     {11: 'gcc 4.3.2'},
        'cpp':   {41: 'g++ 4.3.2'},
        'cs':    {27: 'gmcs 2.0.1'},
        'asm':   {13: 'nasm 2.03.01'},
        'go':    {114: 'gc 2010-07-14'},
        'sh':    {104: 'bash 4.0.37'},
        }

#        'cpp':   {41: 'g++ 4.3.2', 1: 'g++ 4.0.0-8'},
#        'py':    {4: 'python 2.7', 116: 'python 3.2.3'},


class TackleProblem(Command):
    def __init__(self):
        super(TackleProblem, self).__init__('tackle',
                'upload a solution to %s' % settings.ROOM_URL())
        self.wait_time = 4

    def add_arguments(self, parser):
        parser.add_argument('file_name', help='file_name must be formatted \
                like this: <problem_id>.<lang_extention>\n for example: \
                ABR0001.py')

    def doing(self, args):


        #if settings.compiler_id:
        #    cmp_id = int(settings.compiler_id)
        #    print 'compiler id loaded from settings: %d' % cmp_id
        #else:
        cmp_id, cmp_name = self.get_compiler(args.file_name)
        print 'Your solution will be compiled via %s(%d)' % (cmp_name,cmp_id)

        self.auth_if()
        problem_id = args.file_name.split('.')[0]
        url = _url('submit/complete')
        files = {'subm_file': (args.file_name, open(args.file_name, 'r'))}
        r = self.post(url,
                data={'lang':cmp_id,
                    'problemcode':problem_id,
                    'file': '',
                    'submit': 'submit',
                    },
                files=files)
        loop = True
        while loop:
            print 'waiting result for %d seconds!' % self.wait_time
            time.sleep(self.wait_time)
	    os.system('clear')
            print '\n \t\t\t**result** \n'
            result = self.get_result(problem_id)
            print '   date: %s\n   name: %s\n   status: %s\n   time: %s\n   memory: %s\n\n' %\
                    result
            if u'ing' not in result[2]:
		col="31m"
		if 'accept' in result[2]:
			col="32m"
		print "\t\t\033[5;"+col+result[2].upper()+"\033[0m"
		print "\n"	
                loop = False
            else:
                print 'fetching result again, ',


    def get_compiler(self, file_name):
        ext = file_name.split('.')[-1]
        compilers = LANG_COMP.get(ext, {})

        compiler_id = -1
        compiler_name = ''

        if len(compilers) == 0:
            raise ValueError('oops, don\'t have a compiler for your file')
        elif len(compilers) > 1:
            print 'there are many compilers,',
            while True:
                print 'please choose one of followings:'
                for k, v in compilers.items():
                    print '%3d: %s' % (k, v)
                try:
                    compiler_id = input()
                    compiler_name = compilers[compiler_id]
                    break
                except:
                    print 'invalid!, only choose one id of provided'
        else:
            compiler_id, compiler_name = compilers.items()[0]

        return compiler_id, compiler_name

    def get_result(self, problem_id):
        '''
        return last result of the problem
        '''
        url = _url('status/%s,%s' % (problem_id, settings.get_user_name()))
        __, soup = self.get_soup(url)
        #display_in_browser(__.text)
        rows = soup.findAll('table', {'class': 'problems'})[1].\
                findAll('tr')[1].findAll('td')
        date = rows[2].text
        name = _(rows[3].text)
        status = _(rows[4].text)
        status = status.replace('edit', '')
        status = status.replace('running', 'jasmine')
	status = status.replace('run', '')
	status = status.replace('jasmine', 'running')
        time = rows[5].find('a').text
        mem = rows[6].text

        return (date, name, status, time, mem)
