import argparse
import sys
import h5py
import numpy as np
from ssa import  SSA
import time, math
from mintpy.utils import readfile, writefile, ptime, utils as ut
from mintpy.objects import timeseries

def create_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('timeseries_file', 
                    help='time-series file to do SSA \n'
                    'i.e.:geo_timeseries_GACOS_ramp_demErr.h5 (MintPy)\n')
    parser.add_argument("-w", "--window", 
                    type=int,
                    help='Widow length (default is 7) ')
    parser.add_argument('-o', '--output', dest='outfile', help='output file name (default ssa.h5)')
    # args=parser.parse_args()
    # computing
    # parser = arg_group.add_memory_argument(parser)
    return parser
def cmd_line_parse(iargs=None):
    parser = create_parser()
    inps = parser.parse_args(args=iargs)
    inps.key = readfile.read_attribute(inps.timeseries_file)['FILE_TYPE']
    if inps.key not in ['timeseries', 'giantTimeseries', 'HDFEOS']:
        raise Exception('input file is {}, NOT timeseries!'.format(inps.key))
    if not inps.window:
        inps.window = int(7)
    if not inps.outfile:
        outname = 'ssa'
        outname += '.h5'
        inps.outfile = outname
    tsobj = timeseries(inps.timeseries_file)
    return inps
def is_number(s):
    if s==0:
        return False
    elif math.isnan(s):
         return False
    else:
        return True
def main(iargs=None):
    # if cmd:
         # iargs = cmd.split()[1:]
    inps = cmd_line_parse(iargs)
    date_list = timeseries(inps.timeseries_file).get_date_list()
    data, atr = readfile.read(inps.timeseries_file)
    length, width = int(atr['LENGTH']), int(atr['WIDTH'])
    N_dates=len(date_list)
    # with h5py.File(inps.timeseries_file,'r') as f:
    #     data = f['timeseries'][:]
    #     date_list = f['date'][:]
    data_matrix = np.empty((len(date_list),length,width))
    data_matrix[:] = np.nan
    start_time = time.time()
    for i in range(length):
        for j in range(width):
            if is_number(sum(data[:,i,j])):
                a=SSA(data[:,i,j], inps.window)
                data_matrix[:,i,j]=a.reconstruct([0,1])  # Grouping recostructed components, by defaults it takes F1 and F2 as trend
    m, s = divmod(time.time()-start_time, 60)
    block= [0,N_dates,0,length,0,width]
    writefile.layout_hdf5(inps.outfile, metadata=atr, ref_file=inps.timeseries_file)
    writefile.write_hdf5_block(inps.outfile,
                          data=data_matrix,
                          datasetName='timeseries',
                          block=block,
                          print_msg=False)


    print(inps.timeseries_file)
    print(inps.window)
    # print(date_list)
    print(length,width)
    print('time used: {:02.0f} mins {:02.1f} secs.'.format(m, s))
if __name__ == '__main__':
    main(sys.argv[1:])    

