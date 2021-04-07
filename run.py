import os
from multiprocessing import Pool

processes = ('Application.py', 'refreshtime.py')


def run_process(process):
    os.system(f'python {process}')


if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map(run_process, processes)
