

runtime env

python3.5.3 
PyQt 5.10




brew install opencv3 --with-python3 --c++11 --with-contrib

brew unlink opencv3 && brew link --force opencv3

ll /usr/local/Cellar
cd ~/Documents/pyenv/cr-py3/lib/python3.5/site-packages/

ln -s ll /usr/local/Cellar/opencv/3.4.0_1/lib/python3.6/site-packages/cv2.cpython-36m-darwin.so cv2.so
ln -s /usr/local/Cellar/opencv/3.4.0_1/lib/python3.6/site-packages/cv2.cpython-36m-darwin.so cv2.so

pip install --upgrade numpy
