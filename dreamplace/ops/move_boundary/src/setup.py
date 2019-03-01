##
# @file   setup.py
# @author Yibo Lin
# @date   Jun 2018
#

import os 
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

def add_prefix(filename):
    return os.path.join('${CMAKE_CURRENT_SOURCE_DIR}/src', filename)

modules = []

modules.extend([
    CppExtension('move_boundary_cpp', 
        [
            add_prefix('move_boundary.cpp')
            ]),
    ])

if not "${CUDA_FOUND}" or "${CUDA_FOUND}".upper() == 'TRUE': 
    modules.extend([
            CUDAExtension('move_boundary_cuda', 
                [
                    add_prefix('move_boundary_cuda.cpp'),
                    add_prefix('move_boundary_cuda_kernel.cu')
                    ], 
                libraries=['cusparse', 'culibos']
                ),
        ])

setup(
        name='move_boundary',
        ext_modules=modules,
        cmdclass={
            'build_ext': BuildExtension
            })