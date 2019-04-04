#       Runs all 4 tensorflow benchmark. This is to be run from the root directory of 
#	https://github.com/tensorflow/benchmarks.git.



MODELS=(resnet50 inception3 vgg16 resnet152)

for i in ${MODELS[@]}
do
	python tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=$i --variable_update=parameter_server > $i.log
done












