#!/bin/bash
if test -f ../../QuetzalcoatlProto/invoicing/decrypt-local-secret-enduser.sh; then
    echo ../../QuetzalcoatlProto/invoicing/decrypt-local-secret-enduser.sh
    pushd ../../QuetzalcoatlProto/invoicing/
    source ./decrypt-local-secret-enduser.sh
    popd
fi

if test -f ../../../QuetzalcoatlProto/invoicing/decrypt-local-secret-enduser.sh; then
    echo ../../../QuetzalcoatlProto/invoicing/decrypt-local-secret-enduser.sh
    pushd ../../../QuetzalcoatlProto/invoicing/
    source ./decrypt-local-secret-enduser.sh
    popd
fi

echo $QUETZALCOATL_USER1

if [ -f $HOME/anaconda3/etc/profile.d/conda.sh ]; then
    source $HOME/anaconda3/etc/profile.d/conda.sh
else
    source $HOME/miniforge3/etc/profile.d/conda.sh
fi

conda activate vqe-ml2
conda activate qiskit

for i in simpleTest24N*.py; do
    echo $i;
    QUETZALCOATL_USER1=$QUETZALCOATL_USER1 QUETZALCOATL_TOKEN1=$QUETZALCOATL_TOKEN1 time python $i || exit -1;
done
