#### Here is how I set up my environment for running Keras with GPU

Install Python 3.5 and pip if you do not already have it

##### If you want GPU, you'll need CUDA and cuDNN
Install CUDA 8.0
Install cuDNN 5

#### Install virtualenv if you don't already have it
`pip install virtualenv`

#### Create a location for virtualenvs. I prefer to put mine at ~/ve/, this location is not critical
```bash
mkdir ~/ve
cd ~/ve
```

#### Create a VE for Keras install. Use the -p flag to specify python3. 
Note: depending on your env, you may need to specify python3.5 explicitly
```bash
virtualenv -p `which python3` keras
```
#### Install essentials
```bash
pip install numpy scipy pandas jupyter
```
#### Install Tensorflow.
##### For GPU users:
```bash
pip install tensorflow-gpu
```
##### For CPU Users:
```bash
pip install tensorflow
```
Note: I was able to do this with the very simple pip call. 
The Tensorflow install instructions used to call for pointed to a specific TF_BINARY_URL, but it seems that is no longer necessary

#### Verify CUDA connection
```bash
ipython
```

```python
In [1]: import tensorflow

I tensorflow/stream_executor/dso_loader.cc:135] successfully opened CUDA library libcublas.so.8.0 locally
I tensorflow/stream_executor/dso_loader.cc:135] successfully opened CUDA library libcudnn.so.5 locally
I tensorflow/stream_executor/dso_loader.cc:135] successfully opened CUDA library libcufft.so.8.0 locally
I tensorflow/stream_executor/dso_loader.cc:135] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:135] successfully opened CUDA library libcurand.so.8.0 locally

In [2]: import keras
Using TensorFlow backend.
```
#### After this, I also like to pull up a small Keras model and train it while watching my GPU to make sure it hasn't defaulted to CPU mode (it does this sometimes and it drives me nuts!)
```bash
watch -n1 nvidia-smi
```
