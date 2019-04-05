GITHUB_URL_ROC=(\
"https://github.com/RadeonOpenCompute/ROCm.git" \
"https://github.com/RadeonOpenCompute/ROCm-docker.git" \
"https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver.git" \
"https://github.com/RadeonOpenCompute/ROCm_Documentation.git" \
"https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface.git" \
)

GITHUB_URL_ROCM=(\
https://github.com/ROCmSoftwarePlatform/MIOpen.git \
https://github.com/ROCmSoftwarePlatform/rocBLAS.git \
https://github.com/ROCmSoftwarePlatform/rocFFT.git \
https://github.com/ROCmSoftwarePlatform/rocRAND.git \
https://github.com/ROCmSoftwarePlatform/rocPRIM.git \
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream.git \
https://github.com/ROCmSoftwarePlatform/pytorch.git \
https://github.com/ROCmSoftwarePlatform/hipBLAS.git \
https://github.com/ROCmSoftwarePlatform/hipCaffe.git \
https://github.com/ROCmSoftwarePlatform/benchmarks \
https://github.com/ROCmSoftwarePlatform/DeepBench.git \
)

GITHUB_URL_NON_AMD=(\
https://github.com/xianyi/OpenBLAS.git \
https://github.com/tensorflow/tensorflow \
https://github.com/pytorch/pytorch.git \
https://github.com/pytorch/caffe2.github.io.git \
https://github.com/tensorflow/benchmarks.git \
https://github.com/baidu-research/DeepBench \
)

GITHUB_URL_BENCHMARKS=(\
https://github.com/baidu-research/DeepBench.git \
)

mkdir roc
cd roc

for i in ${GITHUB_URL_ROC[@]}
do
        if [[ ! -f $i ]] ; then
                echo "-- git cloning ${i}..."
                git clone ${i}
        else
                echo "-- already checked out..."
        fi
done

cd ..
mkdir rocm
cd rocm

for i in ${GITHUB_URL_ROCM[@]}
do
        if [[ ! -f $i ]] ; then
                echo "-- git cloning ${i}..."
                git clone ${i}
        else
                echo "-- already checked out..."
        fi
done

cd ..
mkdir non-amd 
cd non-amd

for i in ${GITHUB_URL_NON_AMD[@]}
do
	echo "git cloning ${i}..."
	git clone ${i}
done

cd ..
mkdir benchmarks
cd benchmarks

for i in ${GITHUB_URL_BENCHMARKS[@]}
do
	echo "git cloning ${i}..."
	git clone ${i}
done
cd ..
ls -ltr



