#!/bin/bash

# setup dependencies for PIConGPU for CMake and runtime usage

set -e
set -o pipefail

if [ -d "/opt/pngwriter" ] ; then
  export PNGWRITER_ROOT=/opt/pngwriter/0.7.0
else
  # pngwriter is currently install to the / instead of /opt
  export PNGWRITER_ROOT=/pngwriter/0.7.0
fi
export CMAKE_PREFIX_PATH=$PNGWRITER_ROOT:$CMAKE_PREFIX_PATH
export LD_LIBRARY_PATH=$PNGWRITER_ROOT/lib:$LD_LIBRARY_PATH

export HDF5_ROOT=/opt/hdf5/1.10.7/
export LD_LIBRARY_PATH=$HDF5_ROOT/lib:$LD_LIBRARY_PATH

export ADIOS2_ROOT=/opt/adios/2.7.1
export CMAKE_PREFIX_PATH=$ADIOS2_ROOT:$CMAKE_PREFIX_PATH
export PATH=$ADIOS2_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$ADIOS2_ROOT/lib:$LD_LIBRARY_PATH

if [ -z "$DISABLE_ISAAC" ] ; then
  export ICET_ROOT=/opt/icet/2.9.0
  export CMAKE_PREFIX_PATH=$ICET_ROOT/lib:$CMAKE_PREFIX_PATH
  export LD_LIBRARY_PATH=$ICET_ROOT/lib:$LD_LIBRARY_PATH

  export JANSSON_ROOT=/opt/jansson/2.9.0/
  export CMAKE_PREFIX_PATH=$JANSSON_ROOT/lib/cmake:$CMAKE_PREFIX_PATH
  export LD_LIBRARY_PATH=$JANSSON_ROOT/lib:$LD_LIBRARY_PATH

  export ISAAC_ROOT=/opt/isaac/1.6.0-dev-custom
  # install cusom version of isaac
  source $CI_PROJECT_DIR/share/ci/install/isaac.sh

  export CMAKE_PREFIX_PATH=$ISAAC_ROOT:$CMAKE_PREFIX_PATH
  export LD_LIBRARY_PATH=$ISAAC_ROOT/lib:$LD_LIBRARY_PATH
fi

export OPENPMD_ROOT=/opt/openPMD-api/0.13.2
export CMAKE_PREFIX_PATH=$OPENPMD_ROOT:$CMAKE_PREFIX_PATH
export LD_LIBRARY_PATH=$OPENPMD_ROOT/lib:$LD_LIBRARY_PATH
